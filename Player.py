#IMPORTS
import pygame

#CREATING PLAYER CLASS
class Player:

    #CLASS VARIABLES WITH CONSTANT VALUES
    width = 100
    height = 20
    speed = 5
    isDead = False

    #CONSTRUCTOR
    def __init__(self, _x, _y) -> None:
        self.x = _x
        self.y = _y
        self.playerRect = pygame.Rect(_x, _y, self.width, self.height)

    #RENDER FUNCTION
    def render(self, _window):
        _x = self.x - self.width/2
        _y = self.y - self.height/2

        self.playerRect = pygame.Rect(_x, _y, self.width, self.height)

        #drawing rectangle
        # self.playerRect.blit(playerBumper, self.x, self.y)    #attempt at drawing asset at player location
        pygame.draw.rect(_window, (255,0,255), self.playerRect)

    #MOVE FUNCTION
    def move(self):
        #handle player movement from key presses
        keysPressed = pygame.key.get_pressed()
        
        if keysPressed[pygame.K_a] == True: #if the 'a' key is pressed
            self.x -= self.speed
        elif keysPressed[pygame.K_d] == True: #if the 'd' key is pressed
            self.x += self.speed