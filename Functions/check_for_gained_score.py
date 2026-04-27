import pygame
pygame.mixer.init()

from Functions.initialize_variables import banger_sound
def check_for_gained_score_func(scored_sound, bird_x, tube_pos_list, scroll_speed, tube_width, score, has_scored_on_current_tube, current_sprite_index):
    
    first_tube_x_pos = tube_pos_list[0][0]
    if has_scored_on_current_tube == False and first_tube_x_pos + tube_width < bird_x:
        if current_sprite_index == 3:
            banger_sound.play()
        else:
            scored_sound.play()
        score += 1
        has_scored_on_current_tube = True
    # if bird_x - scroll_speed <= first_tube_x_pos + tube_width and bird_x + scroll_speed >= first_tube_x_pos + tube_width:
    #     scored_sound.play()
    #     score += .5
    return score, has_scored_on_current_tube