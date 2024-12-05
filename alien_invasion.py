import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.bg_image = pygame.image.load('images/tjnw6xv5.png')
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self._update_bullets()
            self.ship.update()
            

        
            print(len(self.bullets))

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)

    def _check_keydown_events(self,event):
                     
                if event.key == pygame. K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                      sys.exit()
                elif event.key == pygame.K_SPACE:
                      self._fire_bullet()

    def _check_keyup_events(self, event):
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                      self.ship.moving_left = False

                      self.ship.rect.x += 1

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
          new_bullet = Bullet(self)
          self.bullets.add(new_bullet)

    def _update_bullets(self):
           self.bullets.update()

    def _update_screen(self):
            self.screen.blit(self.bg_image, (0,0))
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)




if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


