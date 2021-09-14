import pygame

class Ship:
    def __init__(self, si_game):
        """Initialize the ship and set its starting position"""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()

        # Lädt das Bilddes Schiffes und ruft dessen umgebendes Rechteck ab
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Platziert jedes neue Schiff mittig am unteren Bildschirmrand
        self.rect.midbottom = self.screen_rect.midbottom

        # Bewegungsflags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)