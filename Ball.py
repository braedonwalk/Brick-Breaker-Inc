import pygame

class Ball:
    ############
    # class vars w/ constant start values
    ###########
    width = 10
    height = 10
    #radius = 5
    speed = 3

    #constructor function
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    #render function
    def render(self, _window):
        Ball = pygame.Rect(self.x, self.y, self.width, self.height)
        #drawing a rectangle
        pygame.draw.rect(_window, (255,0,0), Ball)