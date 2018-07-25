#!/usr/bin/env python3

#~ import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group            

def run_game():
    # Initialize the game and create a game object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
     
    # build a ship
    ship = Ship(ai_settings, screen)
    # bulid a group for storing the bullets
    bullets = Group()
    # build a group for storing the aliens
    aliens = Group()
    
    # create aliens 
    game_functions.create_fleet(ai_settings, screen, aliens, ship)
        
    # Begin the main loop
    while True:
        game_functions.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        game_functions.update_bullets(ai_settings, screen, ship, bullets, aliens)
        game_functions.update_aliens(ai_settings, aliens)
        
        game_functions.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()
