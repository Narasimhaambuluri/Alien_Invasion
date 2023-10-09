import pygame
import sys
import settings
import ship
import bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from  button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    '''A class that manages the main game'''
    def __init__(self):
        pygame.init()
        self.settings=settings.Settings()
        self.clock=pygame.time.Clock()
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.height=self.screen.get_rect().height
        self.settings.width=self.screen.get_rect().width
        self.game_active=False
        pygame.display.set_caption("Alien Invasion")
        self.ship = ship.Ship(self)
        self.button=Button(self,"Play")
        self.stats=GameStats(self)
        self.sb=Scoreboard(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.screen.fill(self.settings.background_color)
            self.sb.show_score()
            if not self.game_active:
                self.button.draw_button()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_events()
            self.clock.tick(60)
            pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._keyup_events(event)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                self._play_game()
    def _update_bullets(self):
        self.bullets.update()
        self._delete_bullets()
        self._check_collisions_create_fleet()
        self._alien_ship_collision()
        self._alien_hitting_bottom()

    def _delete_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
    def _check_collisions_create_fleet(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for alien in collisions.values():
                self.stats.score+=self.stats.score_bonus*len(alien)
            if self.stats.score>self.stats.high_score:
                self.stats.high_score=self.stats.score
                self.sb.prep_high_score()
            self.sb.prep_score()
        if not self.aliens:
            self.bullets.empty()
            print("fllet is complete creating another one")
            self.stats.game_level+=1
            self.sb.prep_level()
            self._create_fleet()
            self.settings.increase_level()
            self.ship.rect.midbottom=self.screen.get_rect().midbottom
    def _alien_ship_collision(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            if self.stats.ships>0:
                self.stats.ships -= 1
                self.sb.prep_ships()
                self.aliens.empty()
                self.bullets.empty()
                self._create_fleet()
                self.ship.rect.midbottom = self.screen.get_rect().midbottom
                # print(self.stats.ships)
                # print("alien and ship collided")
                sleep(0.5)
            else:
                self.game_active=False
                pygame.mouse.set_visible(True)
    def _alien_hitting_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=self.screen.get_rect().height:
                if self.stats.ships>0:
                    self.stats.ships -= 1
                    self.sb.prep_ships()
                    self.aliens.empty()
                    self.bullets.empty()
                    self._create_fleet()
                    self.ship.rect.midbottom = self.screen.get_rect().midbottom
                    print("alien hitting bottom")
                    sleep(0.5)
                    break
                else:
                    self.game_active = False
    def _keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key==pygame.K_SPACE:
            new_bullet=bullet.Bullet(self)
            self.bullets.add(new_bullet)
        elif event.key==pygame.K_q:
            sys.exit()
    def _keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_events(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self._move_fleet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
    def _create_fleet(self):
        alien= Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        while current_y<(self.settings.height-7*alien_height):
            while current_x<(self.settings.width-2*alien_width):
                new_alien=Alien(self)
                # new_alien.x=current_x
                new_alien.rect.x=current_x
                new_alien.rect.y=current_y
                self.aliens.add(new_alien)
                current_x+=2*alien_width
            current_x=alien_width
            current_y+=2*alien_height
    def _move_fleet(self):
        self._check_fleet_edges()
        self.aliens.update()
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.alien_down_speed
        self.settings.fleet_direction*=-1
    def _play_game(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button.rect.collidepoint(mouse_pos) and not self.game_active:
            pygame.mouse.set_visible(False)
            self.settings.dynamic_settings()
            sleep(0.5)
            self.game_active = True
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            # print(self.stats.ships)
            # print("hello testing")

if __name__=="__main__":
    ai=AlienInvasion()
    ai.run_game()
