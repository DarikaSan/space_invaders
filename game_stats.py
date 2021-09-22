class GameStats:
    """Track statistics for Space Invaders"""

    def __init__(self, si_game):
        """Initialize statistics"""
        self.settings = si_game.settings
        self.reset_stats()

        # Startet Space Invaders im aktiven Zustand
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit