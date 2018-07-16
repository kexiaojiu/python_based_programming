#!/usr/bin/env python3

import pygame

class Ship():
    def __init__(self, screen):
        """initialize the ship"""
        self.screen = screen
        
        # load the ship image and get its external rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # put each ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
       
        
    def blitme(self):
        """map the ship at the specified loaction"""
        self.screen.blit(self.image, self.rect)
