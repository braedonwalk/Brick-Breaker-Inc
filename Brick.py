import pygame

class Brick:
    ############
    # class vars w/ constant start values
    ###########
    width = 10
    height = 5
    brickSurface = pygame.Surface(50,100)

    #constructor function
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    #render function
    def render(self, _window):
        _x = self.x - self.width/2
        _y = self.y - self.height/2

        #drawing a rectangle
        pygame.Rect(_window, _x, _y, self.height, self.width)