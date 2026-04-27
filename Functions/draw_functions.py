import pygame

from Functions.initialize_variables import *


def draw_shooter_func(shooter_y, shooter_image):
    
    screen.blit(shooter_image, (shooter_x, shooter_y))
    
    
def draw_bird_func(screen, bird_x, bird_y, bird_image, current_sprite_index):
    
    """
    Draws the bird image on the screen.

    Parameters:
    - screen: The game screen surface where the bird will be drawn
    - bird_x: The horizontal position (x-coordinate) of the bird
    - bird_image: The image used for the bird which is taken from the Images file

    Returns:
    - The bird image on the screen
    
    The `blit` method is also used to render the image of 'flabby' 
    """
    
    
    
    screen.blit(bird_image, (bird_x, bird_y))


def draw_backround_func(screen, background_x, background_image):

    """
    Draws the background image on the screen.

    Parameters:
    - screen: The game screen surface where the background will be drawn
    - background_x: The horizontal position (x-coordinate) where the background starts< This enables a scrolling effect 
    - background_image: The images used as the backgrounds, taken from the Images file

    Returns:
    - The backround image on the screen
    
    The `blit` method is used to render the background image onto the screen at the specified
      coordinates. 
    """
    
    screen.blit(background_image, (background_x, -10))

    
#from Functions.update_functions import update_ground_func

def draw_ground_func(WIDTH, screen, ground_image, ground_y, ground_x):
    
    """
    Draws the ground image on the screen.

    Parameters:
    - screen: The game screen surface where the ground will be drawn
    - ground_x: The horizontal position (x-coordinate) of the ground
    - ground_y: The vertical position (y-coordinate) of the ground
    - ground_image: The image used for the ground which is taken from the Images file
    - WIDTH: This corresponds to the game-window width

    Returns:
    - The ground image on the screen
    
    The `blit` method is also used to render the image of the ground
    """
    
    screen.blit(ground_image, (ground_x, ground_y))
    screen.blit(ground_image, (ground_x + WIDTH, ground_y))


def draw_tubes_func(screen, tube_pos_list, tube_opening_size, tube_length, imageTubeUp, imageTubeDown): #Downloads the images of upward tubes and downward tubes

    """
    Draws the tube images on the screen.

    Parameters:
    - screen: The game screen surface where the ground will be drawn
    - tube_pos_list: The list of x and y coordinates of each tube that comes across the screen
    - tube_opening_size: Sets the distance between the two tubes at each x_coordinate
    - tube_length: Defines the lenght of each tube
    - imageTubeUp: The image used for the Tube facing upwards, which is taken from the Images file
    - imageTubeDown: The image used for the Tube facing downwards, which is taken from the Images file

    Returns:
    - The tubes images on the screen
    
    """
    
    for coords in tube_pos_list:        #Positions the upwards tubes and downwards tubes along the scrolling background
        screen.blit(imageTubeUp, (coords[0], coords[1]-tube_length))
        screen.blit(imageTubeDown, (coords[0], coords[1]+tube_opening_size))

    

        
pygame.font.init()
font = pygame.font.Font("Fonts/ARCADE.TTF",80)

def score_display_function(screen,score,RED,WIDTH, WHITE, ORANGE):
    
    pygame.draw.rect(screen, GREY, pygame.Rect(WIDTH//2-73, 0, 146, 70),
                     border_bottom_right_radius = 5, border_bottom_left_radius = 5)
    pygame.draw.rect(screen, ORANGE, pygame.Rect(WIDTH//2-63, 0, 126, 60))
    if score >= 10:
         
        Score_text = font.render(str(int(score)), True, RED)
    else:
        Score_text = font.render('0'+str(int(score)), True, RED)
    screen.blit(Score_text,(WIDTH//2-Score_text.get_width()//2+2,0))