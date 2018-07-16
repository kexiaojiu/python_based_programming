#!/usr/bin/env python3

import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Test")
    
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
                
        screen.fill((0, 255, 255))
        pygame.display.flip()
    
    
run_game()
