from enum import Enum

class ConstRes(Enum):
    
    # constant numbers
    FOUR_DIGITS = 4
    SEVEN_DIGITS = 7
    
    # default string values for missing days/months in fetched data
    DEFAULT_MISSING_DAY = "-01"
    DEFAULT_MISSING_MONTH_AND_DAY = "-12-01"
    DEFAULT_MISSING_YEAR_MONTH_AND_DAY = "2000-01-01"
    
    # JSON data constants from APIClient
    TITLE = "title"
    GAME_ID = "game_id"
    MOBY_SCORE = "moby_score"
    NUM_VOTES = "num_votes"
    PLATFORMS = "platforms"
    PLATFORM_NAME = "platform_name"
    PLATFORM_ID = "platform_id"
    FIRST_RELEASE_DATE = "first_release_date"
    GAMES = "games"
    GENRES = "genres"
    GENRE_NAME = "genre_name"
    
    # genre names
    ADD_ON = "Add-on"
    SPECIAL_EDITION = "Special edition"
    
    # filenames
    CONFIG_FILE_NAME = "config_file.json"
    
    # general constants
    API_KEY = "api_key"