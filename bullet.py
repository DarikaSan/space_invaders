import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, si_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = si_game.screen
        self.self.settings = si_game.settings
        self.color = self.settings.bullet_color

        # Erstellt ein Geschossrechteck bei (0, 0) und legt dann die richtige 
        # Position fest
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.recht.midtop = si_game.ship.rect.midtop

        # Speichert die Position des geschosses als Fließkommawert
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Aktualisiert die Flieskommaposition des Geschosses 
        self.y -= self.settings.bullet_speed
        # Aktualisiert die Position des Rechtecks 
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)