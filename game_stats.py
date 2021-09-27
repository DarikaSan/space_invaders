class GameStats:
    """Track statistics for Space Invaders"""

    def __init__(self, si_game):
        """Initialize statistics"""
        self.settings = si_game.settings
        self.reset_stats()

        # Startet Space Invaders im aktiven Zustand
        self.game_active = False
        # Der Hightscore darf nie zurückgesetzt werden 
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
