#!/usr/bin/env python3

#~ import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions
            

def run_game():
    # Initialize the game and create a game object
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    bg_color = ai_settings.bg_color
     
    # build a ship
    ship = Ship(screen)
        
    # Begin the main loop
    while True:
        game_functions.check_events()
        game_functions.updata_screen(ai_settings, screen, ship)

run_game()