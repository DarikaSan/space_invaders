import pygame


class Ship:
    def __init__(self, si_game):
        """Initialize the ship and set its starting position"""
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.screen_rect = si_game.screen.get_rect()

        # Lädt das Bilddes Schiffes und ruft dessen umgebendes Rechteck ab
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Platziert jedes neue Schiff mittig am unteren Bildschirmrand
        self.rect.midbottom = self.screen_rect.midbottom

        # Speichert einen Fließkommawert für den Schiffsmittelpunkt
        self.x = float(self.rect.x)

        # Bewegungsflags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags"""
        # Aktualisiert den Wert für den Mittelpunkt des Schiffs,
        # nicht des Rechtecks
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Aktualisiert das rect-Objekt auf der Grundlage von self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
