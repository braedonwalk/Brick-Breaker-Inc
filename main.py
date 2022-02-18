#IMPORTS
import pygame
from Player import Player
from Ball import Ball
from Brick import Brick

# Defining global variables and set-up #

#Define the size of the game window
WIDTH = 1200
HEIGHT = 700
#Make the game window object
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
#Name the game window
pygame.display.set_caption("Brick Breaker Inc")
#Frame rate of game
FPS = 60


#PLAYER VARIABLES
playerStartX = WIDTH/2
playerStartY = HEIGHT-10
player = Player(playerStartX, playerStartY)

#BALL VARIABLES
ballStartX = WIDTH/2
ballStartY = playerStartY - 25
ball1 = Ball(ballStartX, ballStartY) #define start position of ball
gameOver = False

#BRICK VARIABLES
brick = Brick(200, 400, 1) #(X, Y, health)

brickList = []
brickX = 0
brickY = 50
brickHealth = 3

#ADD ENOUGH BRICKS TO FILL UP WIDTH
while brickX < WIDTH:
    brickList.append(Brick(brickX, brickY, brickHealth))
    brickX += 100

if brickX > WIDTH-100:
    brickX = 0
    brickY += 75
    brickHealth -= 1

while brickX < WIDTH:
    brickList.append(Brick(brickX, brickY, brickHealth))
    brickX += 100

if brickX > WIDTH-100:
    brickX = 0
    brickY += 75
    brickHealth -= 1

while brickX < WIDTH:
    brickList.append(Brick(brickX, brickY, brickHealth))
    brickX += 100

#SCORE
score = 0
scoreColor = (255,255,255)
pygame.font.init()
scoreFont = pygame.font.SysFont("rage", 40)
scoreObject = scoreFont.render(str(score), True, scoreColor)
scoreString = scoreFont.render("String: ", True, scoreColor)

###################
# OTHER FUNCTIONS #
###################
def gameOver():
    pass

def updateBounds():
    global rightBoundBall
    global leftBoundBall
    global bottomBoundBall
    global topBoundBall

    global rightBoundPlayer
    global leftBoundPlayer
    global bottomBoundPlayer
    global topBoundPlayer

    #ball bounds
    rightBoundBall = ball1.x
    leftBoundBall = ball1.x - 10
    bottomBoundBall = ball1.y
    topBoundBall = ball1.y - 10

    #player bounds
    rightBoundPlayer = player.x + player.width/2
    leftBoundPlayer = player.x - player.width/2
    topBoundPlayer = player.y + player.height/2
    bottomBoundPlayer = player.y - player.height/2

    #IF BALL HITS PLAYER BOUNCE AWAY
    # if bottomBoundBall >= bottomBoundPlayer and rightBoundBall <= rightBoundPlayer and leftBoundBall >= leftBoundPlayer:
    #     ball1.speedY = -ball1.speedY

   

def ballWindowBound():
    #check conditions
    if rightBoundBall >= WIDTH or leftBoundBall <= 0: #if the ball bounces off right or left wall
        #print("yee haw")
        ball1.speedX = -ball1.speedX #flip the direction of the ball

    if topBoundBall <= 0: #if the ball bounces off top wall
        #print("haw yee")
        ball1.speedY = -ball1.speedY #flip the direction of the ball

    if bottomBoundBall > topBoundPlayer:
        # global gameOver
        # print("game over")
        # gameOver = True
        ball1.speedX = 0
        ball1.speedY = 0
        #ball1.y = HEIGHT - ball1.radius
        gameOver
        

def playerWindowBound():
    #check conditions
    if rightBoundPlayer >= WIDTH:
        player.x = WIDTH - player.width/2

    if leftBoundPlayer <= 0:
        player.x = 0 + player.width/2


# MAIN FUNCTION #

def main():
    global brickList
    global score
    global scoreObject

    # this gets a list of booleans showing which keys are currently pressed
    keysPressed = pygame.key.get_pressed()
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

        #display score
        WINDOW.blit(scoreString, (0, HEIGHT-40))
        WINDOW.blit(scoreObject, (110, HEIGHT-40))
        
        #MOVEMENT
        #make player move
        player.move()
        


        #make ball move
        ball1.move()
        ball1.playerCollision(player)

        #NOT WORKING~~~~~~~~~~~~~~~
        # if gameOver:            #IF BALL GOES BELOW SCREEN, RESET BALL AND PLAYER
        #     global ballStartX
        #     global ballStartY
        #     global playerStartX
        #     global ball1
        #     ballStartX = WIDTH/2
        #     ballStartY = playerStartY - 25
        #     playerStartX = WIDTH/2
        #     ball1 = Ball(ballStartX, ballStartY)
        #     gameOver = False

        

        #bricks
        #brick.ballCollision(ball1.hitBox)

       
       #RENDER FUNCTIONS
        player.render(WINDOW)
        ball1.render(WINDOW)
        
        for aBrick in brickList:
            aBrick.render(WINDOW)


        updateBounds() #Update all the bounds for the ball
        ballWindowBound() #Collision with wall detection for the ball
        playerWindowBound() #Collision with wall detection for the player

        #RENDER ALL BRICKS IN BRICKLIST & BREAK BRICKS
        bricksToKeep = []
        for aBrick in brickList:
            aBrick.render(WINDOW)
            ball1.brickCollision(aBrick)
            if(aBrick.isDead == False):
                bricksToKeep.append(aBrick)
            if(aBrick.isDead):              #IF A BRICK BREAKS
                score = score + 100         #INCREASE SCORE
                scoreObject = scoreFont.render(str(score), True, scoreColor)
                print(score)
        
        brickList = bricksToKeep #UPDATE BRICKLIST TO REMOVE DEAD BRICK
        
        #Put code here that should be run every frame in the game             
        pygame.display.update()
        

# THINGS TO RUN #

<<<<<<< Updated upstream
main()
# print(pygame.font.get_fonts())
=======
main()
>>>>>>> Stashed changes
