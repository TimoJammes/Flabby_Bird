import pygame

from Functions.generate_tubes import *

pygame.init()
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT = 1000, 600
AREA = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(AREA)
clock = pygame.time.Clock()

FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKIN = (241,194,125)
GREY = (169, 169, 169)
FIRE = (252, 82, 0)
BROWN = (90, 56, 37)
LIGHT_BLUE = (137, 207, 240)
ORANGE = (255,165,0)

flappy_font = pygame.font.Font("Fonts/FlappyBird.ttf", 48)
flabby_font = pygame.font.Font("Fonts/FlappyBird.ttf", 150)
arcade_font = pygame.font.Font("Fonts/ARCADE.TTF", 48)
bird_image = pygame.image.load("Images/yellowbird-downflap.png")
bird_image_dead = pygame.image.load("Images/yellowbird-downflap-dead.png")
orig_bird_image_width, orig_bird_image_height = bird_image.get_size()
orig_bird_image_dead_width, orig_bird_image_dead_height = bird_image_dead.get_size()
bird_scale_ratio = 7
bird_rect_width, bird_rect_height = orig_bird_image_width // bird_scale_ratio, orig_bird_image_height // bird_scale_ratio
bird_dead_rect_width, bird_dead_rect_height = orig_bird_image_dead_width // bird_scale_ratio, orig_bird_image_dead_height // bird_scale_ratio


start_bird_x = 250
start_bird_y = 150

bird_x = start_bird_x
bird_y = start_bird_y

velocity = 0
max_velocity = 8
acceleration = .5
jumpvelocity = -10
    
tube_opening_size = 200
minimum_tube_height = 75

tube_width = 80
tube_height = 600
nb_of_tubes = 3
distance_between_tubes = 500
no_tube_starting_zone_width = WIDTH

imageTubeUp = pygame.image.load("Images/Tube down.png") 
imageTubeDown = pygame.image.load("Images/Tube up.png")
imageTubeUp = pygame.transform.scale(imageTubeUp, (tube_width, tube_height))
imageTubeDown = pygame.transform.scale(imageTubeDown, (tube_width, tube_height))

background_x = -10
scroll_speed = 4
ground_x = 0
ground_height = 110
ground_y = HEIGHT - ground_height
ground_image = pygame.image.load("Images/ground.png")
ground_image = pygame.transform.scale(ground_image, (WIDTH + 100, ground_height))  # Resize the ground image

background_image_original = pygame.image.load("Images/background_original.png")
background_image_night = pygame.image.load("Images/background_night.png")
background_image_sea = pygame.image.load("Images/Sea.jpg")
background_image_beach = pygame.image.load("Images/beach.jpg")
background_image_cafe = pygame.image.load("Images/cafe_du_commerce.png")
background_image_nantes = pygame.image.load("Images/background_nantes.jpg")
background_image_onepoint = pygame.image.load("images/onepoint.jpeg")
background_image_list = [background_image_original, background_image_night,
                         background_image_sea, background_image_beach, background_image_cafe,
                         background_image_nantes, background_image_onepoint]

for i in range(len(background_image_list)):
    
    background_image_list[i] = pygame.transform.scale(background_image_list[i], (WIDTH + 20, HEIGHT))


current_background_index = 0

sprite_image_original_downflap = pygame.image.load("Images/yellowbird-downflap.png")
sprite_image_original_midflap = pygame.image.load("Images/yellowbird-midflap.png")
sprite_image_original_upflap = pygame.image.load("Images/yellowbird-upflap.png")
sprite_image_original = [sprite_image_original_downflap, sprite_image_original_midflap, sprite_image_original_upflap]
sprite_image_original_dead = pygame.image.load("Images/yellowbird-downflap-dead.png")

sprite_image_blue_downflap = pygame.image.load("Images/bluebird-downflap.png")
sprite_image_blue_midflap = pygame.image.load("Images/bluebird-midflap.png")
sprite_image_blue_upflap = pygame.image.load("Images/bluebird-upflap.png")
sprite_image_blue = [sprite_image_blue_downflap, sprite_image_blue_midflap, sprite_image_blue_upflap]
sprite_image_blue_dead = pygame.image.load("Images/bluebird-downflap-dead.png")

sprite_image_red_downflap = pygame.image.load("Images/redbird-downflap.png")
sprite_image_red_midflap = pygame.image.load("Images/redbird-midflap.png")
sprite_image_red_upflap = pygame.image.load("Images/redbird-upflap.png")
sprite_image_red = [sprite_image_red_downflap, sprite_image_red_midflap, sprite_image_red_upflap]
sprite_image_red_dead = pygame.image.load("Images/redbird-downflap-dead.png")


sprite_image_ezer = [pygame.image.load("Images/ezer.png"),pygame.image.load("Images/ezer.png"),pygame.image.load("Images/ezer.png")]
sprite_image_ezer_dead = pygame.image.load("Images/ezer-dead.png")


sprite_image_list = [[sprite_image_original, sprite_image_original_dead],
                     [sprite_image_blue, sprite_image_blue_dead],
                     [sprite_image_red, sprite_image_red_dead], [sprite_image_ezer, sprite_image_ezer_dead]]

