import pygame


class Button:
    def __init__(self,ai_game,msg):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings
        self.width,self.height=200,50
        self.text_color=(255,255,255)
        self.button_color=(0,135,0)
        self.font=pygame.font.SysFont(None,48)
        self.rect=pygame.Rect(0,0,self.settings.button_width,self.settings.button_height)
        self.rect.center=self.screen_rect.center
        self._prep_msg(msg)
    def _prep_msg(self,msg):
        self.msg_img=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_img_rect=self.msg_img.get_rect()
        self.msg_img_rect.center=self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_img,self.msg_img_rect)
