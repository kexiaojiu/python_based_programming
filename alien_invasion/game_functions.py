#!/usr/bin/env python3
import sys
import pygame
from bullet import Bullet
from alien import Alien

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
            
        elif event.key == pygame.K_q:
            sys.exit()

  
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
            

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """update screen  images and go to the new screen"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
            
    # make the recently painted screen visible
    pygame.display.flip()


def fire_bullet(ai_settings, screen, ship, bullets):
    # creat a bullet, and add it to the group of bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
        
def update_bullets(ai_settings, screen, ship, bullets, aliens):
    #delete the missing bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # for testing
        #~ print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)
            
            
def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
    # whether there is a bullet hitting a alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if len(aliens) == 0:
        create_fleet(ai_settings, screen, aliens, ship)


def check_fleet_edges(ai_settings, aliens):
    """There is a alien reaching the edge, thire directions should be changed"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
            
def change_fleet_direction(ai_settings, aliens):
    """change the directions and move aliens down"""
    ai_settings.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed


def update_aliens(ai_settings, aliens):
    """update aliens's locations"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x  = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows  = int(available_space_y / (2 * alien_height))
    return number_rows
    
        
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)  
    
    
def create_fleet(ai_settings, screen, aliens, ship):
    """create a group of aliens"""
    # get number of aliens in a line
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)
    
    # create aliens in the every row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        
