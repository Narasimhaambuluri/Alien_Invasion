import pygame
class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()
        self.settings=ai_game.settings
        self.moving_right=False
        self.moving_left=False


        self.rect.midbottom=self.screen_rect.midbottom
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.x+=self.settings.ship_speeed
        if self.moving_left and self.rect.left>0:
            self.rect.x-=self.settings.ship_speeed
    def blitme(self):
        self.screen.blit(self.image,self.rect)
