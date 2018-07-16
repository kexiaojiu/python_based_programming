#!/usr/bin/env python3
import sys
import pygame

def check_events():
    """Respond to mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            

def updata_screen(ai_settings, screen, ship):
    """updata screen  images and go to the new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
            
    # Make the recently painted screen visible
    pygame.display.flip()
