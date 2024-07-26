import requests
import json
import time

from models.Platform.platform_ids import platform_ids
from models.GameData.GameObject import GameObject
from models.Constants.ConstRes import ConstRes
from common.LoggerSingleton import LoggerSingleton

class APIClient(object):
    
    def __init__(self, offset=0, limit=100, games_array=[]):
        self.offset = offset
        self.limit = limit
        self.games_array = games_array
        self.max_retries = 20
        self.logger = LoggerSingleton()
        
    def get_data(self, api_key, selected_platform_id):
        api_url = f"https://api.mobygames.com/v1/games?"
        
        for attempt in range(self.max_retries):
            try:
                r = requests.get(api_url, params={
                                    "platform": selected_platform_id,
                                    "format": "normal",
                                    "offset": self.offset,
                                    "api_key": api_key})
                r.raise_for_status() # raises HTTPError for bad responses
            
                data = r.json()
                
                if ConstRes.GAMES.value in data:
                    return data[ConstRes.GAMES.value]
                else:
                    self.logger.log_warning("Key 'games' not found in the response. Attempting again.")
                    time.sleep(5)
                    continue        
        
            except requests.exceptions.RequestException as e:
                self.logger.log_exception("ERROR: An error occurred while making a request to the API", e)
                
            except json.JSONDecodeError as e:
                self.logger.log_exception("ERROR: An error occured while decoding JSON response", e)
                
            except KeyError as e:
                self.logger.log_exception("ERROR: Missing key in JSON response", e)
                
            if attempt < self.max_retries - 1:
                self.logger.log_warning("Another attempt for fetching data...")
                time.sleep(5)
            else:
                return []
    
    def check_if_game_is_a_dlc_or_limited_edition(self, single_game, genre_name):
        if genre_name == ConstRes.ADD_ON.value:
            single_game.is_DLC = True
                    
        elif genre_name == ConstRes.SPECIAL_EDITION.value:
            single_game.is_special_edition = True
    
    def fetch_data_from_API(self, selected_platform):
        with open(ConstRes.CONFIG_FILE_NAME.value, 'r') as config_file:
            config = json.load(config_file)
        api_key = config[ConstRes.API_KEY.value]
        
        selected_platform_id = platform_ids[selected_platform]
        
        while True:
            data = self.get_data(api_key, selected_platform_id)
            
            if not data:
                break
            
            for game in data:            
                single_game = GameObject()
                single_game.title = game[ConstRes.TITLE.value]
                
                single_game.game_id = game[ConstRes.GAME_ID.value]
                single_game.moby_score = game[ConstRes.MOBY_SCORE.value]
                single_game.moby_num_votes = game[ConstRes.NUM_VOTES.value]
                
                genres = game[ConstRes.GENRES.value]              # nested data
                genre_name = genres[0][ConstRes.GENRE_NAME.value]
                
                self.check_if_game_is_a_dlc_or_limited_edition(single_game, genre_name)
                
                platform_details = game[ConstRes.PLATFORMS.value] # nested data
                
                i = 0 
                platform_not_found = True
                
                 # making sure that index won't get out of range. 
                 # data on mobygames is not perfect, so we need to
                 # make sure that we won't get a crash
                for i in range(len(platform_details)):
                    if platform_details[i][ConstRes.PLATFORM_NAME.value] == selected_platform:
                        single_game.first_release_date = platform_details[i][ConstRes.FIRST_RELEASE_DATE.value]
                        single_game.platform_name = platform_details[i][ConstRes.PLATFORM_NAME.value]
                        single_game.platform_id = platform_details[i][ConstRes.PLATFORM_ID.value]
                        platform_not_found = False
                    else:
                        i += 1
                                        
                single_game.print_and_log_details()
                self.games_array.append(single_game)
                
            time.sleep(10)
            self.offset += self.limit
        
        self.logger.log_info("Finished downloading data for a platform\n")
        return self.games_array