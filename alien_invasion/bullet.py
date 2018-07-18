#!/usr/bin/env python3
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        """create a bullet object in the ship's position"""
        super().__init__()
        self.screen = screen
        # load the bullet image and get its external rectangle
        self.image = pygame.image.load('images/bullet.bmp')
        self.rect = self.image.get_rect()
        #~ # draw a rectangle for a bullet
        #~ self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            #~ ai_settings.bullet_height)
        #~ self.color = ai_settings.bullet_color
        
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # store bullet positions in decimal numbers
        self.y = float(self.rect.y)
        

        self.speed_factor = ai_settings.bullet_speed_factor
       
        
    def update(self):
        """move the bullet up"""
        # update  the decimal value of bullet position
        self.y -= self.speed_factor
        # update the location of the rect of the bullet
        self.rect.y = self.y
        
    
    def draw_bullet(self):
        #~ """draw bullet on the screen"""
        #~ pygame.draw.rect(self.screen,self.color, self.rect)
        
        """map the bullet at the specified loaction"""
        self.screen.blit(self.image, self.rect)
