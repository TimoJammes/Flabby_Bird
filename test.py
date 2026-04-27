import pygame
import random as rd
from Functions.check_for_collision import *
from Functions.check_for_gained_score import *
from Functions.check_if_need_to_add_tubes import *
from Functions.choose_background import *
from Functions.collision_bird_and_ground import *
from Functions.collision_bird_and_tubes import *
from Functions.DEAD_update_bird_pos import *
from Functions.draw_background import *
from Functions.draw_bird import *
from Functions.draw_ground import *
from Functions.draw_tubes import *
from Functions.generate_tubes import *
from Functions.start_screen import *
from Functions.update_bird_pos import *
from Functions.update_ground import *
from Functions.update_tube_pos import *
from Functions.update_velocity import *

def test_check_for_collision_func():
   HEIGHT = 600
   ground_height = 100
   bird_rect_height = 50
   bird_rect_width = 40
   tube_width = 60
   tube_height = 600
   tube_opening_size = 150
   tolerance_x = 5
   tolerance_y = 5

   bird_y = 500
   tube_pos_list = [[300, 200]]  
   bird_x = 100
   assert check_for_collision_func(HEIGHT, bird_y, ground_height, bird_rect_height, tube_pos_list, bird_x, bird_rect_width, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y) == 'ground'

   bird_y = 150  
   tube_pos_list = [[100, 200]]  
   bird_x = 100
   assert check_for_collision_func(HEIGHT, bird_y, ground_height, bird_rect_height, tube_pos_list, bird_x, bird_rect_width, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y) == 'tube'

   bird_x = 100
   bird_y = 150 
   tube_pos_list = [[100, 200]]
   assert check_for_collision_func(HEIGHT, bird_y, ground_height, bird_rect_height, tube_pos_list, bird_x, bird_rect_width, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y) == 'tube'

   bird_y = 100  
   tube_pos_list = [[300, 300]]  
   bird_x = 100
   assert check_for_collision_func(HEIGHT, bird_y, ground_height, bird_rect_height, tube_pos_list, bird_x, bird_rect_width, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y) is None

test_check_for_collision_func()

def test_check_for_gained_score_func():
   pygame.init()
   pygame.mixer.init()

   bird_x = 100
   scroll_speed = 5
   tube_width = 60
   scored_sound_path = "Sounds/scored.mp3"
   tube_pos_list = [[140, 200], [300, 250], [460, 300]]
   score = 0 

   scored_sound = pygame.mixer.Sound(scored_sound_path)

   class SoundWrapper:
      def __init__(self, sound):
         self.sound = sound
         self.play_called = False

      def play(self):
         self.play_called = True
         self.sound.play()

   wrapped_sound = SoundWrapper(scored_sound)

   tube_pos_list[0][0] = bird_x + scroll_speed - tube_width
   wrapped_sound.play_called = False
   score = check_for_gained_score_func(wrapped_sound, bird_x, tube_pos_list, scroll_speed, tube_width, score)
   assert wrapped_sound.play_called
   assert score == 1

   tube_pos_list[0][0] = bird_x + scroll_speed + 10 
   wrapped_sound.play_called = False 
   score = check_for_gained_score_func(wrapped_sound, bird_x, tube_pos_list, scroll_speed, tube_width, score)
   assert not wrapped_sound.play_called
   assert score == 1

   tube_pos_list[0][0] = bird_x + scroll_speed - tube_width 
   wrapped_sound.play_called = False 
   score = check_for_gained_score_func(wrapped_sound, bird_x, tube_pos_list, scroll_speed, tube_width, score)
   assert wrapped_sound.play_called
   assert score == 2
    
test_check_for_gained_score_func()
    
