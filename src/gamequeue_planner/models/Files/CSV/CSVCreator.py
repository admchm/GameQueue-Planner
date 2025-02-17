import csv

from common.LoggerSingleton import LoggerSingleton

class CSVCreator:
    def __init__(self):
        self.logger = LoggerSingleton()
    
    def process_file(self, games_list, path_combined, additional_columns):   
        try:
            with open(path_combined, mode='w', newline='') as file:
                self.__populate_file_with_data(games_list, file, additional_columns)
                
        except PermissionError as e:
            self.logger.log_exception(f"ERROR: Permission denied when trying to write to {path_combined}", e)
        except IOError as e:
            self.logger.log_exception(f"ERROR: Permission denied when trying to write to {path_combined}", e)
        except Exception as e:
            self.logger.log_exception("ERROR: An unexpected error occured", e)
        finally:
            file.close()
            self.logger.log_info(f"Created file at: {path_combined}")
            print(f"Created file at: {path_combined}")

    def __populate_file_with_data(self, games_list, file, additional_columns):
        try:
            row = ["Title", "Platform name", "Release date", "Moby (votes)", "Genre"]
            
            for column in additional_columns:
                row.append(column)
            
            writer = csv.writer(file)
            writer.writerow(row)
            
            for item in games_list:
                data_to_append = [item.title, item.platform_name, item.first_release_date, f"{item.moby_score} ({item.moby_num_votes})", item.genre]
                writer.writerow(data_to_append)
        except csv.Error as e:
            self.logger.log_exception("ERROR: CSV error occured", e)