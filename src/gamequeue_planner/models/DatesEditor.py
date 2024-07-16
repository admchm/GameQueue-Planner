from models.ConstRes import ConstRes

class DatesEditor(object):
        
    def fix_the_dates_if_needed(self, games_list):
        for game in games_list:
            if len(game.first_release_date) == ConstRes.FOUR_DIGITS.value:
                game.first_release_date += ConstRes.DEFAULT_MISSING_MONTH_AND_DAY.value
                
            elif len(game.first_release_date) == ConstRes.SEVEN_DIGITS.value:
                game.first_release_date += ConstRes.DEFAULT_MISSING_DAY.value
                
        return games_list