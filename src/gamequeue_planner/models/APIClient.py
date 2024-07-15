import requests
import json
import time
import pandas as pd

from models.Platform import Platform
from models.platform_ids import platform_ids
from models.GameObject import GameObject
from models.CSVCreator import CSVCreator
from models.DatesEditor import DatesEditor

class APIClient(object):
    # TODO: - move this function to a GamesObject class or something similar
    # def sort_objects(self, games_array):
    #     df = pd.DataFrame(games_array)
    #     df['first_release_date'] = pd.to_datetime(df['first_release_date'])
    #     df = df.sort_values(by='first_release_date')
        
    #     return df
    
    def fetch_data_from_API(self):
        with open('config_file.json', 'r') as config_file:
            config = json.load(config_file)
        api_key = config['api_key']
        
        selected_platform = Platform.SNES.value
        selected_platform_id = platform_ids[selected_platform]

        #r = requests.get(api_url, params={
        #"course_id": 1, "full": "true" })
        
        #offset = 0
        offset = 1200
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
        
        dates_editor = DatesEditor()
        games_array = dates_editor.fix_the_dates_if_needed(games_array)
        # sorted_items = self.sort_objects(games_array)
        
        csv = CSVCreator()
        csv.prepare_file(games_array)