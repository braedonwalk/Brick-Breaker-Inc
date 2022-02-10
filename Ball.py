import pygame

class Ball:
    ############
    # class vars w/ constant start values
    ###########
    radius = 7
    speed = 3

    #constructor function
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        #ball bounds
        rightBound = self.x + self.radius
        leftBound = self.x - self.radius
        bottomBound = self.y + self.radius
        topBound = self.y - self.radius


    #render function
    def render(self, _window):

        _x = self.x - self.radius/2
        _y = self.y - self.radius/2

        #drawing a cirlce
        pygame.draw.circle(_window, (255,255,255), (_x, _y), self.radius)

    