def test_check_if_need_to_remove_and_gen_tubes_func():
   HEIGHT = 600
   ground_height = 100
   tube_width = 50
   minimum_tube_height = 50
   tube_opening_size = 150
   distance_between_tubes = 200
   nb_of_tubes = 5

   tube_pos_list = [[-60, 200], [140, 250], [340, 300], [540, 350], [740, 400]]

   assert len(check_if_need_to_remove_and_gen_tubes_func(tube_pos_list, tube_width, HEIGHT, minimum_tube_height, ground_height, nb_of_tubes, distance_between_tubes, tube_opening_size)) == nb_of_tubes

   expected_new_x = 740 + distance_between_tubes 
   assert check_if_need_to_remove_and_gen_tubes_func(tube_pos_list, tube_width, HEIGHT, minimum_tube_height, ground_height, nb_of_tubes, distance_between_tubes, tube_opening_size)[-1][0] == expected_new_x

   new_tube_height = check_if_need_to_remove_and_gen_tubes_func(tube_pos_list, tube_width, HEIGHT, minimum_tube_height, ground_height, nb_of_tubes, distance_between_tubes, tube_opening_size)[-1][1]
   max_tube_height = HEIGHT - minimum_tube_height - ground_height - tube_opening_size
   assert minimum_tube_height <= new_tube_height <= max_tube_height

   tube_pos_list = [[140, 200], [340, 250], [540, 300], [740, 350], [940, 400]]

   assert len(check_if_need_to_remove_and_gen_tubes_func(tube_pos_list, tube_width, HEIGHT, minimum_tube_height, ground_height, nb_of_tubes, distance_between_tubes, tube_opening_size)) == nb_of_tubes
   assert check_if_need_to_remove_and_gen_tubes_func(tube_pos_list, tube_width, HEIGHT, minimum_tube_height, ground_height, nb_of_tubes, distance_between_tubes, tube_opening_size) == tube_pos_list

test_check_if_need_to_remove_and_gen_tubes_func()

def test_choose_background_func():
   background_image_list = ["background1", "background2", "background3"]
   current_background_index = 0

   new_index = choose_background_func('right', current_background_index, background_image_list)
   assert new_index == 1

   current_background_index = len(background_image_list) - 1 
   new_index = choose_background_func('right', current_background_index, background_image_list)
   assert new_index == 0

   current_background_index = 1 
   new_index = choose_background_func('left', current_background_index, background_image_list)
   assert new_index == 0

   current_background_index = 0 
   new_index = choose_background_func('left', current_background_index, background_image_list)
   assert new_index == len(background_image_list) - 1

test_choose_background_func()

def test_collision_bird_and_ground_func():
   HEIGHT = 600
   ground_height = 110
   bird_rect_height = 40
   tolerance = 5

   assert collision_bird_and_ground_func(HEIGHT, 400, ground_height, bird_rect_height, tolerance) == False

   assert collision_bird_and_ground_func(HEIGHT, 455, ground_height, bird_rect_height, tolerance) == True

   assert collision_bird_and_ground_func(HEIGHT, 465, ground_height, bird_rect_height, tolerance) == True

   assert collision_bird_and_ground_func(HEIGHT, 454, ground_height, bird_rect_height, tolerance) == False

test_collision_bird_and_ground_func()

def test_collision_bird_and_tubes_func():
   pygame.init()

   tube_height = 600
   tube_width = 50
   tube_opening_size = 150
   tolerance_x = 5
   tolerance_y = 5

   tube_pos_list = [[300, 200]] 
   bird_x = 100
   bird_y = 100
   bird_rect_width = 40
   bird_rect_height = 40
   assert collision_bird_and_tubes_func(tube_pos_list, bird_x, bird_y, bird_rect_width, bird_rect_height, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y) == False

   tube_pos_list = [[100, 150]]
   bird_x = 100
   bird_y = 100  
   bird_rect_width = 40
   bird_rect_height = 40
   assert collision_bird_and_tubes_func(tube_pos_list, bird_x, bird_y, bird_rect_width, bird_rect_height, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y) == True

   tube_pos_list = [[100, 150]]  
   bird_x = 100
   bird_y = 300  
   bird_rect_width = 40
   bird_rect_height = 40
   assert collision_bird_and_tubes_func(tube_pos_list, bird_x, bird_y, bird_rect_width, bird_rect_height, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y) == True

   tube_pos_list = [[100, 150]]
   bird_x = 100
   bird_y = 100
   bird_rect_width = 40
   bird_rect_height = 40
   tolerance_x = 20  
   tolerance_y = 20
   assert collision_bird_and_tubes_func(tube_pos_list, bird_x, bird_y, bird_rect_width, bird_rect_height, tube_height, tube_width, tube_opening_size, tolerance_x, tolerance_y) == False

