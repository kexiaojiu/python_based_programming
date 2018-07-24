#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    def __init__(self, screen):
        """initialize the star"""
        super().__init__()
        self.screen = screen
        
        # load the raindrop image and get its external rectangle
        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()
        
        # put the raindrop at the uper-lift corener of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store raindrop's positions in decimal numbers
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.raindrop_speed_factor = 1
        
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
            
        
    def update(self):
        """move the raindrop down"""
        self.y += self.raindrop_speed_factor
        self.rect.y = self.y
        
        
    def blitme(self):
        """map the raindrop at the specified loaction"""
        self.screen.blit(self.image, self.rect)
