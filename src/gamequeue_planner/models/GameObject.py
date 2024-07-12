class GameObject(object):
    
    def _init__(self, title, game_id, first_release_date, moby_score, moby_num_votes, platform_name, platform_id):
        self.title = title
        self.game_id = game_id
        self.first_release_date = first_release_date
        self.moby_score = moby_score
        self.moby_num_votes = moby_num_votes
        self.platform_name = platform_name
        self.platform_id = platform_id
        
    def print_details(self):
        print("Fetched data:")
        print(f"title: {self.title}")