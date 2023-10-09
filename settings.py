class Settings:
    def __init__(self):
        self.height=1000
        self.width=600
        self.background_color=(230,230,230)
        self.bullet_height=25
        self.bullet_width=15
        self.bullet_color=(60,60,60)
        self.fleet_direction=1
        self.ship_limit=3
        self.button_width=200
        self.button_height=50
        self.speedup_scale=2
        self.dynamic_settings()
    def dynamic_settings(self):
        self.ship_speeed=5
        self.alien_down_speed=10
        self.alien_speed=5
        self.bullet_speed=5
    def increase_level(self):
        self.ship_speeed+=self.speedup_scale
        self.alien_speed+=self.speedup_scale
        self.bullet_speed+=self.speedup_scale