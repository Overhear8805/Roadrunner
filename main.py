#!/usr/bin/python2
'''
An IT security game in form of a run'n'jump side scroller.

Simon Cedergren Malmqvist
Licensed under GNU GPLv3

Python 2.7
pygame

TODO:
Cut down drastically on the use of global variables. They are left from a time when this wasn't written as object oriented code.

'''
import pygame 
import random
import sys
import inputbox
from pygame.locals import * 
from obsticle_object import *
from car_object import *
from score_counter import *
from question_loader import *
from road_object import *
from question_dialog import *
from life_meter import *
from leaderboard import *
from intro_screen import *

SCORE = 0
SPEED = 0
DRAG = 0.2
TIME_SINCE_LAST_OBSTICLE = 0

pygame.init()

screen = pygame.display.set_mode((640,480))

player_sprite = pygame.image.load('sprites/car.png').convert_alpha()
road_sprite = pygame.image.load('sprites/road.png').convert_alpha()
tree_sprite = pygame.image.load('sprites/tree.png').convert_alpha()
box_sprite = pygame.image.load('sprites/box.png').convert_alpha()
barrel_sprite = pygame.image.load('sprites/barrel.png').convert_alpha()
sign_sprite = pygame.image.load('sprites/sign.png').convert_alpha()
sky_sprite = pygame.image.load('sprites/sky.png').convert_alpha()
into_sprite = pygame.image.load('sprites/intro.png').convert_alpha()
dialog_sprite = pygame.image.load('sprites/dialog.png').convert_alpha()
heart_sprite = pygame.image.load('sprites/heart.png').convert_alpha()
highscore_background = pygame.image.load('sprites/highscore.png').convert_alpha()

screen.blit(sky_sprite, (0, 0))

player_position = 1 
display_dialog = False
has_collided_already = False

obsticle = Obsticle(tree_sprite)
car = CarObject(player_sprite)
score_counter = ScoreCounter()
question_controller = Question_Loader()
left_road_piece = Road_Object(road_sprite, 0)
right_road_piece = Road_Object(road_sprite, 640/2)
question_dialog = Question_Dialog(dialog_sprite)
life_meter = Life_Meter(heart_sprite)
intro_screen = Intro_Screen(into_sprite)

# Move the background to make it look like the car is moving.
def move_forward():
    global SPEED 
    # Call it gears if you'd like!
    if SPEED >= 0 and SPEED < 5:
        SPEED += 5
    elif SPEED >= 5 and SPEED < 10:
        SPEED += 4 
    elif SPEED >= 10 and SPEED < 15:
        SPEED += 2
    else:
        SPEED += 1.5
    
def jump():
    car.jump()

def generate_obsticle():
    global obsticle 
    global has_collided_already 
    global TIME_SINCE_LAST_OBSTICLE 

    if (obsticle.x + 128) <= 0: # Make sure there's no obsticles on the screen.
        sprite_rand = random.randint(0,3) # Pick a random number.
        if sprite_rand == 0: # Each sprite has its own number. If sprite_rand is 0, the tree sprite will show.
            obsticle = Obsticle(tree_sprite)
        elif sprite_rand == 1: # If sprite_rand is 1, the box sprite will show instead, and so on...
            obsticle = Obsticle(box_sprite)
        elif sprite_rand == 2:
            obsticle = Obsticle(sign_sprite)
        elif sprite_rand == 3:
            obsticle = Obsticle(barrel_sprite)

        obsticle.reset() # Moves the obsticle further away (to the right side) on the screen.
        has_collided_already = False # This is to make sure that an obsticle only triggers *one* dialog.
        TIME_SINCE_LAST_OBSTICLE = pygame.time.get_ticks() 


def update_values(delta):
    global display_dialog 
    global is_game_over 

    if not display_dialog or not is_game_over:
        global obsticle 
        global SPEED
        global SCORE
        global DRAG
        global has_collided_already 

        if SPEED > 0 and not car.jumping:
            SPEED -= DRAG
        elif SPEED > 0 and car.jumping:
        #    SPEED -= (DRAG*0.5)
            pass
        else:
            SPEED = 0

        SCORE += SPEED/10

        obsticle.update(SPEED, 0)
        score_counter.update(int(SCORE))
        left_road_piece.update(SPEED)
        right_road_piece.update(SPEED)
        intro_screen.update(SPEED)
        car.update()

        if pygame.sprite.collide_rect(car, obsticle) and not has_collided_already:
            has_collided_already = True
            show_dialog()
           # print(question)
#        print("SPEED = " + str(SPEED))

def show_dialog():
    global display_dialog
    global correct_answer 
    question = question_controller.get_next_question()
    correct_answer = question_dialog.set_question(question)
    display_dialog = True

def update_screen():
    global display_dialog
    global question_dialog 
    global obsticle 
    global sky_sprite 
    global is_game_over 

    if not is_game_over:
        screen.blit(sky_sprite, (0, 0))

        intro_screen.draw(screen)
        score_counter.draw(screen)
        left_road_piece.draw(screen)
        right_road_piece.draw(screen)
        car.draw(screen)
        obsticle.draw(screen)
        life_meter.draw(screen)
 
    if display_dialog and not is_game_over:
        question_dialog.draw(screen)       

    pygame.display.update()

def on_correct_answer():
#    print("Correct answer!")
    pass

def on_incorrect_answer():
    global life_meter 
#    print("Incorrect answer!")
    life_meter.lose_life()
    if life_meter.lifes_left <= 0:
        game_over()

def game_over():
    global is_game_over 
    global name
    global highscore_background
    global leaderboard
    is_game_over = True
    screen.blit(highscore_background, (0,0))
    name = inputbox.ask(screen, "Name")
    leaderboard = Leaderboard(name, SCORE)
    leaderboard.load_previous_scores()
    leaderboard.save_score()

def show_highscore():
    global SCORE
    global screen
    global leaderboard
    screen.blit(highscore_background, (0,0))
    leaderboard.draw(screen)
    pygame.display.update()

def reset():
    global SPEED
    global SCORE
    global display_dialog
    global correct_answer 
    global life_meter 
    global is_game_over 
    global active_game 
    global obsticle 
    global has_collided_already

    SPEED = 0
    SCORE = 0
    display_dialog = False
    correct_answer = False
    is_game_over = False
    active_game = True
    has_collided_already = False
    life_meter.reset()
    obsticle.reset()

def main():
    global SPEED
    global display_dialog
    global correct_answer 
    global life_meter 
    global is_game_over 
 
    clock = pygame.time.Clock()
    active_game = True
    is_game_over = False

    # The game loop!
    while active_game:

        # This is a buffer that reads user input and does a corresponding thing depending on what the user does.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not display_dialog and not is_game_over:
                generate_obsticle()
                if not car.jumping:
                    move_forward()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1 and display_dialog and not is_game_over:
                display_dialog = False
                if correct_answer == 1:
                    on_correct_answer()
                else:
                    on_incorrect_answer()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and display_dialog and not is_game_over:
                display_dialog = False
                if correct_answer == 0:
                    on_correct_answer()
                else:
                    on_incorrect_answer()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not display_dialog and not is_game_over:
                jump()
                
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                active_game = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r and is_game_over:
                reset()
                
        if is_game_over:
            show_highscore()
            display_dialog  = False

        update_values(pygame.time.get_ticks())
        update_screen()

        clock.tick(60)

if __name__=='__main__':
    main()
