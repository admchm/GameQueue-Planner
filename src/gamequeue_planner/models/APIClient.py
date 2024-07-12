import requests
import json

from models.platforms import platforms
from models.GameObject import GameObject

class APIClient(object):
    def fetch_data_from_API(self):
        with open('config_file.json', 'r') as config_file:
            config = json.load(config_file)
        api_key = config['api_key']
        
        #selected_platform = "SEGA Saturn"
        #selected_platform_id = platforms['SEGA Saturn']
        
        selected_platform = "SNES"
        selected_platform_id = platforms['SNES']
        
        #selected_platform = "Nintendo DS"
        #selected_platform_id = platforms['Nintendo DS']
        
        print(selected_platform_id)
        
        #api_url = f"https://api.mobygames.com/v1/games/37067?format=normal&api_key={api_key}"
        api_url = f"https://api.mobygames.com/v1/games/78?format=normal&api_key={api_key}"

        #req = requests.get(api_url)
        #data = req.json()
        #pprint(data)

        r = requests.get(api_url, params={
        "course_id": 1, "full": "true" })

        data = r.json()
              
        single_game = GameObject()
        single_game.title = data['title']
        single_game.game_id = data['game_id']
        single_game.moby_score = data['moby_score']
        single_game.moby_num_votes = data['num_votes']

        platform_details = data['platforms'] # getting nested data
        
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
        
        return single_game