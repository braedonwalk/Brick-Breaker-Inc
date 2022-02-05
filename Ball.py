import pygame

class Ball:
    ############
    # class vars w/ constant start values
    ###########
    diameter = 10
    speed = 3

    #constructor function
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    #render function\
    def render(self, _window):
        #ballCircle = pygame.circle(self.x, self.y, self.width, self.height)
        #drawing a rectangle
        #pygame.draw.circle(_window, (100,0,100), playerRect)
        return
