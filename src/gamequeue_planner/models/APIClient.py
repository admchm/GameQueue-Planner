import requests
import json
from pprint import pprint
from models.platforms import platforms


class APIClient(object):
    def fetch_data_from_API(self):
        with open('config_file.json', 'r') as config_file:
            config = json.load(config_file)
        api_key = config['api_key']
        
        print("##################")
        api_url = f"https://api.mobygames.com/v1/games/37067?format=normal&api_key={api_key}"

        #req = requests.get(api_url)
        #data = req.json()
        #pprint(data)

        r = requests.get(api_url, params={
        "course_id": 1, "full": "true" })

        data = r.json()
        pprint(data)

#print(platforms["PlayStation"])