class Settings():
    """A class to store all settings for Space Invaders"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Bildschirmeinstellungen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # schiffeinstellungen
        self.ship_limit = 3
        # Geschosseinstellungen
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Invasionsiffeinstellung
        self.fleet_drop_speed = 7 # og drop 10
        # Stärke der Beschleunigung des Spiels
        self.speedup_scale = 1.05
        # Stärke der Punktewerterhöhung bei Treffern
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change thoughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.8 # og speed 1.0
        # Der Wert 1 für fleet_direction bedeutet "nach rechts", -1 "nach link "
        self.fleet_direction = 1
        # Punktwertung
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed += self.speedup_scale
        self.bullet_speed += self.speedup_scale
        self.alien_speed += self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)