#!/usr/bin/env python3

class Settings():
    """store all settings"""
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230, 230)
        """blue"""
        #~ self.bg_color = (0, 255, 255)
        
        # speed of a ship
        #~ self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # settings for bullets
        #~ self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        #~ self.bullet_color = 60, 60 ,60
        self.bullets_allowed = 5
        
        # settings for alien
        #~ self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #~ #1 respects right, -1 respects left
        #~ self.fleet_direction = 1
        
        # speed up the game
        self.speedup_scale = 1.2
        self.initialize_dynamial_settings()
        
        
    def initialize_dynamial_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #1 respects right, -1 respects left
        self.fleet_direction = 1
        
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale


