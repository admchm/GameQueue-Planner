import pytest
from src.gamequeue_planner.models.GameObject import GameObject

def test_game_object_initialization():
    game = GameObject('Fifa 2007', '43242', 31, 2, '2006-10-09', 'PlayStation 2', 16, False, False)
    
    assert game.title == 'Fifa 2007'
    assert game.game_id == '43242'
    assert game.moby_score == 31
    assert game.moby_num_votes == 2
    assert game.first_release_date == '2006-10-09'
    assert game.platform_name == 'PlayStation 2'
    assert game.platform_id == 16
    assert game.is_DLC == False
    assert game.is_special_edition == False
    
def test_game_object_default_init():
    game = GameObject()
    
    assert game.title == ''
    assert game.game_id == ''
    assert game.moby_score =='' 
    assert game.moby_num_votes == ''
    assert game.first_release_date == '' 
    assert game.platform_name == ''
    assert game.platform_id == ''
    assert game.is_DLC == False
    assert game.is_special_edition == False
    
def test_game_object_print_details(capfd):
    game = GameObject('Fifa 2007', '43242', 31, 2, '2006-10-09', 'PlayStation 2', 16, False, False)
    
    game.print_and_log_details()
    captured = capfd.readouterr()
    
    expected_output = (
        "title: Fifa 2007\n"
        "game id: 43242\n"
        "moby score: 31\n"
        "moby num votes: 2\n"
        "first release date: 2006-10-09\n"
        "platform name: PlayStation 2\n"
        "platform id: 16\n\n"
    )
    
    assert captured.out == expected_output
    