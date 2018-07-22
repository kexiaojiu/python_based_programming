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
        
    
    def blitme(self):
        """map the alien at the specified loaction"""
        self.screen.blit(self.image, self.rect)
