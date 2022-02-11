###########
# Imports #
###########
import pygame
from Player import Player
from Ball import Ball
from Brick import Brick

########################################
# Defining global variables and set-up #
########################################
# Define the size of the game window
WIDTH = 1200
HEIGHT = 700
# make the game window object
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# name the game window
pygame.display.set_caption("Brick Breaker Inc")
# frame rate of game
FPS = 60

# player vars
playerStartX = WIDTH/2
playerStartY = HEIGHT-40
player = Player(playerStartX, playerStartY)

# Ball vars
ballStartX = WIDTH/2
ballStartY = HEIGHT/2
ball1 = Ball(ballStartX, ballStartY)          #define start position of ball

#ball bounds
rightBoundBall = ball1.x + ball1.radius
leftBoundBall = ball1.x - ball1.radius
bottomBoundBall = ball1.y + ball1.radius
topBoundBall = ball1.y - ball1.radius


###################
# OTHER FUNCTIONS #
###################
def updateBounds():
    global rightBoundBall
    global leftBoundBall
    global bottomBoundBall
    global topBoundBall

    #ball bounds
    rightBoundBall = ball1.x + ball1.radius
    leftBoundBall = ball1.x - ball1.radius
    bottomBoundBall = ball1.y + ball1.radius
    topBoundBall = ball1.y - ball1.radius



def crash():
    #check conditions
    if rightBoundBall >= WIDTH or leftBoundBall <= 0:   #if the ball bounces off right or left wall
        print("yee haw")
        ball1.speedX = -ball1.speedX                    #flip the direction of the ball

    if bottomBoundBall >= HEIGHT or topBoundBall <= 0:  #if the ball bounces off top or bottom wall
        print("haw yee")
        ball1.speedY = -ball1.speedY                    #flip the direction of the ball

#Brick vars
brick = Brick(200, 400, 1)  #(width, height, health)

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
        
        player.move()

        #render Player
        player.render(WINDOW)
        ball1.render(WINDOW)
        brick.render(WINDOW)

        #make ball move
        ball1.x += ball1.speedX
        ball1.y -= ball1.speedY

        updateBounds()      #update all the bounds for the ball
        crash()             #collision detection for the ball


        # put code here that should be run every frame in the game             
        pygame.display.update()


####################
#OTHER FUNCTIONS
####################
def renderBricks():
    
    return


main()
print(player.x)