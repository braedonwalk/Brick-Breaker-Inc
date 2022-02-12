import pygame

class Brick:
    ############
    # class vars w/ constant start values
    ###########
    width = 100
    height = 50
    # brickSurface = pygame.Surface(50,100)
    isDead = False

    # blueBrick = pygame.image.load('Assets/01-Breakout-Tiles.png')
    # brickSurface = pygame.image.load(blueBrick)
    # print(blueBrick)

    #constructor function
    def __init__(self, _x, _y, _health):
        self.x = _x
        self.y = _y
        self.health = _health

        self.brickRect = pygame.Rect(_x, _y, self.width, self.height)

        # brickSurface = pygame.surface(self.width, self.height)

    #render function
    def render(self, _window):
        _x = self.x
        _y = self.y

        self.brickRect = pygame.Rect(_x, _y, self.width, self.height)
        
        #drawing a rectangle
        pygame.draw.rect(_window, (255,0,0), pygame.Rect(self.brickRect))
        # self.brickRect.blit(blueBrick)
        
        if self.health < 0:
            self.isDead = True