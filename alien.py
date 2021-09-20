import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, si_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = si_game.screen 

        # Lädtdas bild des Invasionsschiffs und legt das rect-Attribut fest
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Platziert jedes neue Invasionsschiff oben links auf dem Bildschirm
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Speichert die genaue Position des Invasionsschiffes 
        self.x = float(self.rect.x)