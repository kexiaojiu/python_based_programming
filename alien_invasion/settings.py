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
        self.ship_speed_factor = 1.5
        
        # settings for bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        #~ self.bullet_color = 60, 60 ,60
        self.bullets_allowed = 5
