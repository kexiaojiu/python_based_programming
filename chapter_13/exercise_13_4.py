#!/usr/bin/env python3

import sys
import pygame
from raindrop import Raindrop
from pygame.sprite import Group


def create_raindrop_fleet(screen, raindrops):
    raindrop = Raindrop(screen)
    number_raindrops_x = get_number_raindrops_x(screen, raindrop.rect.width)
    number_raindrops_y = get_number_raindrops_y(screen, raindrop.rect.height)
    
    for line_number in range(number_raindrops_y):
        for row_number in range(number_raindrops_x):
            create_raindrop(screen, raindrops, row_number, line_number)


def get_number_raindrops_x(screen, raindrop_width):
    available_x = screen.get_rect().width - 2 * raindrop_width
    number_raindrops_x = int(available_x / (2 * raindrop_width))
    return number_raindrops_x


def get_number_raindrops_y(screen, raindrop_height):
    available_y = screen.get_rect().height - 2 * raindrop_height
    number_raindrops_y = int(available_y / (2 * raindrop_height))
    return number_raindrops_y
    
    
def create_raindrop(screen, raindrops, row_number, line_number):
    raindrop = Raindrop(screen)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    raindrop.x = raindrop_width + 2 * raindrop_width * row_number
    raindrop.y = raindrop_height + 2 *raindrop_height * line_number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop.y
    raindrops.add(raindrop)


def update_raindrops(screen, raindrops):
    for raindrop in raindrops.copy():
        if raindrop.check_edges():
            #~ print("missing")
            raindrops.remove(raindrop)
            #~ print(len(raindrops))
    if len(raindrops) == 0:
        create_raindrop_fleet(screen, raindrops)
            
            
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("raindrop")
    bg_color = (255, 255, 255)
    
    # build raindrops
    raindrops = Group()
    create_raindrop_fleet(screen, raindrops)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        raindrops.update()
        update_raindrops(screen, raindrops)
        raindrops.draw(screen)
        #~ raindrop.blitme()
                
        pygame.display.flip()
        

run_game()
