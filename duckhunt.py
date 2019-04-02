import pygame
import math
import random
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
class duck:
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
        self.flightCount = 0  # Used for the duck animation

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
        """else:
            if self.color == 1:
                win.blit(greenRight[0], (self.x - self.width/2, self.y - self.height/2))
            elif self.color == 2:
                win.blit(blueRight[0], (self.x - self.width/2, self.y - self.height/2))
            elif self.color == 3:
                win.blit(redRight[0], (self.x - self.width/2, self.y - self.height/2))"""

    def flightPoint(self):
        xPoint = random.randint(350, 750)  # Change to make it choose random x coordinate
        yPoint = 100  # Change to make it choose random y coordinate
        if self.x < xPoint:
            self.right = True
        elif self.x > xPoint:
            self.left = True
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
    for fly in ducks:
        fly.draw(win)
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (50, 525))
    timer = font.render(str(time)[0:4], 1, (0, 0, 0))
    win.blit(timer, (380, 525))
    greenScore = font.render("Green: 25 Points", 1, (0, 0, 0))
    blueScore = font.render("Blue: 50 Points", 1, (0, 0, 0))
    redScore = font.render("Red: 75 Points", 1, (0, 0, 0))
    win.blit(greenScore, (600, 510))
    win.blit(blueScore, (600, 535))
    win.blit(redScore, (600, 560))
    win.blit(grass, (0, 0))
    pygame.display.update()

def drawGameOver():
    win.fill((0, 0, 0))
    gameOver = font.render("Your Score: " + str(score), 1, (255, 255, 255))
    win.blit(gameOver, (300, 200))
    pygame.display.update()

def addDuck():
    newX = random.randint(100, 700)
    newColor = random.randint(1, 3)
    velocity = -1
    if newColor == 1:
        velocity = 5
    elif newColor == 2:
        velocity = 6
    elif newColor == 3:
        velocity = 7
    newDuck = duck(newX, 420, 60, 60, newColor, velocity)
    newDuck.flightPoint()
    ducks.append(newDuck)
    newDuck.draw(win)


run = True
ducks = []
font = pygame.font.SysFont('Comic Sans MS', 24, True)
pygame.time.set_timer(pygame.USEREVENT, 100)
time = 30.0
score = 0
duckCount = 0

# Main Loop
while run:
    clock.tick(30)
    # Closes the game window when the X in the top left is clicked
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            if time <= 0:
                drawGameOver()
                pygame.time.delay(5000)
                run = False
                break
            time -= 0.1
        if event.type == pygame.QUIT:
            run = False

    duckCount = len(ducks)
    while duckCount < 7:
        addDuck()
        duckCount = len(ducks)

    # Checks if the ducks on the screen have flown off the screen and will delete them from the screen
    for flyboi in ducks:
        if flyboi.y <= 0 or flyboi.x >= 800 or flyboi.x <= 0:
            ducks.pop(ducks.index(flyboi))

    # Code for shooting the ducks and removing them from the screen
    event = pygame.event.get()
    if pygame.mouse.get_pressed()[0]:
        # Gets the position of the mouse cursor on the screen and returns it in a tuple form (x, y)
        mousePos = pygame.mouse.get_pos()
        for flyboi in ducks:
            if math.sqrt(math.pow(flyboi.x - mousePos[0], 2) + math.pow(flyboi.y - mousePos[1], 2)) < 30:
                if ducks.__contains__(flyboi):
                    if flyboi.color == 1:
                        score += 25
                    elif flyboi.color == 2:
                        score += 50
                    elif flyboi.color == 3:
                        score += 75
                    ducks.pop(ducks.index(flyboi))

    redrawGameWindow()

pygame.quit()
