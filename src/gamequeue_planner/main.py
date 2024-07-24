import time

from models.APIClient import APIClient
from models.DatesEditor import DatesEditor
from models.GamesListEditor import GamesListEditor
from models.CSVCreator import CSVCreator
from models.Platform import Platform
from models.SelectedFileFormat import SelectedFileFormat
from models.ExcelFileCreator import ExcelFileCreator

#selected_platforms = [Platform.PSP.value, Platform.Nintendo_DS.value]
selected_platforms = [Platform.SEGA_32X.value, Platform.SEGA_CD.value]

fetched_data = []

def filter_excluding_special_edition(fetched_data_with_correct_dates):
    return [game for game in fetched_data_with_correct_dates if not game.is_special_edition]

def filter_excluding_dlcs(partially_filtered_data):
    return [game for game in partially_filtered_data if not game.is_DLC]

for platform in selected_platforms:
    client = APIClient()
    
    # TODO: - games_data will contain entire data for all, selected platforms.
    #         For now, it's okay, but it should be initialized again
    fetched_data = client.fetch_data_from_API(platform)
    time.sleep(10) # set sleep between new requests
 
dates_editor = DatesEditor()
fetched_data_with_correct_dates = dates_editor.fix_the_dates_if_needed(fetched_data)
 

# TODO: - both functions are temporary and will be removed after implementing database
partially_filtered_data = filter_excluding_special_edition(fetched_data_with_correct_dates)
filtered_data = filter_excluding_dlcs(partially_filtered_data)

games_list_editor = GamesListEditor()
sorted_data = games_list_editor.sort_by_date(filtered_data)

file_extension = SelectedFileFormat.EXCEL

if file_extension == SelectedFileFormat.CSV:
    csv = CSVCreator()
    csv.set_path("~/")
    csv.set_file_name("Games_list.csv")
    csv.prepare_file(sorted_data)
    
elif file_extension == SelectedFileFormat.EXCEL:
    excel = ExcelFileCreator()
    excel.set_path("~/")
    excel.set_file_name("Games_list.xlsx")
    excel.prepare_file(sorted_data)
    