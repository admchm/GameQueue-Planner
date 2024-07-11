from pprint import pprint
import requests

from models.platforms import platforms

api_url = "https://api.mobygames.com/v1/games/37067?format=normal&api_key="

req = requests.get(api_url)
data = req.json()

pprint(data)

# alter this code tomorrow
r = requests.get(api_url, params={
    "course_id": 1, "full": "true" })

data = r.json()
pprint(data)


#print(platforms["PlayStation"])