#!/usr/bin/env python3

import sys
import pygame
from star import Star
from pygame.sprite import Group
from random import randint


def create_star_fleet(screen, stars):
    star = Star(screen)
    number_stars_x = get_number_stars_x(screen, star.rect.width)
    number_stars_y = get_number_stars_y(screen, star.rect.height)
    
    for line_number in range(number_stars_y):
        for row_number in range(number_stars_x):
            if row_number == randint(0, number_stars_x) or line_number == randint(0, number_stars_y):
                create_star(screen, stars, row_number, line_number)

def get_number_stars_x(screen, star_width):
    available_x = screen.get_rect().width - 2 * star_width
    number_stars_x = int(available_x / (2 * star_width))
    return number_stars_x

def get_number_stars_y(screen, star_height):
    available_y = screen.get_rect().height - 2 * star_height
    number_stars_y = int(available_y / (2 * star_height))
    return number_stars_y
    
def create_star(screen, stars, row_number, line_number):
    star = Star(screen)
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = star_width + 2 * star_width * row_number
    star.y = star_height + 2 *star_height * line_number
    star.rect.x = star.x
    star.rect.y = star.y
    stars.add(star)



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Star")
    bg_color = (255, 255, 255)
    
    # build stars
    stars = Group()
    create_star_fleet(screen, stars)
    #~ star = Star(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        stars.draw(screen)
        #~ star.blitme()
                
        pygame.display.flip()
        

run_game()
