import pygame
from Functions.initialize_variables import *
def draw_bullets_func(bullet_list):
    
    try:
        for bullet in bullet_list:
            
            screen.blit(bullet_image, (bullet[0], bullet[1]))
            #pygame.draw.rect(screen, BLACK, pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height))
    except:
        pass
        
        