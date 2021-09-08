import pygame
import sys

from settings import Settings

class SpaceInvaders:
    """Overall class to manage game assest and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")

        #Legt die Hintergrundfarbe fest.
        self.bg_color = (230, 230,230)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Lauscht auf Tastatur- und Mausereignisse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Zeichnet den Bildschirm bei jedem Schleifendurchlauf neu.
            self.screen.fill(self.settings.bg_color)

            # Macht den zuletzt gezeichneten Bildschirm sichbar.
            pygame.display.flip()

if __name__ == '__main__':
    # Erstellteine Spielinstanz und führt das Spiel aus.
    si = SpaceInvaders()
    si.run_game()
