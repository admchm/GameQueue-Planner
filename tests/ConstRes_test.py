import pytest
from src.gamequeue_planner.models.ConstRes import ConstRes

def test_const_numbers():
    assert ConstRes.FOUR_DIGITS.value == 4
    assert ConstRes.SEVEN_DIGITS.value == 7

def test_const_default_date_strings():
    assert ConstRes.DEFAULT_MISSING_DAY.value == "-01"
    assert ConstRes.DEFAULT_MISSING_MONTH_AND_DAY.value == "-12-01"
    
def test_const_JSON_data():
    assert ConstRes.TITLE.value == "title"
    assert ConstRes.GAME_ID.value == "game_id"
    assert ConstRes.MOBY_SCORE.value == "moby_score"
    assert ConstRes.NUM_VOTES.value == "num_votes"
    assert ConstRes.PLATFORMS.value == "platforms"
    assert ConstRes.PLATFORM_NAME.value == "platform_name"
    assert ConstRes.PLATFORM_ID.value == "platform_id"
    assert ConstRes.FIRST_RELEASE_DATE.value == "first_release_date"
    assert ConstRes.GAMES.value == "games"
    assert ConstRes.GENRES.value == "genres"
    assert ConstRes.GENRE_NAME.value == "genre_name"
    
def test_const_genre_names():
    assert ConstRes.ADD_ON.value == "Add-on"
    assert ConstRes.SPECIAL_EDITION.value == "Special edition"

def test_const_file_names():
    assert ConstRes.CONFIG_FILE_NAME.value == "config_file.json"

def test_general_constants():
    assert ConstRes.API_KEY.value == "api_key"

def test_resources_immutable():
    with pytest.raises(AttributeError):
        ConstRes.CONFIG_FILE_NAME.value = "A new message"