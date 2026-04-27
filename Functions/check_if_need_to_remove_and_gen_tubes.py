import random as rd


def check_if_need_to_remove_and_gen_tubes_func(tube_pos_list, tube_width, HEIGHT, minimum_tube_height, ground_height,
                                               nb_of_tubes, distance_between_tubes, tube_opening_size,
                                               has_scored_on_current_tube):
    
    
    if tube_pos_list[0][0] <= -tube_width:
        
        old_first_tube_x_pos = tube_pos_list[0][0]
        del tube_pos_list[0]
        
        new_tube_x_coord = tube_pos_list[len(tube_pos_list)-1][0]+distance_between_tubes
        #new_tube_x_coord = old_first_tube_x_pos+nb_of_tubes*(distance_between_tubes+tube_width)-2*tube_width
        maximum_height = HEIGHT - minimum_tube_height - ground_height - tube_opening_size
        new_tube_top_tube_height = rd.randint(minimum_tube_height, maximum_height)
        
        moving_dir = rd.randint(0,1)
        if moving_dir == 0:
            moving_dir = -1
        tube_pos_list.append([new_tube_x_coord, new_tube_top_tube_height, moving_dir])
        
        has_scored_on_current_tube = False
    return tube_pos_list, has_scored_on_current_tube