#!/usr/bin/env python3

#~ import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions
            

def run_game():
    # Initialize the game and create a game object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    bg_color = ai_settings.bg_color
     
    # build a ship
    ship = Ship(ai_settings, screen)
        
    # Begin the main loop
    while True:
        game_functions.check_events(ship)
        ship.update()
        game_functions.updata_screen(ai_settings, screen, ship)

run_game()
