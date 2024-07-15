#from datetime import datetime
from datetime import datetime

class GamesListEditor(object):
        
    def sort_by_date(self, games_list):
        for item in games_list:
            item.first_release_date = datetime.strptime(item.first_release_date, "%Y-%m-%d")
            
        games_list.sort(key=lambda x: x.first_release_date)
            
        # converting back to string
        for item in games_list:
            item.first_release_date = item.first_release_date.strftime("%Y-%m-%d")
            
        return games_list
        
        