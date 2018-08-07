#!/usr/bin/env python3

#~ import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from game_stats import GameStats    
from button import Button  
from scoreboard import Scoreboard      

def run_game():
    # Initialize the game and create a game object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # create a class for storing imformation
    stats = GameStats(ai_settings)
    # create a class for scrore
    scores = Scoreboard(ai_settings, screen, stats) 
    # build a ship
    ship = Ship(ai_settings, screen)
    # bulid a group for storing the bullets
    bullets = Group()
    # build a group for storing the aliens
    aliens = Group()
    
    # create aliens 
    game_functions.create_fleet(ai_settings, screen, aliens, ship)
    
    # create a button
    play_button = Button(ai_settings, screen, "Play")
        
    # Begin the main loop
    while True:
        game_functions.check_events(ai_settings, screen, ship, aliens, bullets, play_button, stats)
        if stats.game_active:
            ship.update()
            bullets.update()
            game_functions.update_bullets(ai_settings, screen, ship, bullets, aliens)
            game_functions.update_aliens(ai_settings, screen, ship, aliens, bullets, stats)
        
        game_functions.update_screen(ai_settings, screen, ship, bullets, 
            aliens, play_button, stats, scores)

run_game()
