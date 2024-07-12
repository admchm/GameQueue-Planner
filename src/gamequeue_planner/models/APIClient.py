import requests
from pprint import pprint
from models.platforms import platforms

class APIClient(object):
    
    def fetch_data_from_API(self):
        print("##################")
        api_url = "https://api.mobygames.com/v1/games/37067?format=normal&api_key=moby_"

        #req = requests.get(api_url)
        #data = req.json()
        #pprint(data)

        r = requests.get(api_url, params={
        "course_id": 1, "full": "true" })

        data = r.json()
        pprint(data)

#print(platforms["PlayStation"])