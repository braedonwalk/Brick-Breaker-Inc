import pygame

class Player:

################
# CLASS VARS WITH CONSTANT VALUES
################

    width = 100
    height = 20
    speed = 5
    isDead = False

    #CONSTRUCTOR
    def __init__(self, _x, _y) -> None:
        self.x = _x
        self.y = _y

    def render(self, _window):
        playerRect = pygame.Rect(self.x, self.y, self.width, self.height)

        # drawing rectangle
        pygame.draw.rect(_window, (255,0,0), playerRect)
