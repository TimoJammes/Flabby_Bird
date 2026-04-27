import pygame

from Functions.generate_tubes import *
from Functions.draw_functions import *
from Functions.initialize_variables import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

easy_difficulty_image = pygame.transform.scale(pygame.image.load("Images/Easy.png"), (50, 50))
medium_difficulty_image = pygame.transform.scale(pygame.image.load("Images/Medium.png"), (50, 50))
hard_difficulty_image = pygame.transform.scale(pygame.image.load("Images/Hard.png"), (50, 50))

green_check_image = pygame.transform.scale(pygame.image.load("Images/green_check.png"), (50, 50))
red_cross_image = pygame.transform.scale(pygame.image.load("Images/red_cross.png"), (50, 50))

moving_tubes_image = red_cross_image

shooter_mode_image = red_cross_image

def choose_background_func(pressed_key, current_background_index, background_image_list):
    
    if pressed_key == 'right':
        
        if current_background_index < len(background_image_list) - 1:
            
            current_background_index += 1
        else:
            current_background_index = 0
    
    if pressed_key == 'left':
        
        if current_background_index > 0:
            
            current_background_index -= 1
        else:
            current_background_index = len(background_image_list) - 1
    
    return current_background_index

def choose_sprite_func(pressed_key, current_sprite_index, sprite_image_list):
    
    if pressed_key == 'right':
        
        if current_sprite_index < len(sprite_image_list) - 1:
            
            current_sprite_index += 1
        else:
            current_sprite_index = 0
    
    if pressed_key == 'left':
        
        if current_sprite_index > 0:
            
            current_sprite_index -= 1
        else:
            current_sprite_index = len(sprite_image_list) - 1
    
    return current_sprite_index

