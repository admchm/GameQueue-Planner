import pytest

from datetime import datetime
from src.gamequeue_planner.models.GamesListEditor import GamesListEditor

# mocking single game (only partially)
class MockGame:
    def __init__(self, title, first_release_date):
        self.title = title
        self.first_release_date = first_release_date

@pytest.fixture
def game_list():
    return [
        MockGame("First game", "1991-03-21"),
        MockGame("Second game", "1989-02-02"),
        MockGame("Third game", "1990-03-07")
    ]
    
def test_sort_by_date(game_list):
    editor = GamesListEditor()
    sorted_games = editor.sort_by_date(game_list)
    
    assert [game.title for game in sorted_games] == ["Second game", "Third game", "First game"]