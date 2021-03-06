#!/usr/bin/env python3

class GameStats():
    """track game statistics"""
    
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # default value
        self.game_active = False
        
    
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
