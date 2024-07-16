import requests
import json
import time

from models.Platform import Platform
from models.platform_ids import platform_ids
from models.GameObject import GameObject
from models.CSVCreator import CSVCreator
from models.DatesEditor import DatesEditor
from models.GamesListEditor import GamesListEditor

class APIClient(object):
    def fix_dates(self, games_array):
        dates_editor = DatesEditor()
        games_array = dates_editor.fix_the_dates_if_needed(games_array)
        
        return games_array
    
    def sort_data(self, games_array):
        games_list_editor = GamesListEditor()
        games_array = games_list_editor.sort_by_date(games_array)
        
        return games_array
    
    def create_CSV_file(self, games_array):
        csv = CSVCreator()
        csv.prepare_file(games_array)
    
    def fetch_data_from_API(self):
        with open('config_file.json', 'r') as config_file:
            config = json.load(config_file)
        api_key = config['api_key']
        
        selected_platform = Platform.Xbox_360.value
        selected_platform_id = platform_ids[selected_platform]

        offset = 0
        limit =  100    
        games_array = []
        
        while True:
            api_url = f"https://api.mobygames.com/v1/games?platform={selected_platform_id}&format=normal&offset={offset}&api_key={api_key}"
            
            r = requests.get(api_url)
            data = r.json()['games']
            
            if not data:
                break
            
            for game in data:            
                single_game = GameObject()
                single_game.title = game['title']
                
                single_game.game_id = game['game_id']
                single_game.moby_score = game['moby_score']
                single_game.moby_num_votes = game['num_votes']
                platform_details = game['platforms'] # getting nested data
                
                i = 0 
                platform_not_found = True
                
                while platform_not_found:
                    if platform_details[i]['platform_name'] == selected_platform:
                        single_game.first_release_date = platform_details[i]['first_release_date']
                        single_game.platform_name = platform_details[i]['platform_name']
                        single_game.platform_id = platform_details[i]['platform_id']
                        platform_not_found = False
                    else:
                        i += 1
                        
                single_game.print_details()
                games_array.append(single_game)
                
            time.sleep(10)
            offset += limit
        print(len(games_array))
        
        games_array = self.fix_dates(games_array)
        games_array = self.sort_data(games_array)
        self.create_CSV_file(games_array)