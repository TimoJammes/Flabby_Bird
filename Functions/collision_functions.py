import pygame

from Functions.initialize_variables import bullet_width, bullet_height
def collision_bird_and_ground_func(HEIGHT,bird_y, ground_height, bird_rect_height, tolerance) : # A function that signals true when the bird crashes on the ground
    
    if bird_y + bird_rect_height - tolerance >= HEIGHT - ground_height:              # The condition is when the y coordinate of the bird is bigger than the screen height, the code returns false
        return True
    else :
        return False

def collision_bird_and_tubes_func(tube_pos_list, bird_x, bird_y, bird_rect_width, bird_rect_height, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y): 
    
    bird_x += tolerance_x
    bird_y += tolerance_y
    bird_rect_width -= 2 * tolerance_x
    bird_rect_height -= 2 * tolerance_y
    birdrect = pygame.Rect(bird_x, bird_y, bird_rect_width, bird_rect_height)
    
    if bird_y <= -bird_rect_width:
        for i in range(3):
            bool_to_return = pygame.Rect.colliderect(birdrect, pygame.Rect(tube_pos_list[i][0], bird_y - 20, tube_width, -(bird_y - 20)))
            if bool_to_return:
                return True
        return bool_to_return
    for i in range(3):
        
        tuberect_top = pygame.Rect(tube_pos_list[i][0], tube_pos_list[i][1] - tube_height,
                                tube_width, tube_height)
        tuberect_bottom = pygame.Rect(tube_pos_list[i][0], tube_pos_list[i][1] + tube_opening_size,
                                    tube_width, tube_height)
        
        bool_to_return = pygame.Rect.colliderect(birdrect, tuberect_top) or pygame.Rect.colliderect(birdrect, tuberect_bottom)
        
        if bool_to_return:
            return True
    return bool_to_return

def collision_bird_and_bullets(bullet_list, bird_x, bird_y, bird_rect_width, bird_rect_height):
    
    for bullet in bullet_list:
        
        birdrect = pygame.Rect(bird_x, bird_y, bird_rect_width, bird_rect_height)
        bulletrect = pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)
        
        if pygame.Rect.colliderect(birdrect, bulletrect):
            return True
    return False
        

def check_for_collision_func(HEIGHT, bird_y, ground_height, bird_rect_height, tube_pos_list, bird_x, bird_rect_width, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y, bullet_list):
    
    if collision_bird_and_ground_func(HEIGHT, bird_y, ground_height, bird_rect_height, tolerance_y):
        
        return 'ground'
    
    elif collision_bird_and_tubes_func(tube_pos_list, bird_x, bird_y, bird_rect_width, bird_rect_height, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y):
        
        return 'tube'
    elif collision_bird_and_bullets(bullet_list, bird_x, bird_y, bird_rect_width, bird_rect_height):
        
        return 'bullet'
    
    return None