from Functions.initialize_variables import *

def update_shooter_pos_func(shooter_y):
    
    global shooter_vel
    
    if shooter_vel > 0:
        if not(shooter_y < HEIGHT-shooter_height-ground_height):
            shooter_vel = -shooter_vel
    else:
        if not(shooter_y > 0):
            shooter_vel = -shooter_vel
    
    return shooter_y + shooter_vel
    
    
    #return shooter_y


def update_bird_pos_func(bird_y, velocity):  #Makes the bird move at a certain velocity
    
    return bird_y + velocity


def update_ground_func(scroll_speed, WIDTH, ground_x):
    
    ground_x -= scroll_speed
    if ground_x <= -WIDTH:
        ground_x = 0
    
    return ground_x


from Functions.draw_functions import draw_ground_func

def update_tube_pos_func(tube_pos_list, scroll_speed, moving_tubes,
                         HEIGHT, minimum_tube_height, ground_height, tube_opening_size):
    
    for i in range(len(tube_pos_list)):
        
        tube_pos_list[i][0] -= scroll_speed
        
        if moving_tubes:
            
            if tube_pos_list[i][2] == 1:
                if tube_pos_list[i][1] < HEIGHT - minimum_tube_height - ground_height - tube_opening_size:
                    
                    tube_pos_list[i][1] += 1
                else:
                    tube_pos_list[i][2] = -tube_pos_list[i][2]
            if tube_pos_list[i][2] == -1:
                if tube_pos_list[i][1] > minimum_tube_height:
                    tube_pos_list[i][1] += -1
                else:
                    tube_pos_list[i][2] = -tube_pos_list[i][2]
            
    return tube_pos_list 


def update_velocity_func(velocity, acceleration, max_velocity):  #Allows the bird to fall gradually faster at the beginning
    
    new_velocity = velocity + acceleration
    
    if new_velocity > max_velocity:
        
        return max_velocity
    
    else:
        
        return new_velocity


def DEAD_update_bird_pos_func(collision_state, bird_rect_height, bird_y, HEIGHT, ground_height, velocity, die2_sound):
    
    """
Falling animation of the bird.

This function takes care of the vertical position of the bird during its death seauence, that is when the bird hits a tube or the ground. Thus, it makes flabby fall towards the ground when it htis a tube

The following parameters taken into account are:
 - collision-state: Indicates if the bird hits a tube
 - bird_rect_height: The vertical parameter of the bird's rectangle as the bird is modelised by a rectangle 
 - bird_y: The current vertical position of the bird
 - HEIGHT: The game-window height
 - ground_height: The height of the ground at the bottom of the screen
 - velocity: The velocity of the bird
 - die2_sound: A death sound effect that is played to tell the user that the game is over
 
Returns:
- Updates the vertical position of the bird during the death animation

"""

    if bird_y + bird_rect_height < HEIGHT - ground_height:
        bird_y += velocity
    else:
        bird_y = HEIGHT - ground_height - bird_rect_height
        
        if collision_state == 'tube' or collision_state == 'bullet':
            die2_sound.play()
    return bird_y