###########
# Imports #
###########
import pygame
#from Player import Player
#from Brick import Brick
from Ball import Ball

from Player import Player

########################################
# Defining global variables and set-up #
########################################
# Define the size of the game window
WIDTH = 1200
HEIGHT = 800
# make the game window object
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# name the game window
pygame.display.set_caption("Brick Breaker Inc")
# frame rate of game
FPS = 60

# player vars
player = Player(WIDTH/2, HEIGHT-40)

# Ball vars
ball1 = Ball(WIDTH/2,HEIGHT/2)

#################
# MAIN FUNCTION #
#################
# main game function
def main():
    # make a clock object that will be used
    # to make the game run at a consistent framerate
    clock = pygame.time.Clock()
    # make a boolean that represents whether the game should continue to run or not
    running = True
    # while the game is running
    while running:
	   # this makes it so this function can run at most FPS times/sec
        clock.tick(FPS)
 

        # for all the game events
        for event in pygame.event.get():
           # if the game is exited out of, then stop running the game
            if event.type == pygame.QUIT:
                running = False

        # This fills the game window to be the given RGB color
        WINDOW.fill((51,51,51))

        #render Player
        player.render(WINDOW)
        ball1.render(WINDOW)

        # put code here that should be run every frame in the game             
        pygame.display.update()





main()