import pygame.font
from ship import Ship
from pygame.sprite import Group


class Scoreboard:
    def __init__(self,ai_game):
        self.ai_game=ai_game
        self.screen=ai_game.screen
        self.stats=ai_game.stats
        self.screen_rect=self.screen.get_rect()
        self.font=pygame.font.SysFont(None,25)
        self.text_color=(0,0,0)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    def prep_score(self):
        score=str(self.stats.score)
        self.score_img=self.font.render(f"SCORE:{score}",True,self.text_color)
        self.score_img_rect=self.score_img.get_rect()
        self.score_img_rect.right=self.screen_rect.right-20
        self.score_img_rect.top=20
    def prep_high_score(self):
        high_score=str(self.stats.high_score)
        self.high_score_img=self.font.render(f"High Score:{high_score}",True,self.text_color)
        self.high_score_rect=self.high_score_img.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=20
    def prep_level(self):
        level=str(self.stats.game_level)
        self.level_img=self.font.render(f"Level:{level}",True,self.text_color)
        self.level_img_rect=self.level_img.get_rect()
        self.level_img_rect.right=self.screen_rect.right-20
        self.level_img_rect.top=40
    def prep_ships(self):
        ship=str(self.stats.ships)
        self.ship_img=self.font.render(f"Ships:{ship}",True,self.text_color)
        self.ship_img_rect=self.ship_img.get_rect()
        self.ship_img_rect.left=self.screen_rect.left+20
        self.ship_img_rect.top=20



    def show_score(self):
        self.screen.blit(self.score_img,self.score_img_rect)
        self.screen.blit(self.high_score_img,self.high_score_rect)
        self.screen.blit(self.level_img,self.level_img_rect)
        self.screen.blit(self.ship_img,self.ship_img_rect)
