#!/usr/bin/env python3

import sys
import pygame

def check_keydown_events(event):
    if event.type == pygame.KEYDOWN:
        print(event.key)

  
def check_keyup_events(event):
    if event.type == pygame.KEYUP:
        print(event.key)
               

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_keydown_events(event)
        check_keyup_events(event)        
            

def update_screen(screen):
    """update screen  images and go to the new screen"""
    screen.fill((230,230, 230))
            
    # Make the recently painted screen visible
    pygame.display.flip()



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Test pres")
    
    
    while True:
        check_events()
        update_screen(screen)        
        
run_game()
