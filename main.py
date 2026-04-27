import pygame

from Functions.generate_tubes import *
from Functions.check_if_need_to_remove_and_gen_tubes import *
from Functions.check_for_gained_score import *
from Functions.start_screen import *
from Functions.death_screen import *
from Functions.draw_functions import *
from Functions.update_functions import *
from Functions.collision_functions import *
from Functions.initialize_variables import *
from Functions.game_loop import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

pygame.display.set_caption("Flabby Bird")

if __name__ == '__main__':

    
    while game_state != False:
        clock.tick(FPS)


        if game_state == 'start':
                            
            game_state, background_image, current_background_index, menu_selection, bird_image, bird_image_dead, current_sprite_index, current_difficulty, scroll_speed, nb_of_tubes, distance_between_tubes, tube_opening_size, tube_pos_list, moving_tubes, choose_circle_x, shooter_mode = start_screen_func(WIDTH, HEIGHT, screen, background_x, background_image_list, ground_height, ground_image,
                        bird_rect_width, bird_rect_height, bird_x, bird_y, bird_image, 
                        tube_pos_list, tube_width, tube_opening_size, ground_y, tube_height, imageTubeUp, imageTubeDown,
                        flappy_font, ground_x, current_background_index, menu_selection, current_sprite_index,
                        sprite_image_list, bird_image_dead, current_difficulty, minimum_tube_height, no_tube_starting_zone_width, nb_of_tubes,
                        distance_between_tubes, moving_tubes, title_text, start_text, choosing_bird_text, choose_background_text, choose_difficulty_text, choose_moving_tubes_text, choose_circle_x, shooter_mode)

        elif game_state == 'game':
            
            game_state, velocity, rotating, counter, bird_y, angle, tube_pos_list, ground_x, has_scored_on_current_tube, score, collision_state, shooter_y, bullet_list, nb_frames_next_bullet, counterbulletgen = game_loop_func(game_state, counter, velocity, rotating, bird_image, bird_y, angle, tube_pos_list,
                    has_scored_on_current_tube, moving_tubes, current_sprite_index, nb_of_tubes, distance_between_tubes,
                    tube_opening_size, background_image, bird_x, ground_x, score, bird_rect_height, bird_rect_width, shooter_mode, shooter_y, bullet_list, nb_frames_next_bullet, counterbulletgen)
            
        elif game_state == 'death':
            
            bullet_list, nb_frames_next_bullet, counterbulletgen, bird_x, bird_y, tube_pos_list, game_state, best_score, has_scored_on_current_tube, score, menu_selection  = you_died_func(collision_state, WIDTH, HEIGHT, screen, die1_sound, bird_x, bird_y, ground_height, velocity, 
                        background_x, background_image, tube_pos_list, tube_width, tube_opening_size, 
                        tube_height, imageTubeUp, imageTubeDown, ground_image, ground_y, acceleration,
                        max_velocity, clock, FPS, die2_sound, start_bird_x, start_bird_y,
                        minimum_tube_height, nb_of_tubes, distance_between_tubes, no_tube_starting_zone_width, arcade_font,
                        ground_x, bird_image_dead, score, best_score, bird_rect_width, bird_rect_height, has_scored_on_current_tube, title_text,
                        best_score_text, best_score_text_Rect, best_score_congrats_text, best_score_congrats_text_Rect,
                        you_died_text, you_died_text_Rect, play_again_text, play_again_text_Rect, main_menu_text1, main_menu_text1_Rect, main_menu_text2, main_menu_text2_Rect,
                        Your_final_score, bullet_list, nb_frames_next_bullet, counterbulletgen, shooter_mode, shooter_y, current_sprite_index)
            
            
                
            


        counter += 1
    

    pygame.quit()
