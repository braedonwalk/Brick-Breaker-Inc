import pygame

from Brick import Brick
from Player import Player


class Ball:
    ############
    # class vars w/ constant start values
    ###########
    radius = 7
    speedX = 3
    speedY = 3

    moveButtonPressed = False

    #constructor function
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.hitBox = pygame.rect.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius *2)    

    #render function
    def render(self, _window):
        _x = self.x - self.radius/2
        _y = self.y - self.radius/2

        #drawing a cirlce
        pygame.draw.circle(_window, (255,255,255), (_x, _y), self.radius)


    #make ball move
    def move(self):
        keysPressed = pygame.key.get_pressed()
        
        if keysPressed[pygame.K_SPACE] == True:
            self.moveButtonPressed = True

        if(self.moveButtonPressed == True):
                self.x += self.speedX
                self.y -= self.speedY
                self.hitBox = pygame.rect.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius *2)

    def playerCollision(self, aPlayer):
        collide = pygame.Rect.colliderect(self.hitBox, aPlayer.playerRect)    
        if collide:
            # if self.x >= aPlayer.x - aPlayer.width/2 and self.x <= aPlayer.x + aPlayer.width + aPlayer.width/2: #if the ball is between the player bounds, bounce up
            #     print("hit player")
            #     self.speedY *= -1
            # if (self.x < aPlayer.x - aPlayer.width/2 or self.x < aPlayer.x + aPlayer.width/2):  #if the ball is outside player bounds, bounce sideways
            #     print("hit player side")
            #     self.speedX *= -1
            print("hit player")
            self.speedY *= -1

    def wallCollision(self, _window):
        collide = pygame.Rect.colliderect(self.hitBox, _window)    
        if collide:
            print("haw haw")
            self.speedY *= -1

    def brickCollision(self, aBrick):
        collide = pygame.Rect.colliderect(self.hitBox, aBrick.brickRect)
        if collide:
            if self.x > aBrick.x and self.y > (aBrick.y + aBrick.height):   #BALL HIT BOTTOM OF BRICK
                print("bottom")
                self.speedY *= -1
            elif self.x > aBrick.x and self.y <= aBrick.y:    #BALL HIT TOP OF BRICK
                print("top")
                self.speedY *= -1
            elif self.x > (aBrick.x + aBrick.width) and self.y > aBrick.y:     #BALL HIT RIGHT SIDE OF BRICK
                print("right")
                self.speedX *= -1
            elif self.x < aBrick.x and self.y > aBrick.y:     #BALL HIT LEFT SIDE OF BRICK
                print("left")
                self.speedX *= -1
            # print("breaky break")
            aBrick.health -= 1    
