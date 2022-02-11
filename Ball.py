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
            print("yee haw")
            self.speedY *= -1

    def wallCollision(self, _window):
        collide = pygame.Rect.colliderect(self.hitBox, _window)    
        if collide:
            print("haw haw")
            self.speedY *= -1