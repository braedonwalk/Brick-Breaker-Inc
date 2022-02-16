import pygame

class Player:

################
# CLASS VARS WITH CONSTANT VALUES
################

    width = 100
    height = 20
    speed = 5
    isDead = False
    size = (100,20)

    playerSurface = pygame.Surface(size)

    #load player asset
    playerBumper = pygame.image.load("Assets/50-Breakout-Tiles.png")
    playerBumper = pygame.transform.scale(playerBumper, (width,height))


    #CONSTRUCTOR
    def __init__(self, _x, _y) -> None:
        self.x = _x
        self.y = _y
        self.playerRect = pygame.Rect(_x, _y, self.width, self.height)


    def render(self, _window):
        # global playerSurface
        # global playerBumper
        _x = self.x - self.width/2
        _y = self.y - self.height/2

        self.playerRect = pygame.Rect(_x, _y, self.width, self.height)  #bumper hitbox

        # drawing rectangle
        # self.playerRect.blit(playerBumper, self.x, self.y)    #attempt at drawing asset at player location
        # playerSurface.blit(playerBumper, (0,0))
        pygame.draw.rect(_window, (255,0,0), self.playerRect)

    def move(self):
        # handle player movement from key presses
        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()
        
        if keysPressed[pygame.K_a] == True: # if the 'w' key is pressed
            self.x -= self.speed
        elif keysPressed[pygame.K_d] == True:   # if the 's' key is pressed
            self.x += self.speed
