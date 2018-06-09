#!/usr/bin/env python3

import sys
import pygame

def run_game():
    # Initialize the game and create a game object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # Begin the main loop
    while True:
        
        # Monitoring mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Make the recently painted screen visible
        pygame.display.flip()


run_game()
