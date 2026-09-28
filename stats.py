class Stats:

    def __init__(self):
        self.games_played = 0
        self.wins = 0
        self.losses = 0
        self.lifetime_attempts = 0

    def record_win(self, attempts):
        self.games_played += 1
        self.wins += 1
        self.lifetime_attempts += attempts

    def record_loss(self, attempts):
        self.games_played += 1
        self.losses += 1
        self.lifetime_attempts += attempts

    def display_stats(self):
        print("\nNumber Guessing Game Statistics:")
        print(f"Games Played: {self.games_played}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Lifetime Attempts: {self.lifetime_attempts}")
        average_attempts = self.lifetime_attempts / self.games_played if self.games_played > 0 else 0
        print(f"Average Attempts per Game: {average_attempts:.2f}")