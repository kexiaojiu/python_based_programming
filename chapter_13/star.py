#!/usr/bin/env python3

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, screen):
        """initialize the star"""
        super().__init__()
        self.screen = screen
        
        # load the star image and get its external rectangle
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()
        
        # put the star at the uper-lift corener of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store star positions in decimal numbers
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    
    def blitme(self):
        """map the alien at the specified loaction"""
        self.screen.blit(self.image, self.rect)
