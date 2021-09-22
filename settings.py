class Settings():
    """A class to store all settings for Space Invaders"""

    def __init__(self):
        """Initialize the game's settings"""
        # Bildschirmeinstellungen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # schiffeinstellungen
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Geschosseinstellungen
        self.bullet_speed = 1.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Invasionsiffeinstellung
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Der Wert 1 für fleet_direction bedeutet "nach rechts", -1 "nach link "
        self.fleet_direction = 1