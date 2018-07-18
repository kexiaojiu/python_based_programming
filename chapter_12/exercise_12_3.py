#!/usr/bin/env python3

import sys
import pygame
from rocket import Rocket

def check_keydown_events(event, rocket):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move the ship to the right
            rocket.moving_left = True
        elif event.key == pygame.K_UP:
            # move the ship to the up
            rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            # move the ship to the down
            rocket.moving_down = True

  
def check_keyup_events(event, rocket):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            rocket.moving_left = False
        elif event.key == pygame.K_UP:
            rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            rocket.moving_down = False
               

def check_events(rocket):
    """Respond to mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_keydown_events(event, rocket)
        check_keyup_events(event, rocket)        
            

def update_screen(screen, rocket):
    """update screen  images and go to the new screen"""
    screen.fill((230,230, 230))
    rocket.blitme()
            
    # Make the recently painted screen visible
    pygame.display.flip()



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Move rocket")
    
    rocket = Rocket(screen)
    
    while True:
        check_events(rocket)
        rocket.update()
        update_screen(screen, rocket)        
        
run_game()
