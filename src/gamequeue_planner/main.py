from models.APIClient import APIClient
from models.DatesEditor import DatesEditor
from models.GamesListEditor import GamesListEditor
from models.CSVCreator import CSVCreator
from models.Platform import Platform

client = APIClient()
selected_platforms = Platform.SNES.value
games_data = client.fetch_data_from_API(selected_platforms)

dates_editor = DatesEditor()
dates_editor.fix_the_dates_if_needed(games_data)

games_list_editor = GamesListEditor()
games_array = games_list_editor.sort_by_date(games_data)

csv = CSVCreator()
csv.prepare_file(games_data)