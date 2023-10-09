import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.rect=pygame.Rect(0,0,ai_game.settings.bullet_width,ai_game.settings.bullet_width)
        self.rect.midtop=ai_game.ship.rect.midtop
    def update(self):
        self.rect.y-=self.settings.bullet_speed
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.settings.bullet_color,self.rect)