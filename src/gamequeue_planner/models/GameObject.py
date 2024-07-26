from common.LoggerSingleton import LoggerSingleton

class GameObject(object):
    
    def __init__(self,
                 title='',
                 game_id='',
                 moby_score='', 
                 moby_num_votes='',
                 first_release_date='', 
                 platform_name='',
                 platform_id='',
                 is_DLC=False,
                 is_special_edition=False):
        
        self.title = title
        self.game_id = game_id
        self.moby_score = moby_score
        self.moby_num_votes = moby_num_votes
        self.first_release_date = first_release_date
        self.platform_name = platform_name
        self.platform_id = platform_id
        self.is_DLC = is_DLC
        self.is_special_edition=is_special_edition
        self.logger = LoggerSingleton()
        
    def print_and_log_details(self):
        print(f"title: {self.title}")
        print(f"game id: {self.game_id}")
        print(f"moby score: {self.moby_score}")
        print(f"moby num votes: {self.moby_num_votes}")
        print(f"first release date: {self.first_release_date}")
        print(f"platform name: {self.platform_name}")
        print(f"platform id: {self.platform_id}\n")

        self.logger.log_info(f"DETAIL - title: {self.title}")
        self.logger.log_info(f"DETAIL - game id: {self.game_id}")
        self.logger.log_info(f"DETAIL - moby score: {self.moby_score}")
        self.logger.log_info(f"DETAIL - moby num votes: {self.moby_num_votes}")
        self.logger.log_info(f"DETAIL - first release date: {self.first_release_date}")
        self.logger.log_info(f"DETAIL - platform name: {self.platform_name}")
        self.logger.log_info(f"DETAIL - platform id: {self.platform_id}")
        self.logger.log_info(f"DETAIL - dlc: {self.is_DLC}")
        self.logger.log_info(f"DETAIL - special edition: {self.is_special_edition}\n")