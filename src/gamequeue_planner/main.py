import time

from models.Network.APIClient import APIClient
from models.Dates.DatesEditor import DatesEditor
from models.GameData.GamesListEditor import GamesListEditor
from models.Platform.Platform import Platform
from models.Files.FileExtensions import FileExtensions
from models.Files.FilenameCreator import FilenameCreator
from common.LoggerSingleton import LoggerSingleton

selected_platforms = [Platform.SEGA_32X.value]

# selected_platforms = [Platform.PSP.value, 
#                       Platform.Nintendo_DS.value, 
#                       Platform.Xbox_360.value, 
#                       Platform.PlayStation_3.value, 
#                       Platform.Wii_U.value, 
#                       Platform.Nintendo_3DS.value, 
#                       Platform.PS_Vita.value]

fetched_data = []
logger = LoggerSingleton()

def filter_data(filter_excluding_special_edition, filter_excluding_dlcs, fetched_data_with_correct_dates):
    partially_filtered_data = filter_excluding_special_edition(fetched_data_with_correct_dates)
    filtered_data = filter_excluding_dlcs(partially_filtered_data)
    
    return filtered_data

def filter_excluding_special_edition(fetched_data_with_correct_dates):
    return [game for game in fetched_data_with_correct_dates if not game.is_special_edition]

def filter_excluding_dlcs(partially_filtered_data):
    return [game for game in partially_filtered_data if not game.is_DLC]

def create_file_in_selected_format(sorted_data):
    file_extension = FileExtensions.EXCEL
    file = FilenameCreator()
    file.file_name = "MyFile"
    file.prepare_file(file_extension, sorted_data)

dates_editor = DatesEditor()
logger.log_info(f"Started at {dates_editor.get_current_time_full()}\n")

for platform in selected_platforms:
    client = APIClient()
    
    # TODO: - games_data will contain entire data for all, selected platforms.
    #         For now, it's okay, but it should be initialized again
    fetched_data = client.fetch_data_from_API(platform)
    time.sleep(10) # set sleep between new requests
 
fetched_data_with_correct_dates = dates_editor.fix_the_dates_if_needed(fetched_data)

filtered_data = filter_data(filter_excluding_special_edition, filter_excluding_dlcs, fetched_data_with_correct_dates)

games_list_editor = GamesListEditor()
sorted_data = games_list_editor.sort_by_date(filtered_data)

create_file_in_selected_format(sorted_data)

logger.log_info(f"Finished at {dates_editor.get_current_time_full()}")