test_collision_bird_and_tubes_func()

def test_DEAD_update_bird_pos_func():
   pygame.init()
   pygame.mixer.init()

   HEIGHT = 600
   ground_height = 100
   bird_rect_height = 50
   velocity = 10
   die2_sound_path = "Sounds/die2.mp3"
   collision_state_tube = 'tube'
   collision_state_none = None

   die2_sound = pygame.mixer.Sound(die2_sound_path)

   class SoundWrapper:
      def __init__(self, sound):
         self.sound = sound
         self.play_called = False

      def play(self):
         self.play_called = True
         self.sound.play()

   wrapped_sound = SoundWrapper(die2_sound)

   bird_y = 300
   result_y = DEAD_update_bird_pos_func(collision_state_none, bird_rect_height, bird_y, HEIGHT, ground_height, velocity, wrapped_sound)
   assert result_y == bird_y + velocity
   assert not wrapped_sound.play_called

   bird_y = HEIGHT - ground_height - bird_rect_height
   result_y = DEAD_update_bird_pos_func(collision_state_none, bird_rect_height, bird_y, HEIGHT, ground_height, velocity, wrapped_sound)
   assert result_y == HEIGHT - ground_height - bird_rect_height
   assert not wrapped_sound.play_called

   bird_y = HEIGHT - ground_height - bird_rect_height
   wrapped_sound.play_called = False
   result_y = DEAD_update_bird_pos_func(collision_state_none, bird_rect_height, bird_y, HEIGHT, ground_height, velocity, wrapped_sound)
   assert result_y == HEIGHT - ground_height - bird_rect_height

test_DEAD_update_bird_pos_func()

def test_draw_backround_func():
   pygame.init()

   WIDTH = 800
   HEIGHT = 600
   background_x = -50
   background_image_path = "Images/background_original.png"

   screen = pygame.display.set_mode((WIDTH, HEIGHT))

   try:
      background_image = pygame.image.load(background_image_path)
      background_image = pygame.transform.scale(background_image, (WIDTH + 20, HEIGHT))

      screen.fill((0, 0, 0))

      draw_backround_func(WIDTH, HEIGHT, screen, background_x, background_image)

      pygame.display.flip()
        
      pygame.time.wait(3000)

   finally:
      pygame.quit()

test_draw_backround_func()

def test_draw_bird_func():
   pygame.init()

   WIDTH = 800
   HEIGHT = 600
   bird_rect_width = 50
   bird_rect_height = 40
   bird_x = 100
   bird_y = 200
   bird_image_path = "Images/Bird.png"

   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   
   try:
      bird_image = pygame.image.load(bird_image_path)
      bird_image = pygame.transform.scale(bird_image, (bird_rect_width, bird_rect_height))

      screen.fill((0, 0, 0))

      draw_bird_func(screen, bird_rect_width, bird_rect_height, bird_x, bird_y, bird_image)

      pygame.display.flip()

      pygame.time.wait(3000)
      
   finally:
      pygame.quit()

test_draw_bird_func()

def test_draw_ground_func():
   pygame.init()
   WIDTH = 800
   HEIGHT = 600
   ground_height = 110
   ground_y = HEIGHT - ground_height
   ground_x = -50

   screen = pygame.Surface((WIDTH, HEIGHT))

   ground_image = pygame.Surface((WIDTH, ground_height))
   ground_image.fill((0, 255, 0))

   draw_ground_func(WIDTH, screen, ground_image, ground_y, ground_x)

   screen_array = pygame.surfarray.array3d(screen)

   ground_pixels = screen_array[:, ground_y:ground_y + ground_height, :]
   assert (ground_pixels[:, :, 1] == 255).all()

test_draw_ground_func()

