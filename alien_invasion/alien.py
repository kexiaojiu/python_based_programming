#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen):
        """initialize the alien"""
        super().__init__()
        self.screen = screen
        self.ai_settings = settings
        
        # load the alien image and get its external rectangle
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # put the alien at the uper-lift corener of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store alien positions in decimal numbers
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
            
        
    def update(self):
        """move the aliens to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor * 
            self.ai_settings.fleet_direction)
        self.rect.x = self.x
 
        
    def blitme(self):
        """map the alien at the specified loaction"""
        self.screen.blit(self.image, self.rect)
