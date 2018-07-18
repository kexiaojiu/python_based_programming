#!/usr/bin/env python3

import pygame

class Rocket():
    def __init__(self, screen):
        """initialize the rocket"""
        self.screen = screen
        
        # load the ship image and get its external rectangle
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
       
        # flag for moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
       
    
    def update(self):
        if self.moving_right and self.rect.centerx + self.rect.width/2 < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.centerx - self.rect.width/2 > 0: 
            self.rect.centerx -= 1
        if self.moving_up and self.rect.centery - self.rect.height/2 > 0:
            self.rect.centery -= 1
        if self.moving_left and self.rect.centery + self.rect.height/2 < self.screen_rect.bottom:
            self.rect.centery += 1

        
        
    def blitme(self):
        """map the ship at the specified loaction"""
        self.screen.blit(self.image, self.rect)
