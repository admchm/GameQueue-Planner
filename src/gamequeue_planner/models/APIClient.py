import requests
import json
import time

from models.platform_ids import platform_ids
from models.GameObject import GameObject
from models.ConstRes import ConstRes

class APIClient(object):
    
    def __init__(self, offset=1000, limit=100, games_array=[]):
        self.offset = offset
        self.limit = limit
        self.games_array = games_array
    
    def fetch_data_from_API(self, selected_platforms):
        with open(ConstRes.CONFIG_FILE_NAME.value, 'r') as config_file:
            config = json.load(config_file)
        api_key = config[ConstRes.API_KEY.value]
        
        selected_platform_id = platform_ids[selected_platforms]
        
        while True:
            api_url = f"https://api.mobygames.com/v1/games?platform={selected_platform_id}&format=normal&offset={self.offset}&api_key={api_key}"
            
            r = requests.get(api_url)
            data = r.json()[ConstRes.GAMES.value]
            
            if not data:
                break
            
            for game in data:            
                single_game = GameObject()
                single_game.title = game[ConstRes.TITLE.value]
                
                single_game.game_id = game[ConstRes.GAME_ID.value]
                single_game.moby_score = game[ConstRes.MOBY_SCORE.value]
                single_game.moby_num_votes = game[ConstRes.NUM_VOTES.value]
                platform_details = game[ConstRes.PLATFORMS.value] # getting nested data
                
                i = 0 
                platform_not_found = True
                
                while platform_not_found:
                    if platform_details[i][ConstRes.PLATFORM_NAME.value] == selected_platforms:
                        single_game.first_release_date = platform_details[i][ConstRes.FIRST_RELEASE_DATE.value]
                        single_game.platform_name = platform_details[i][ConstRes.PLATFORM_NAME.value]
                        single_game.platform_id = platform_details[i][ConstRes.PLATFORM_ID.value]
                        platform_not_found = False
                    else:
                        i += 1
                        
                single_game.print_details()
                self.games_array.append(single_game)
                
            time.sleep(10)
            self.offset += self.limit
        
        return self.games_array