# Problem with importing APIClient

# import pytest
# import requests
# import json

# from src.gamequeue_planner.models.APIClient import APIClient
# from src.gamequeue_planner.models.platform_ids import platform_ids
# from src.gamequeue_planner.models.GameObject import GameObject
# from src.gamequeue_planner.models.ConstRes import ConstRes

# # Mock data
# mock_api_response = {
#     ConstRes.GAMES.value: [
#         {
#             ConstRes.TITLE.value: "Test Game",
#             ConstRes.GAME_ID.value: 1,
#             ConstRes.MOBY_SCORE.value: 85,
#             ConstRes.NUM_VOTES.value: 100,
#             ConstRes.GENRES.value: [{ConstRes.GENRE_NAME.value: "Action"}],
#             ConstRes.PLATFORMS.value: [
#                 {
#                     ConstRes.PLATFORM_NAME.value: "Test Platform",
#                     ConstRes.FIRST_RELEASE_DATE.value: "2021-01-01",
#                     ConstRes.PLATFORM_ID.value: 123
#                 }
#             ]
#         }
#     ]
# }

# mock_config = json.dumps({
#     ConstRes.API_KEY.value: "test_api_key"
# })

# @pytest.fixture
# def api_client():
#     return APIClient()

# def mock_requests_get(url, params):
#     class MockResponse:
#         def json(self):
#             return mock_api_response
#     return MockResponse()

# @pytest.fixture
# def mock_config_file(monkeypatch):
#     def mock_open(filename, mode='r'):
#         if filename == ConstRes.CONFIG_FILE_NAME.value:
#             return mock_config
#         raise FileNotFoundError

#     monkeypatch.setattr('builtins.open', lambda f, mode='r': mock_open(f, mode))
#     monkeypatch.setattr('json.load', lambda f: json.loads(f))
    
# def test_get_data(api_client, monkeypatch):
#     monkeypatch.setattr(requests, 'get', mock_requests_get)
#     data = api_client.get_data("test_api_key", 1)
#     assert data == mock_api_response[ConstRes.GAMES.value]

# def test_check_if_game_is_a_dlc_or_limited_edition(api_client):
#     game = GameObject()
#     api_client.check_if_game_is_a_dlc_or_limited_edition(game, ConstRes.ADD_ON.value)
#     assert game.is_DLC
#     api_client.check_if_game_is_a_dlc_or_limited_edition(game, ConstRes.SPECIAL_EDITION.value)
#     assert game.is_special_edition

# def test_fetch_data_from_API(api_client, mock_config_file, monkeypatch):
#     monkeypatch.setattr(requests, 'get', mock_requests_get)
#     platform_ids["Test Platform"] = 1  # Add test platform ID to platform_ids
#     games = api_client.fetch_data_from_API("Test Platform")
#     assert len(games) == 1
#     assert games[0].title == "Test Game"
#     assert games[0].game_id == 1
#     assert games[0].moby_score == 85
#     assert games[0].moby_num_votes == 100
#     assert games[0].platform_name == "Test Platform"

# def test_fetch_data_from_API_handles_multiple_calls(api_client, mock_config_file, monkeypatch):
#     def mock_requests_get_multiple(url, params):
#         class MockResponse:
#             def json(self):
#                 if params['offset'] == 0:
#                     return mock_api_response
#                 else:
#                     return {ConstRes.GAMES.value: []}
#         return MockResponse()

#     monkeypatch.setattr(requests, 'get', mock_requests_get_multiple)
#     platform_ids["Test Platform"] = 1
#     games = api_client.fetch_data_from_API("Test Platform")
#     assert len(games) == 1
#     assert games[0].title == "Test Game"
