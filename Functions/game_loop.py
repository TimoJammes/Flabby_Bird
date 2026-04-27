import pygame

from Functions.initialize_variables import *

from Functions.check_for_gained_score import *
from Functions.check_if_need_to_remove_and_gen_tubes import *

from Functions.update_functions import *
from Functions.draw_functions import *
from Functions.collision_functions import *

from Functions.draw_bullets import *
from Functions.update_bullets_pos import *
from Functions.generate_bullet import *
from Functions.update_bullet_list import *

def game_loop_func(game_state, counter, velocity, rotating, bird_image, bird_y, angle, tube_pos_list,
                   has_scored_on_current_tube, moving_tubes, current_sprite_index, nb_of_tubes, distance_between_tubes,
                   tube_opening_size, background_image, bird_x, ground_x, score, bird_rect_height, bird_rect_width,
                   shooter_mode, shooter_y, bullet_list, nb_frames_next_bullet, counterbulletgen):
    
    #print(bird_image)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    velocity = jumpvelocity
                    rotating = True
                    flap_sound.play()

    if counter % 3 == 0:
        bird_image = sprite_image_list[current_sprite_index][0][2]
    elif counter % 2 == 0:
        bird_image = sprite_image_list[current_sprite_index][0][1]
    elif counter % 1 == 0:
        bird_image = sprite_image_list[current_sprite_index][0][0]


    velocity = update_velocity_func(velocity, acceleration, max_velocity)
    bird_y = update_bird_pos_func(bird_y, velocity)

    if rotating and angle < 30:
        angle += rotation_speed
    elif not rotating and angle >-90:
        angle -= fall_speed

    if velocity == 8:
        rotating = False
        

    bird_image = pygame.transform.rotate(bird_image, angle)
    
    tube_pos_list = update_tube_pos_func(tube_pos_list, scroll_speed, moving_tubes,
                                            HEIGHT, minimum_tube_height, ground_height, tube_opening_size)
    
    ground_x = update_ground_func(scroll_speed, WIDTH, ground_x)
    tube_pos_list, has_scored_on_current_tube = check_if_need_to_remove_and_gen_tubes_func(tube_pos_list, tube_width, HEIGHT, minimum_tube_height, ground_height,
                                                            nb_of_tubes, distance_between_tubes, tube_opening_size, has_scored_on_current_tube)
    
    
    
    draw_backround_func(screen, background_x, background_image)
    draw_bird_func(screen, bird_x, bird_y, bird_image, current_sprite_index)
    draw_tubes_func(screen, tube_pos_list, tube_opening_size, tube_height, imageTubeUp, imageTubeDown)
    draw_ground_func(WIDTH, screen, ground_image, ground_y, ground_x)
    score_display_function(screen,score,RED, WIDTH, WHITE, ORANGE)
    
    if shooter_mode:
        shooter_y = update_shooter_pos_func(shooter_y)
        bullet_list = update_bullets_pos_func(bullet_list)
        draw_shooter_func(shooter_y, shooter_image)
        
        if counterbulletgen == nb_frames_next_bullet:
            cannon_sound.play()
            bullet_list = generate_bullet_func(bullet_list, shooter_y, shooter_width)
            nb_frames_next_bullet = rd.randint(30*3, 30*6)
            counterbulletgen = 0
        draw_bullets_func(bullet_list)
        
        bullet_list = update_bullet_list_func(bullet_list)
        counterbulletgen += 1

            
    if current_sprite_index == 3:
        screen.blit(title_ezer_text, (WIDTH // 2 - title_ezer_text.get_width()//2, HEIGHT - 90))
    else:
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width()//2, HEIGHT - 90))
    pygame.display.update()
    
    collision_state = check_for_collision_func(HEIGHT, bird_y, ground_height, bird_rect_height, tube_pos_list, bird_x, bird_rect_width, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y, bullet_list)
        
    if collision_state != None:
        game_state = 'death'
    
    score, has_scored_on_current_tube = check_for_gained_score_func(scored_sound, bird_x, tube_pos_list, scroll_speed, tube_width, score, has_scored_on_current_tube, current_sprite_index)

    return game_state, velocity, rotating, counter, bird_y, angle, tube_pos_list, ground_x, has_scored_on_current_tube, score, collision_state, shooter_y, bullet_list, nb_frames_next_bullet, counterbulletgen