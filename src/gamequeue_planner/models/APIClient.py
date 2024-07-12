import requests
import json

from models.platforms import platforms
from models.GameObject import GameObject

class APIClient(object):
    def fetch_data_from_API(self):
        with open('config_file.json', 'r') as config_file:
            config = json.load(config_file)
        api_key = config['api_key']
        
        api_url = f"https://api.mobygames.com/v1/games/37067?format=normal&api_key={api_key}"

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

        # TODO: - Possible error; verify the behavior for game that was released for a couple of platforms
        platform_details = data['platforms'] # getting nested data
        single_game.first_release_date = platform_details[0]['first_release_date']
        single_game.platform_name = platform_details[0]['platform_name']
        single_game.platform_id = platform_details[0]['platform_id']
        
        single_game.print_details()
        
        #pprint(data)

#print(platforms["PlayStation"])