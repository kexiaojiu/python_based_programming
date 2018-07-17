#!/usr/bin/env python3

import pygame

class Ship():
    def __init__(self, settings, screen):
        """initialize the ship"""
        self.screen = screen
        self.ai_settings = settings
        
        # load the ship image and get its external rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # put each ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # only integer can be stored in centerx
        self.center = float(self.rect.centerx)
       
        # flag for moving
        self.moving_right = False
        self.moving_left = False
       
    
    def update(self):
        if self.moving_right and self.center < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.center > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        
        
    def blitme(self):
        """map the ship at the specified loaction"""
        self.screen.blit(self.image, self.rect)
