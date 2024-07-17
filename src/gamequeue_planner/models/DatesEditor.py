from datetime import datetime
from models.ConstRes import ConstRes

class DatesEditor(object):
        
    def fix_the_dates_if_needed(self, games_list):
        for game in games_list:
            if len(game.first_release_date) == ConstRes.FOUR_DIGITS.value:
                game.first_release_date += ConstRes.DEFAULT_MISSING_MONTH_AND_DAY.value
                
            elif len(game.first_release_date) == ConstRes.SEVEN_DIGITS.value:
                game.first_release_date += ConstRes.DEFAULT_MISSING_DAY.value
                
        return games_list
    
    def get_current_time(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime('_%Y-%m-%d')
        
        return formatted_time