import time

from models.APIClient import APIClient
from models.DatesEditor import DatesEditor
from models.GamesListEditor import GamesListEditor
from models.CSVCreator import CSVCreator
from models.Platform import Platform

selected_platforms = [Platform.PSP.value, Platform.Nintendo_DS.value]
fetched_data = []

for platform in selected_platforms:
    client = APIClient()
    
    # TODO: - games_data will contain entire data for all, selected platforms.
    #         For now, it's okay, but it should be initialized again
    fetched_data = client.fetch_data_from_API(platform)
    time.sleep(10) # set sleep between new requests
 
dates_editor = DatesEditor()
fetched_data_with_correct_dates = dates_editor.fix_the_dates_if_needed(fetched_data)
 
games_list_editor = GamesListEditor()
sorted_data = games_list_editor.sort_by_date(fetched_data_with_correct_dates)

csv = CSVCreator()
csv.set_path("~/")
csv.set_file_name("Games_list.csv")
csv.prepare_file(sorted_data)