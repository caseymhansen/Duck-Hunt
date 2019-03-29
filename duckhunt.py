import pygame
import math
pygame.font.init()

# Sets the display size of the game
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Duck Hunter")

clock = pygame.time.Clock()

# Green Duck Sprites
greenLeft = [pygame.image.load("images/greenleft1.png"), pygame.image.load("images/greenleft2.png"), pygame.image.load("images/greenleft3.png")]
greenRight = [pygame.image.load("images/greenright1.png"), pygame.image.load("images/greenright2.png"), pygame.image.load("images/greenright3.png")]
greenDead = [pygame.image.load("images/greenleftdead.png"), pygame.image.load("images/greenrightdead.png")]

# Blue Duck Sprites
blueLeft = [pygame.image.load("images/blueleft1.png"), pygame.image.load("images/blueleft2.png"), pygame.image.load("images/blueleft3.png")]
blueRight = [pygame.image.load("images/blueright1.png"), pygame.image.load("images/blueright2.png"), pygame.image.load("images/blueright3.png")]
blueDead = [pygame.image.load("images/blueleftdead.png"), pygame.image.load("images/bluerightdead.png")]

# Red Duck Sprites
redLeft = [pygame.image.load("images/redleft1.png"), pygame.image.load("images/redleft2.png"), pygame.image.load("images/redleft3.png")]
redRight = [pygame.image.load("images/redright1.png"), pygame.image.load("images/redright2.png"), pygame.image.load("images/redright3.png")]
redDead = [pygame.image.load("images/redleftdead.png"), pygame.image.load("images/redrightdead.png")]

bg = pygame.image.load("images/background.png")
grass = pygame.image.load("images/grass.png")

# Duck Class
class duck(object):
    def __init__(self, x, y, width, height, color, vel):
        self.x = x  # X Coord of Duck
        self.y = y  # Y Coord of Duck
        self.width = width  # Width of Duck Sprite
        self.height = height  # Height of Duck Sprite
        self.color = color  # Color Code: 1-Green, 2-Blue, 3-Red
        self.vel = vel  # Velocity of duck
        self.angle = 0  # Angle of Next Flight Point
        self.dx = 0  # Change in x of next flight point
        self.dy = 0  # Change in y of next flight point
        self.left = False  # Facing left variable
        self.right = False  # Facing right variable
        self.flightCount = 0  #
        self.hitbox = -1  # Sets the hitbox of the duck

    # Draws the duck
    def draw(self, win):
        self.move()
        if self.flightCount + 1 >= 30:
            self.flightCount = 0
        if self.left:
            if self.color == 1:
                win.blit(greenLeft[self.flightCount // 10], (self.x - self.width/2, self.y - self.height/2))
                self.flightCount += 1
            elif self.color == 2:
                win.blit(blueLeft[self.flightCount // 10], (self.x - self.width/2, self.y - self.height/2))
                self.flightCount += 1
            elif self.color == 3:
                win.blit(redLeft[self.flightCount // 10], (self.x - self.width/2, self.y - self.height/2))
                self.flightCount += 1
        elif self.right:
            if self.color == 1:
                win.blit(greenRight[self.flightCount // 10], (self.x - self.width/2, self.y - self.height/2))
                self.flightCount += 1
            elif self.color == 2:
                win.blit(blueRight[self.flightCount // 10], (self.x - self.width/2, self.y - self.height/2))
                self.flightCount += 1
            elif self.color == 3:
                win.blit(redRight[self.flightCount // 10], (self.x - self.width/2, self.y - self.height/2))
                self.flightCount += 1
        else:
            if self.color == 1:
                win.blit(greenRight[0], (self.x - self.width/2, self.y - self.height/2))
            elif self.color == 2:
                win.blit(blueRight[0], (self.x - self.width/2, self.y - self.height/2))
            elif self.color == 3:
                win.blit(redRight[0], (self.x - self.width/2, self.y - self.height/2))

    def flightPoint(self):
        xPoint = 600  # Change to make it choose random x coordinate
        yPoint = 100  # Change to make it choose random y coordinate
        self.angle = math.atan2(yPoint - self.y, xPoint - self.x)
        self.dx = math.cos(self.angle) * self.vel
        self.dy = -math.sin(self.angle) * self.vel

    def move(self):
        if self.vel > 0:
            if self.right:
                self.x += self.dx
                self.y -= self.dy
            elif self.left:
                self.x += self.dx
                self.y -= self.dy

def redrawGameWindow():
    win.blit(bg, (0, 0))
    test.draw(win)
    pygame.draw.circle(win, (255, 0, 0), (600, 100), 5)
    win.blit(grass, (0, 0))
    pygame.display.update()


# Main Loop
run = True
ducks = []
test = duck(100, 420, 60, 60, 1, 5)
test.right = True
test.flightPoint()

score = 0

while run:
    clock.tick(30)
    # Closes the game window when the X in the top left is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    redrawGameWindow()

pygame.quit()
