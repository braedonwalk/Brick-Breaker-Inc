#IMPORTS
import pygame

#CREATING BRICK CLASS
class Brick:

    #CLASS VARIABLES WITH CONSTANT VALUES
    width = 100
    height = 50
    # brickSurface = pygame.Surface(50,100)
    isDead = False

    # blueBrick = pygame.image.load('Assets/01-Breakout-Tiles.png')
    # brickSurface = pygame.image.load(blueBrick)
    # print(blueBrick)

    #CONSTRUCTOR
    def __init__(self, _x, _y, _health):
        self.x = _x
        self.y = _y
        self.health = _health

        self.brickRect = pygame.Rect(_x, _y, self.width, self.height)

        # brickSurface = pygame.surface(self.width, self.height)

    #RENDER FUNCTION
    def render(self, _window):
        _x = self.x
        _y = self.y

        self.brickRect = pygame.Rect(_x, _y, self.width, self.height)
        
        #drawing a rectangle
        pygame.draw.rect(_window, (255,0,0), pygame.Rect(self.brickRect))
        # self.brickRect.blit(blueBrick)
        
        if self.health <= 0:
            self.isDead = True
            # print("is dead")

        #drawing rectangle
        pygame.draw.rect(_window, (255,0,0), self.brickRect)
    
    #def ballCollision(self, _ball):
        #collide = pygame.Rect.colliderect(self.brickRect, _ball.hitBox)    
        #if collide:
            #print("yee haw")
            #self.speedY *= -1
