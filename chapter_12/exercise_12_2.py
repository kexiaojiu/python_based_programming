#!/usr/bin/env python3

import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Test")
    
    image = pygame.image.load('ship.bmp')
    rect = image.get_rect()
    screen_rect = screen.get_rect()
    
    rect.centerx = screen_rect.centerx
    rect.bottom = screen_rect.bottom
    
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
                
        screen.fill((0, 255, 255))

        screen.blit(image, rect)
        
        pygame.display.flip()
    
    
run_game()