def test_draw_tubes_func():
   pygame.init()

   WIDTH = 800
   HEIGHT = 600
   GREEN = (0, 255, 0) 
   tube_pos_list = [[200, 300], [400, 250], [600, 350]] 
   tube_width = 60
   tube_opening_size = 150
   tube_length = 600
   imageTubeUp_path = "Images/Tube up.png"
   imageTubeDown_path = "Images/Tube down.png"

   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   
   try:
      imageTubeUp = pygame.image.load(imageTubeUp_path)
      imageTubeDown = pygame.image.load(imageTubeDown_path)

      imageTubeUp = pygame.transform.scale(imageTubeUp, (tube_width, tube_length))
      imageTubeDown = pygame.transform.scale(imageTubeDown, (tube_width, tube_length))

      screen.fill((0, 0, 0))

      draw_tubes_func(screen, GREEN, tube_pos_list, tube_width, tube_opening_size, WIDTH, tube_length, imageTubeUp, imageTubeDown)

      pygame.display.flip()

      for coords in tube_pos_list:
         print(f"Upward tube: ({coords[0]}, {coords[1] - tube_length})")
         print(f"Downward tube: ({coords[0]}, {coords[1] + tube_opening_size})")

      pygame.time.wait(3000)

   finally:
      pygame.quit()

test_draw_tubes_func()

def test_generate_tubes_func():
   minimum_height = 50
   opening_size = 150
   screen_height = 600
   nb_of_coordinates = 1000
   distance_between_tubes = 200
   ground_height = 110
   no_tube_starting_zone_width = 100

   tube_coordinates = generate_tubes_func(minimum_height, opening_size, screen_height, nb_of_coordinates, distance_between_tubes, ground_height, no_tube_starting_zone_width)

   maximum_height = screen_height - minimum_height - ground_height - opening_size

   for i, (x, y) in enumerate(tube_coordinates):
      assert minimum_height <= y <= maximum_height

   assert len(tube_coordinates) == nb_of_coordinates

   for i in range(len(tube_coordinates) - 1):
      assert tube_coordinates[i + 1][0] - tube_coordinates[i][0] == distance_between_tubes

   assert tube_coordinates[0][0] == no_tube_starting_zone_width

   for i, (x, y) in enumerate(tube_coordinates):
      assert isinstance(x, int) and isinstance(y, int)

test_generate_tubes_func()

def test_start_screen_func():
   pygame.init()

   WIDTH, HEIGHT = 800, 600
   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   background_x = 0
   ground_height = 100
   ground_image = pygame.Surface((WIDTH, ground_height))
   ground_image.fill((0, 255, 0))

   bird_rect_width, bird_rect_height = 40, 40
   bird_x, bird_y = 100, 300
   bird_image = pygame.Surface((bird_rect_width, bird_rect_height))
   bird_image.fill((255, 255, 0))

   GREEN = (0, 255, 0)
   RED = (255, 0, 0)
   WHITE = (255, 255, 255)
   tube_pos_list = [[200, 300], [400, 250], [600, 200]]
   tube_width, tube_opening_size, tube_height = 60, 150, 600
   imageTubeUp = pygame.Surface((tube_width, tube_height))
   imageTubeDown = pygame.Surface((tube_width, tube_height))
   imageTubeUp.fill(GREEN)
   imageTubeDown.fill(GREEN)

   ground_y = HEIGHT - ground_height
   ground_x = 0

   background_image_list = [
        pygame.Surface((WIDTH, HEIGHT)),
        pygame.Surface((WIDTH, HEIGHT)),
    ]
   background_image_list[0].fill((0, 0, 255)) 
   background_image_list[1].fill((255, 0, 0))

   flappy_font = pygame.font.Font(None, 36)
   current_background_index = 0

   pygame.event.clear()
   pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RIGHT}))
   pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RETURN}))

   game_state, background_image, updated_index = start_screen_func(WIDTH, HEIGHT, screen, background_x, background_image_list, ground_height, ground_image, bird_rect_width, bird_rect_height, bird_x, bird_y, bird_image, GREEN, tube_pos_list, tube_width, tube_opening_size, ground_y, tube_height, imageTubeUp, imageTubeDown, RED, WHITE, flappy_font, ground_x, current_background_index)
   assert game_state == 'game'
   assert background_image == background_image_list[1]
   assert updated_index == 1
   pygame.quit()
