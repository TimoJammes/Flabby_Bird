
import pygame

from Functions.generate_tubes import *
from Functions.draw_functions import *
from Functions.update_functions import update_velocity_func
from Functions.update_functions import DEAD_update_bird_pos_func
from Functions.initialize_variables import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

def you_died_func(collision_state, WIDTH, HEIGHT, screen, die1_sound, bird_x, bird_y, ground_height,
                  velocity, background_x, background_image, tube_pos_list, tube_width,
                  tube_opening_size, tube_height, imageTubeUp, imageTubeDown, ground_image,
                  ground_y, acceleration, max_velocity, clock, FPS, die2_sound, start_bird_x,
                  start_bird_y, minimum_tube_height, nb_of_tubes, distance_between_tubes, no_tube_starting_zone_width, arcade_font,
                  ground_x, bird_image_dead, score, best_score, bird_rect_height, bird_rect_width, has_scored_on_current_tube,
                  title_text, best_score_text, best_score_text_Rect, best_score_congrats_text, best_score_congrats_text_Rect,
                  you_died_text, you_died_text_Rect, play_again_text, play_again_text_Rect, main_menu_text1, main_menu_text1_Rect, main_menu_text2, main_menu_text2_Rect,
                  Your_final_score, bullet_list, nb_frames_next_bullet, counterbulletgen, shooter_mode, shooter_y, current_sprite_index):
    

    if score >= best_score:
        
        best_score = score
    
    best_score_text = arcade_font.render('Best: ' + str(int(best_score)), True, RED)
    best_score_text_Rect = best_score_text.get_rect()
    best_score_text_Rect.center = (WIDTH // 2, HEIGHT // 2 - 100)
    
    arcade_font.underline = True
    best_score_congrats_text = arcade_font.render('NEW BEST SCORE', True, RED)
    arcade_font.underline = False
    best_score_congrats_text_Rect = best_score_congrats_text.get_rect()
    best_score_congrats_text_Rect.center = (WIDTH // 2, HEIGHT //2 + 50-100)
    Your_final_score = arcade_font.render('Score: '+str(int(score)), True, RED)
    
    game_state = 'death'
    
    deathloop = True
    if collision_state != 'bullet':
        
        
        if current_sprite_index == 3:
            ohwesh_sound.play()
        else:
            die1_sound.play()
    else:
        explosion_sound.play()
        if current_sprite_index == 3:
            ohwesh_sound.play()
    while deathloop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = False
                deathloop = False
            elif bird_y == HEIGHT - ground_height - bird_rect_height:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_x = start_bird_x
                        bird_y = start_bird_y
                        tube_pos_list = generate_tubes_func(minimum_tube_height, tube_opening_size, HEIGHT,
                                                            nb_of_tubes, distance_between_tubes, ground_height, no_tube_starting_zone_width)
                        game_state = 'game'
                        has_scored_on_current_tube = False
                        deathloop = False
                        
                
                    elif event.key == pygame.K_BACKSPACE:
                        bird_x = start_bird_x
                        bird_y = start_bird_y
                        tube_pos_list = generate_tubes_func(minimum_tube_height, tube_opening_size, HEIGHT,
                                                            nb_of_tubes, distance_between_tubes, ground_height, no_tube_starting_zone_width)
                        game_state = 'start'
                        has_scored_on_current_tube = False
                        deathloop = False
                        
                        
        if bird_y != HEIGHT - ground_height - bird_rect_height:
            bird_y = DEAD_update_bird_pos_func(collision_state, bird_rect_height, bird_y, HEIGHT, ground_height, velocity, die2_sound)
            velocity = update_velocity_func(velocity, acceleration, max_velocity)
        draw_backround_func(screen, background_x, background_image)
        draw_tubes_func(screen, tube_pos_list, tube_opening_size, tube_height, imageTubeUp, imageTubeDown)
        draw_bird_func(screen, bird_x, bird_y, bird_image_dead, current_sprite_index)
        draw_ground_func(WIDTH, screen, ground_image, ground_y, ground_x)

        if shooter_mode:
            
            draw_shooter_func(shooter_y, shooter_image)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width()//2, HEIGHT - 90))
        if bird_y == HEIGHT - ground_height - bird_rect_height:
            pygame.draw.rect(screen, GREY, pygame.Rect(WIDTH//5, HEIGHT//4-100, 3*WIDTH//5, 2*HEIGHT//3-30), border_radius = 15)
            pygame.draw.rect(screen, ORANGE, pygame.Rect(WIDTH//5+10, HEIGHT//4+10-100, 3*WIDTH//5-20, 2*HEIGHT//3-50))
            
            screen.blit(you_died_text, you_died_text_Rect)
            screen.blit(play_again_text, play_again_text_Rect)
            screen.blit(main_menu_text1, main_menu_text1_Rect)
            screen.blit(main_menu_text2, main_menu_text2_Rect)
            screen.blit(best_score_text, best_score_text_Rect)
            if score >= best_score:
                screen.blit(best_score_congrats_text, best_score_congrats_text_Rect)
                
                

        
            screen.blit(Your_final_score,(WIDTH // 2 - Your_final_score.get_width()//2, HEIGHT // 2 - 75-100))
        
        pygame.display.update()
        
    score = 0
    menu_selection = 1
    
    bullet_list = []
    nb_frames_next_bullet = rd.randint(2*30, 3*30)
    counterbulletgen = 0
    
    
    return bullet_list, nb_frames_next_bullet, counterbulletgen, bird_x, bird_y, tube_pos_list, game_state, best_score, has_scored_on_current_tube, score, menu_selection

            