for i in range(len(sprite_image_list)):
    sprite_image_list[i][0][0] = pygame.transform.scale(sprite_image_list[i][0][0], (bird_rect_width, bird_rect_height))
    sprite_image_list[i][0][1] = pygame.transform.scale(sprite_image_list[i][0][1], (bird_rect_width, bird_rect_height))
    sprite_image_list[i][0][2] = pygame.transform.scale(sprite_image_list[i][0][2], (bird_rect_width, bird_rect_height))
    sprite_image_list[i][1] = pygame.transform.scale(sprite_image_list[i][1], (bird_rect_height, bird_rect_width))

tube_pos_list = generate_tubes_func(minimum_tube_height, tube_opening_size, HEIGHT, nb_of_tubes, distance_between_tubes,
                                    ground_height, no_tube_starting_zone_width)

current_sprite_index = 0

score = 0
best_score = 0

tolerance_x = bird_rect_width // 10
tolerance_y = bird_rect_height // 10 #number of pixels to remove from all sides of bird when testing collisions to make game slightly easier

flap_sound = pygame.mixer.Sound("Sounds/flap.mp3")
scored_sound = pygame.mixer.Sound("Sounds/scored.mp3")
die1_sound = pygame.mixer.Sound("Sounds/die1.mp3")
die2_sound = pygame.mixer.Sound("Sounds/die2.mp3")
explosion_sound = pygame.mixer.Sound("Sounds/explosion.mp3")
menu_selection_sound = pygame.mixer.Sound("Sounds/menu_selection.mp3")
cannon_sound = pygame.mixer.Sound("Sounds/cannon.mp3")
ohwesh_sound = pygame.mixer.Sound("Sounds/ohwesh.mp3")
banger_sound = pygame.mixer.Sound("Sounds/banger.mp3")

moving_tubes = False

menu_selection = 1

title_text = flabby_font.render("FLABBY BIRD", True, RED)
title_ezer_text = flabby_font.render("FLABBY EZER", True, RED)
start_text = arcade_font.render("Press Space to Play", True, RED)

choosing_bird_text = arcade_font.render("Bird Color:", True, RED)

choose_background_text = arcade_font.render("Theme:", True, RED)
choose_difficulty_text = arcade_font.render("Difficulty:", True, RED)
choose_moving_tubes_text = arcade_font.render("Moving tubes:", True, RED)
choose_shooter_mode_text = arcade_font.render("Shooter mode:", True, RED)

best_score_text = arcade_font.render('Best: ' + str(int(best_score)), True, RED)
best_score_text_Rect = best_score_text.get_rect()
best_score_text_Rect.center = (WIDTH // 2, HEIGHT // 2 - 100)
arcade_font.underline = True
best_score_congrats_text = arcade_font.render('NEW BEST SCORE', True, RED)
arcade_font.underline = False
best_score_congrats_text_Rect = best_score_congrats_text.get_rect()
best_score_congrats_text_Rect.center = (WIDTH // 2, HEIGHT //2 + 50-100)

arcade_font.underline = True
you_died_text = arcade_font.render('YOU DIED', True, RED)
arcade_font.underline = False
you_died_text_Rect = you_died_text.get_rect()
you_died_text_Rect.center = (WIDTH // 2, HEIGHT // 2 - 100-100)

play_again_text = arcade_font.render('Press Space to Play Again', True, RED)
play_again_text_Rect = play_again_text.get_rect()
play_again_text_Rect.center = (WIDTH // 2+1, HEIGHT // 2 + 100-100)

main_menu_text1 = arcade_font.render('Press Backspace', True, RED)
main_menu_text1_Rect = main_menu_text1.get_rect()
main_menu_text1_Rect.center = (WIDTH // 2, HEIGHT // 2 + 160-100)

main_menu_text2 = arcade_font.render('to go back to main menu', True, RED)
main_menu_text2_Rect = main_menu_text2.get_rect()
main_menu_text2_Rect.center = (WIDTH // 2, HEIGHT // 2 + 195-100)

Your_final_score = arcade_font.render('Score: '+str(int(score)), True, RED)

choose_circle_x = WIDTH//2 - choose_background_text.get_width()/2 - 10

current_difficulty = 1

counter = 1

has_scored_on_current_tube = False

# Define rotation parameters
angle = 0  # Initial rotation angle
rotation_speed = 10  # Degrees per frame
fall_speed = 5
rotating = False  # Rotation flag

init_shooter_y = 50
shooter_x = 0
shooter_y = init_shooter_y
shooter_width, shooter_height = 100, 100
shooter_image = pygame.transform.scale(pygame.image.load("Images/shooter.png"), (shooter_width, shooter_height))
shooter_vel = 3

shooter_mode = False
game_state = 'start'

bullet_list = []
nb_frames_next_bullet = rd.randint(2*30, 3*30)
counterbulletgen = 0
bullet_speed = 5
bullet_width, bullet_height = 50, 20
bullet_image = pygame.transform.scale(pygame.image.load("Images/bullet.png"), (bullet_width, bullet_height))
