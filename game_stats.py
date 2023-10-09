class GameStats:
    def __init__(self,ai_game):
        self.settings=ai_game.settings
        self.score_bonus=50
        self.high_score=0
        self.reset_stats()
    def reset_stats(self):
        self.ships=self.settings.ship_limit
        self.score=0
        self.game_level = 1