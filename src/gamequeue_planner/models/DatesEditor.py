from datetime import datetime
from models.ConstRes import ConstRes

class DatesEditor(object):
    def fix_the_dates_if_needed(self, games_list):
        
        for game in games_list:
            if not game.first_release_date: # if empty, setting default date
                game.first_release_date = ConstRes.DEFAULT_MISSING_YEAR_MONTH_AND_DAY.value
            
            if len(game.first_release_date) == ConstRes.FOUR_DIGITS.value:
                game.first_release_date += ConstRes.DEFAULT_MISSING_MONTH_AND_DAY.value
                
            elif len(game.first_release_date) == ConstRes.SEVEN_DIGITS.value:
                game.first_release_date += ConstRes.DEFAULT_MISSING_DAY.value
                
        return games_list
    
    def get_current_time_days(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d')
        
        return formatted_time
    
    def get_current_time_full(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        
        return formatted_time