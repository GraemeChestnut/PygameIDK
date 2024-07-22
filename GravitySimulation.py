import pygame
import random

# pygame setup
SCREEN_SIZE = 500
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Gravity Simulation")
clock = pygame.time.Clock()
running = True

####### PLAYER VARIABLES ########
color = "black"
radius = 25

x, y = SCREEN_SIZE/2 , SCREEN_SIZE/2    # middle of the screen
dy = 0  # vertical speed, starts at 0 since circle is not moving
dx = 0
gravity = 0.5 # gravity multipler
damping = 0.7 # damping for bounce, when ball bounce it doesn't bounce back as high
acceleration = 0.5   
friction = 0.05

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = "red"
        

enemy = Enemy(0 - radius, random.randint(radius, 450) + radius)
bulletY = enemy.y

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed() # y movement

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    dy += gravity # increase y down force by gravity
    y += dy # updates y position

    x += dx

    if keys[pygame.K_d]:
        dx += acceleration
    if keys[pygame.K_a]:
        dx -= acceleration


    # checks for colision with the ground
    if (y + radius > SCREEN_SIZE):
        y = SCREEN_SIZE - radius
        dy = -dy * damping
    if (y - radius < 0):
        y = radius
        dy = -(dy * damping)
    if (x + radius > SCREEN_SIZE):
        x = SCREEN_SIZE - radius
        dx = -dx * damping
    if (x - radius < 0):
        x = radius
        dx = -(dx * damping)

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if dx > 0:
            dx -= friction
            if dx < 0:
                dx = 0
        elif dx < 0:
            dx += friction
            if dx > 0:
                dx = 0
    
        
    bullet = pygame.draw.circle(screen, "purple", (enemy.x, bulletY), 5)
    bulletY += 1


    ##### DRAW SPRITES #####
    pygame.draw.circle(screen, enemy.color, (enemy.x, enemy.y), enemy.radius)
    enemy.x += 1
    pygame.draw.circle(screen, color, (x, y), radius)
    
   
    if keys[pygame.K_SPACE]:
        #y -= 10 
        dy -= gravity*1.5

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()