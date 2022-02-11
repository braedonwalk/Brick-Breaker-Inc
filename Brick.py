import pygame

class Brick:
    ############
    # class vars w/ constant start values
    ###########
    width = 100
    height = 50
    # brickSurface = pygame.Surface(50,100)

    #constructor function
    def __init__(self, _x, _y, _health):
        self.x = _x
        self.y = _y
        self.health = _health

    #render function
    def render(self, _window):
        _x = self.x - self.width/2
        _y = self.y - self.height/2

        #drawing a rectangle
        pygame.draw.rect(_window, (255,0,0), pygame.Rect(_x, _y, self.width, self.height))