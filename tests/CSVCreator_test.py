# import pytest
# import os
# import csv
# from src.gamequeue_planner.models.CSVCreator import CSVCreator
# from src.gamequeue_planner.models.DatesEditor import DatesEditor

# @pytest.fixture
# def sample_games_list():
#     class Game:
#         def __init__(self, title, platform_name, first_release_date, moby_score, moby_num_votes):
#             self.title = title
#             self.platform_name = platform_name
#             self.first_release_date = first_release_date
#             self.moby_score = moby_score
#             self.moby_num_votes = moby_num_votes

#     return [
#         Game('Game1', 'Platform1', '2022-01-01', 85, 100),
#         Game('Game2', 'Platform2', '2023-01-01', 90, 150)
#     ]

# @pytest.fixture
# def mock_get_current_time(monkeypatch):
#     mock_time = "_20220719"
#     monkeypatch.setattr(DatesEditor, 'get_current_time', lambda self: mock_time)
#     return mock_time

# def test_add_date_to_file_name(mock_get_current_time):
#     csv_creator = CSVCreator(file_name='GameQueue.csv')
#     csv_creator.add_date_to_file_name()
#     assert csv_creator.file_name == f'GameQueue{mock_get_current_time}.csv'

# def test_set_path():
#     csv_creator = CSVCreator()
#     csv_creator.set_path('/new/path/')
#     assert csv_creator.path == '/new/path/'

# def test_set_file_name():
#     csv_creator = CSVCreator()
#     csv_creator.set_file_name('NewFile.csv')
#     assert csv_creator.file_name == 'NewFile.csv'

# def test_combine_path_with_file_name():
#     csv_creator = CSVCreator(path='/new/path/', file_name='GameQueue.csv')
#     csv_creator.combine_path_with_file_name()
#     assert csv_creator.path_combined == os.path.expanduser('/new/path/GameQueue.csv')

# def test_prepare_file_success(monkeypatch, sample_games_list):
#     mock_open_file = mock_open()
#     monkeypatch.setattr('builtins.open', mock_open_file)
    
#     csv_creator = CSVCreator(path='/new/path/', file_name='GameQueue.csv')
#     csv_creator.prepare_file(sample_games_list)
    
#     mock_open_file.assert_called_once_with(csv_creator.path_combined, mode='w', newline='')
#     handle = mock_open_file()
#     handle.write.assert_any_call("Title,Platform name,Release date,Moby (votes)\n")
#     handle.write.assert_any_call("Game1,Platform1,2022-01-01,85 (100)\n")
#     handle.write.assert_any_call("Game2,Platform2,2023-01-01,90 (150)\n")

# def test_prepare_file_permission_error(monkeypatch):
#     monkeypatch.setattr('builtins.open', lambda *args, **kwargs: (_ for _ in ()).throw(PermissionError))
    
#     csv_creator = CSVCreator(path='/new/path/', file_name='GameQueue.csv')
#     games_list = []
    
#     with patch('builtins.print') as mocked_print:
#         csv_creator.prepare_file(games_list)
#         mocked_print.assert_any_call(f"Error: Permission denied when trying to write to {csv_creator.path_combined}")

# def test_prepare_file_io_error(monkeypatch):
#     monkeypatch.setattr('builtins.open', lambda *args, **kwargs: (_ for _ in ()).throw(IOError))
    
#     csv_creator = CSVCreator(path='/new/path/', file_name='GameQueue.csv')
#     games_list = []
    
#     with patch('builtins.print') as mocked_print:
#         csv_creator.prepare_file(games_list)
#         mocked_print.assert_any_call(f"IOError: Permission denied when trying to write to {csv_creator.path_combined}")

# def test_add_date_to_file_name_no_extension(mock_get_current_time):
#     csv_creator = CSVCreator(file_name='GameQueue')
#     csv_creator.add_date_to_file_name()
#     assert csv_creator.file_name == 'GameQueue'

# def test_prepare_file_unexpected_error(monkeypatch):
#     monkeypatch.setattr('builtins.open', lambda *args, **kwargs: (_ for _ in ()).throw(Exception("Unexpected error")))
    
#     csv_creator = CSVCreator(path='/new/path/', file_name='GameQueue.csv')
#     games_list = []
    
#     with patch('builtins.print') as mocked_print:
#         csv_creator.prepare_file(games_list)
#         mocked_print.assert_any_call("An unexpected error occured: Unexpected error")

# if __name__ == '__main__':
#     pytest.main()