test_start_screen_func()

def test_update_bird_pos_func():
   bird_y = 100
   velocity = 10
   result = update_bird_pos_func(bird_y, velocity)
   assert result == 110

   bird_y = 100
   velocity = -20
   result = update_bird_pos_func(bird_y, velocity)
   assert result == 80

   bird_y = 50
   velocity = 0
   result = update_bird_pos_func(bird_y, velocity)
   assert result == 50

   bird_y = 0
   velocity = 1000
   result = update_bird_pos_func(bird_y, velocity)
   assert result == 1000

   bird_y = 500
   velocity = -1000
   result = update_bird_pos_func(bird_y, velocity)
   assert result == -500

   bird_y = 200.5
   velocity = -50.3
   result = update_bird_pos_func(bird_y, velocity)
   assert isinstance(result, (int, float))

test_update_bird_pos_func()

def test_update_ground_func():
   scroll_speed = 5
   WIDTH = 800

   ground_x = 0
   new_ground_x = update_ground_func(scroll_speed, WIDTH, ground_x)
   assert new_ground_x == ground_x - scroll_speed

   ground_x = -WIDTH
   new_ground_x = update_ground_func(scroll_speed, WIDTH, ground_x)
   assert new_ground_x == 0

   ground_x = -WIDTH + scroll_speed
   new_ground_x = update_ground_func(scroll_speed, WIDTH, ground_x)
   expected_ground_x = 0 if ground_x - scroll_speed <= -WIDTH else ground_x - scroll_speed
   assert new_ground_x == expected_ground_x
    
test_update_ground_func()

def test_update_tube_pos_func():
   tube_width = 50
   scroll_speed = 5

   tube_pos_list = [[100, 200]] 
   updated_tube_pos_list = update_tube_pos_func(tube_pos_list.copy(), tube_width, scroll_speed)
   assert updated_tube_pos_list == [[95, 200]]
    
   tube_pos_list = [[100, 200], [200, 300], [300, 400]] 
   updated_tube_pos_list = update_tube_pos_func(tube_pos_list.copy(), tube_width, scroll_speed)
   assert updated_tube_pos_list == [[95, 200], [195, 300], [295, 400]]

   tube_pos_list = [[5, 200], [10, 300]]
   updated_tube_pos_list = update_tube_pos_func(tube_pos_list.copy(), tube_width, scroll_speed)
   assert updated_tube_pos_list == [[0, 200], [5, 300]]

   tube_pos_list = []
   updated_tube_pos_list = update_tube_pos_func(tube_pos_list.copy(), tube_width, scroll_speed)
   assert updated_tube_pos_list == []

test_update_tube_pos_func()

def test_update_velocity_func():
   velocity = 5
   acceleration = 2
   max_velocity = 10
   assert update_velocity_func(velocity, acceleration, max_velocity) == 7

   velocity = 9
   acceleration = 3
   max_velocity = 10
   assert update_velocity_func(velocity, acceleration, max_velocity) == 10

   velocity = 8
   acceleration = 5
   max_velocity = 10
   assert update_velocity_func(velocity, acceleration, max_velocity) == 10

   velocity = -5
   acceleration = 3
   max_velocity = 10
   assert update_velocity_func(velocity, acceleration, max_velocity) == -2

   velocity = -5
   acceleration = 20
   max_velocity = 10
   assert update_velocity_func(velocity, acceleration, max_velocity) == 10

   velocity = 5
   acceleration = 0
   max_velocity = 10
   assert update_velocity_func(velocity, acceleration, max_velocity) == 5

   velocity = 5
   acceleration = -2
   max_velocity = 10
   assert update_velocity_func(velocity, acceleration, max_velocity) == 3

   velocity = 3
   acceleration = -5
   max_velocity = 10
   assert update_velocity_func(velocity, acceleration, max_velocity) == -2
   
test_update_velocity_func()
