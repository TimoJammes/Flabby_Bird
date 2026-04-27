"""
    Generates a list of coordinates for the game's tubes (obstacles), including their positions 
    and heights. 
    
    These coordinates are used to display the tubes on the screen

    Parameters:
    - minimum_height: The minimum height of the bottom tube to ensure it is always visible
    - opening_size: The vertical gap size between the top and bottom tubes
    - screen_height: The total height of the game screen, used to calculate valid tube positions
    - nb_of_coordinates: The number of tubes to generate. This controls how many obstacles appear in the game
    - distance_between_tubes: The horizontal distance between each following tube
    - ground_height: The height of the ground area at the bottom of the screen; This ensures the tubes do not overlap
    - no_tube_starting_zone_width: The space from the starting point where no tubes are generated

    Returns:
    
    - tube_coordinates: A list of tube coordinate pairs, where each pair contains:
        - x-coordinate: The horizontal position of the tube
        - y-coordinate: The height of the top tube
        
    """

import pygame
import random as rd

# Generates a list of all the tube's (obstacle) coordinates for the game, to then display them.
def generate_tubes_func(minimum_height, opening_size, screen_height, nb_of_coordinates, distance_between_tubes, ground_height, no_tube_starting_zone_width): 
# The arguments are minimum height of the bottom tube / size of the opening between the top and bottom tubes / total height of the screen / number of tubes to generate during the game (has to be a big number).
    
    tube_coordinates = [] # Initialize the list to store the coordinates of all the tubes
    # Maximum allowable height for the top tube
    maximum_height = screen_height - minimum_height - ground_height - opening_size # Ensures there is enough space for the opening

    # Generate coordinates for each tube
    for i in range(nb_of_coordinates):
        top_tube_height = rd.randint(minimum_height, maximum_height) # Randomly generate the height of the top tube, ensuring it leaves space for the opening
        # Calculate the x-coordinate for this tube based on its index
        # Tubes are spaced 50 pixels apart horizontally
        tube_x_coord = i*distance_between_tubes+no_tube_starting_zone_width
        moving_dir = rd.randint(0,1)
        if moving_dir == 0:
            moving_dir = -1
        # Append the tube's x and top height as a coordinate pair to the list
        tube_coordinates.append([tube_x_coord, top_tube_height, moving_dir])
    # Return the list of generated tube coordinates where x is the horizontal position of the top left tube and y is the height of the top left tube.
    return tube_coordinates 