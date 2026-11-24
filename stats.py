import json
import os

player_stats = {
    "games_played": 0,
    "wins": 0,
    "losses": 0,
    "lifetime_attempts": 0,
    "best_streak": 0,
    "best_attempts": 0
}

class Stats:

    def __init__(self):
        self.games_played = 0
        self.wins = 0
        self.losses = 0
        self.lifetime_attempts = 0
        self.best_streak = 0
        self.current_streak = 0
        self.best_attempts = 0

    def record_win(self, attempts): # records wins
        self.wins += 1
        self.current_streak += 1
        if self.current_streak > self.best_streak:
            self.best_streak = self.current_streak
        if self.best_attempts == 0 or attempts < self.best_attempts:
            self.best_attempts = attempts

    def record_loss(self, attempts): # records losses
        self.losses += 1
        self.current_streak = 0

    def record_game(self, attempts): # records games played
        self.games_played += 1
        self.lifetime_attempts += attempts

    def display_stats(self): # displays the statistics of the game
        print("\n--Number Guessing Game Statistics--")
        print(f"Games Played: {self.games_played}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Lifetime Attempts: {self.lifetime_attempts}")
        print(f"Best Streak: {self.best_streak}")
        print(f"Fewest Attempts: {self.best_attempts}")
        average_attempts = self.lifetime_attempts / self.games_played if self.games_played > 0 else 0
        print(f"Average Attempts per Game: {average_attempts:.2f}")

    def load_stats(self): # load stats
        if os.path.exists("stats.json"):
            with open("stats.json", "r") as file:
                data = json.load(file)
        else:
            data = player_stats.copy()

        self.games_played = data.get("games_played", 0)
        self.wins = data.get("wins", 0)
        self.losses = data.get("losses", 0)
        self.lifetime_attempts = data.get("lifetime_attempts", 0)
        self.best_streak = data.get("best_streak", 0)
        self.best_attempts = data.get("best_attempts", 0)
        print("Loaded stats:", self.games_played, self.wins, self.losses)

    def save_stats(self): # save stats
        data = {
            "games_played": self.games_played,
            "wins": self.wins,
            "losses": self.losses,
            "lifetime_attempts": self.lifetime_attempts,
            "best_streak": self.best_streak,
            "best_attempts": self.best_attempts
        }
        with open("stats.json", "w") as file:
            json.dump(data, file, indent=4)