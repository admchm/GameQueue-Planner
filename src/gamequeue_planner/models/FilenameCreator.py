import os
from models.DatesEditor import DatesEditor
from models.FileExtensions import FileExtensions
from models.CSVCreator import CSVCreator
from models.ExcelFileCreator import ExcelFileCreator

class FilenameCreator(object):
    def __init__(self, path = '~/', file_name = 'Games_list', path_combined = ''):
        self.path = path
        self.file_name = file_name
        self.path_combined = path_combined
        
    def prepare_file(self, file_extension, games_list):
        if file_extension == FileExtensions.CSV:
            self.set_file_name(self.file_name + ".csv")
            self.process_file_name()
            
            csv = CSVCreator()
            csv.process_file(games_list, self.path_combined)
            
        elif file_extension == FileExtensions.EXCEL:
            self.set_file_name(self.file_name + ".xlsx")
            self.process_file_name()
            
            excel = ExcelFileCreator()
            excel.process_file(games_list, self.path_combined)
        
    def process_file_name(self):
        self.set_path("~/")
        self.add_date_to_file_name()
        self.combine_path_with_file_name()
        
    def set_path(self, path):
        self.path = path
        
    def set_file_name(self, file_name):
        self.file_name = file_name
        
    def add_date_to_file_name(self):
        index = self.file_name.find('.') # inserting before .xlsx
        time = DatesEditor.get_current_time_days(self)
        
        if index == -1:
            return self.file_name
        
        self.file_name = self.file_name[:index] + '_' + time + self.file_name[index:]
                
    def combine_path_with_file_name(self):
        self.path_combined = os.path.expanduser(f"{self.path + self.file_name}")