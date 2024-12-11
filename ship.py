import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/sonic.png')
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.image.set_colorkey((235, 235, 235))
        


        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.x = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False


    def center_ship(self):
        self.center = self.screen_rect.centerx


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor


        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)