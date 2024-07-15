from models.ConstRes import ConstRes

class DatesEditor(object):
        
    def fix_the_dates_if_needed(self, games_list):
        
        for game in games_list:
            if len(game.first_release_date) == ConstRes.four_digits.value:
                game.first_release_date += ConstRes.default_missing_month_and_day.value
                
            elif len(game.first_release_date) == ConstRes.seven_digits.value:
                game.first_release_date += ConstRes.default_missing_day.value
                
        return games_list