def start_screen_func(WIDTH, HEIGHT, screen, background_x, background_image_list, ground_height, ground_image,
                      bird_rect_width, bird_rect_height, bird_x, bird_y, bird_image, 
                      tube_pos_list, tube_width, tube_opening_size, ground_y, tube_height, imageTubeUp, imageTubeDown,
                      flappy_font, ground_x, current_background_index, menu_selection, current_sprite_index,
                      sprite_image_list, bird_image_dead, current_difficulty, minimum_tube_height, no_tube_starting_zone_width, nb_of_tubes,
                      distance_between_tubes, moving_tubes, title_text, start_text, choosing_bird_text, choose_background_text,
                      choose_difficulty_text, choose_moving_tubes_text, choose_circle_x, shooter_mode):

    global moving_tubes_image, shooter_mode_image
    
    
    background_image = background_image_list[current_background_index]
    bird_image = sprite_image_list[current_sprite_index][0][0]
    bird_image_dead = sprite_image_list[current_sprite_index][1]
    
    game_state = 'start'
    
    if current_difficulty == 1:
        scroll_speed = 4
        distance_between_tubes = 500
        nb_of_tubes = 3
        tube_opening_size = 200
        difficulty_image = easy_difficulty_image
    
    elif current_difficulty == 2:
        scroll_speed = 4
        distance_between_tubes = 300
        nb_of_tubes = 4
        tube_opening_size = 175
        difficulty_image = medium_difficulty_image
        
    
    elif current_difficulty == 3:
        scroll_speed = 5
        distance_between_tubes = 200
        nb_of_tubes = 6
        tube_opening_size = 150
        difficulty_image = hard_difficulty_image
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tube_pos_list = generate_tubes_func(minimum_tube_height, tube_opening_size, HEIGHT, nb_of_tubes, distance_between_tubes,
                                ground_height, no_tube_starting_zone_width)
                game_state = 'game'
            if event.key == pygame.K_UP:
                    if menu_selection > 1:
                        menu_selection -= 1
                        menu_selection_sound.play()
            elif event.key == pygame.K_DOWN:
                if menu_selection < 5:
                    menu_selection += 1
                    menu_selection_sound.play()
            
            if menu_selection == 1:
                if event.key == pygame.K_LEFT:
                    menu_selection_sound.play()
                    current_background_index = choose_background_func('left', current_background_index, background_image_list)
                elif event.key == pygame.K_RIGHT:
                    menu_selection_sound.play()
                    current_background_index = choose_background_func('right', current_background_index, background_image_list)

                choose_circle_x = WIDTH//2 - choose_background_text.get_width()/2 - 10
            elif menu_selection == 2:
                
                if event.key == pygame.K_LEFT:
                    menu_selection_sound.play()
                    current_sprite_index = choose_sprite_func('left', current_sprite_index, sprite_image_list)
                if event.key == pygame.K_RIGHT:
                    menu_selection_sound.play()
                    current_sprite_index = choose_sprite_func('right', current_sprite_index, sprite_image_list)

                choose_circle_x = WIDTH//2 - choosing_bird_text.get_width()/2 - 10
            elif menu_selection == 3:
                
                if event.key == pygame.K_LEFT:
                    if current_difficulty > 1:
                        current_difficulty -= 1
                        menu_selection_sound.play()
                    
                elif event.key == pygame.K_RIGHT:
                    if current_difficulty < 3:
                        current_difficulty += 1
                        menu_selection_sound.play()
                choose_circle_x = WIDTH//2 - choose_difficulty_text.get_width()/2 - 10

            elif menu_selection == 4:
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    moving_tubes = not moving_tubes
                    menu_selection_sound.play()
                    if moving_tubes == False:
                        moving_tubes_image = red_cross_image
                    if moving_tubes == True:
                        moving_tubes_image = green_check_image
                choose_circle_x = WIDTH//2 - choose_moving_tubes_text.get_width()/2 - 10
                
            elif menu_selection == 5:
                
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    shooter_mode = not shooter_mode
                    menu_selection_sound.play()
                    if shooter_mode == False:
                        shooter_mode_image = red_cross_image
                    if shooter_mode == True:
                        shooter_mode_image = green_check_image
                        
                choose_circle_x = WIDTH//2 - choose_shooter_mode_text.get_width()/2 - 10
        
    
    draw_backround_func(screen, background_x, background_image_list[current_background_index])
    draw_bird_func(screen, bird_x, bird_y, bird_image, current_sprite_index)
    draw_tubes_func(screen, tube_pos_list, tube_opening_size, tube_height, imageTubeUp, imageTubeDown)
    draw_ground_func(WIDTH, screen, ground_image, ground_y, ground_x)
    
    pygame.draw.rect(screen, GREY, pygame.Rect(WIDTH//5, HEIGHT//4-100, 3*WIDTH//5, 2*HEIGHT//3+30), border_radius = 15)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(WIDTH//5+10, HEIGHT//4+10-100, 3*WIDTH//5-20, 2*HEIGHT//3+10))

    start_text_coords = (WIDTH//2 - start_text.get_width()/2, HEIGHT//4+15-100)
    screen.blit(start_text, start_text_coords)
    pygame.draw.rect(screen, RED, pygame.Rect(start_text_coords[0], start_text_coords[1]+start_text.get_height()-10, start_text.get_width(), 5))
    screen.blit(choose_background_text, ((WIDTH//2 - choose_background_text.get_width()/2, start_text_coords[1]+50)))
    screen.blit(choosing_bird_text, (WIDTH//2 - choosing_bird_text.get_width()/2, start_text_coords[1]+125) )
    screen.blit(choose_difficulty_text, (WIDTH // 2 - choose_difficulty_text.get_width()//2, start_text_coords[1]+200))
    screen.blit(choose_moving_tubes_text, (WIDTH // 2 - choose_moving_tubes_text.get_width()//2, start_text_coords[1]+275))
    screen.blit(choose_shooter_mode_text, (WIDTH // 2 - choose_shooter_mode_text.get_width()//2, start_text_coords[1]+350))
    
    #pygame.draw.circle(screen, BLACK, (choose_circle_x, choosing_bird_text.get_height()//2 + menu_selection*75+start_text_coords[1]-30), 5)
    pygame.draw.line(screen, RED, (choose_circle_x-10, choosing_bird_text.get_height()//2 + menu_selection*75+start_text_coords[1]-30-10),
                     (choose_circle_x, choosing_bird_text.get_height()//2 + menu_selection*75+start_text_coords[1]-30),
                     width = 10)
    pygame.draw.line(screen, RED, (choose_circle_x-10, choosing_bird_text.get_height()//2 + menu_selection*75+start_text_coords[1]-30+10),
                     (choose_circle_x, choosing_bird_text.get_height()//2 + menu_selection*75+start_text_coords[1]-30),
                     width = 10)
    screen.blit(bird_image, (WIDTH//2 + choosing_bird_text.get_width()/2+50, start_text_coords[1]+125))
    screen.blit(pygame.transform.scale(background_image, (100, 50)), ((WIDTH//2 + choose_background_text.get_width()/2+50, start_text_coords[1]+50)))
    
    screen.blit(difficulty_image, (WIDTH // 2 + choose_difficulty_text.get_width()//2+50, start_text_coords[1]+200))
    
    screen.blit(moving_tubes_image, (WIDTH // 2 + choose_moving_tubes_text.get_width()//2+50, start_text_coords[1]+275))
    screen.blit(shooter_mode_image, (WIDTH // 2 + choose_shooter_mode_text.get_width()//2+50, start_text_coords[1]+350))
    
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width()//2, HEIGHT - 90))
    
    pygame.display.update()
    
    return game_state, background_image, current_background_index, menu_selection, bird_image, bird_image_dead, current_sprite_index, current_difficulty, scroll_speed, nb_of_tubes, distance_between_tubes, tube_opening_size, tube_pos_list, moving_tubes, choose_circle_x, shooter_mode
