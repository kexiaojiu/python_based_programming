#!/usr/bin/env python3
import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            # move the ship to the right
            ship.moving_left = True
            
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, screen, ship, bullets)

  
def check_keyup_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
            

def check_events(ai_settings, screen, ship, bullets):
    """Respond to mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_keydown_events(event, ai_settings, screen, ship, bullets)
        check_keyup_events(event, ship)        
            

def update_screen(ai_settings, screen, ship, bullets):
    """update screen  images and go to the new screen"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
            
    # make the recently painted screen visible
    pygame.display.flip()


def fire_bullet(ai_settings, screen, ship, bullets):
    # creat a bullet, and add it to the group of bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
        
def update_bullets(bullets):
    #delete the missing bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # for testing
        #~ print(len(bullets))
