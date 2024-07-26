from datetime import datetime
from common.LoggerSingleton import LoggerSingleton

class GamesListEditor(object):
    def __init__(self):
        self.logger = LoggerSingleton()
        
    @staticmethod
    def valid_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except (ValueError, TypeError): # TypeError is used here for empty values
            return False
    
    def sort_by_date(self, games_list):
        self.logger.log_info("Sorting")
        valid_games_list = []
        
        for game in games_list:
            if self.valid_date(game.first_release_date):
                valid_games_list.append(game)
            else:
                self.logger.log_error(f"ERROR: Invalid date format found {game.first_release_date}")
        
        return sorted(valid_games_list, key=lambda x: datetime.strptime(x.first_release_date, '%Y-%m-%d'))
        