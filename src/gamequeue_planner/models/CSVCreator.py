import csv

class CSVCreator:
    def __init__(self):
        pass
    
    def process_file(self, games_list, path_combined):   
        try:
            with open(path_combined, mode='w', newline='') as file:
                self.__populate_file_with_data(games_list, file)
                
        except PermissionError:
            print(f"Error: Permission denied when trying to write to {path_combined}")
        except IOError as e:
            print(f"IOError: Permission denied when trying to write to {path_combined}")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        finally:
            file.close()
            print(f"LOG: Created file at: {path_combined}")    

    def __populate_file_with_data(self, games_list, file):
        try:
            writer = csv.writer(file)
            writer.writerow(["Title", "Platform name", "Release date", "Moby (votes)"])
                
            for item in games_list:
                data_to_append = [item.title, item.platform_name, item.first_release_date, f"{item.moby_score} ({item.moby_num_votes})"]
                writer.writerow(data_to_append)
        except csv.Error as e:
            print(f"ERROR: CSV error occured: {e}")