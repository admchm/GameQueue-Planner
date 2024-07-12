class GameObject(object):
    
    def __init__(self, title='', game_id='', moby_score='', moby_num_votes='', first_release_date='', platform_name='', platform_id=''):
        self.title = title
        self.game_id = game_id
        self.moby_score = moby_score
        self.moby_num_votes = moby_num_votes
        self.first_release_date = first_release_date
        self.platform_name = platform_name
        self.platform_id = platform_id
        
    def print_details(self):
        print(f"title: {self.title}")
        print(f"game id: {self.game_id}")
        print(f"moby score: {self.moby_score}")
        print(f"moby num votes: {self.moby_num_votes}")
        print(f"first release date: {self.first_release_date}")
        print(f"platform name: {self.platform_name}")
        print(f"platform id: {self.platform_id}\n")