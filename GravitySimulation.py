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

class Player():
    def __init__(self):
        self.color = "black"
        self.radius = 25
        self.x = SCREEN_SIZE/2 
        self.y = SCREEN_SIZE/2    # middle of the screen
        self.dy = 0  # vertical speed, starts at 0 since circle is not moving
        self.dx = 0
        self.gravity = 0.5 # gravity multipler
        self.damping = 0.7 # damping for bounce, when ball bounce it doesn't bounce back as high
        self.acceleration = 0.5   
        self.friction = 0.05

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = "red"
        
player = Player()
enemy = Enemy(0 - player.radius, random.randint(player.radius, 450) + player.radius)

bulletY = enemy.y
bulletX = enemy.x




##################### _____________GAME LOOP_______________ ##########################



######################################################################################


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
    player.dy += player.gravity # increase y down force by gravity
    player.y += player.dy # updates y position

    player.x += player.dx

    if keys[pygame.K_d]:
        player.dx += player.acceleration
    if keys[pygame.K_a]:
        player.dx -= player.acceleration


    # checks for colision with the ground
    if (player.y + player.radius > SCREEN_SIZE):

        player.y = SCREEN_SIZE - player.radius
        player.dy = -player.dy * player.damping

    if (player.y - player.radius < 0):

        player.y = player.radius
        player.dy = -(player.dy * player.damping)

    if (player.x + player.radius > SCREEN_SIZE):

        player.x = SCREEN_SIZE - player.radius
        player.dx = -player.x * player.damping

    if (player.x - player.radius < 0):

        player.x = player.radius
        player.dx = -(player.dx * player.damping)

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:

        if player.dx > 0:
            player.dx -= player.friction

            if player.dx < 0:
                player.dx = 0

        elif player.dx < 0:
            player.dx += player.friction

            if player.dx > 0:
                player.dx = 0
    
    bullet = [pygame.draw.circle(screen, "purple", (enemy.x, bulletY), 5)]
    if(random.randint(0,50) == 50):
        bullet.append(pygame.draw.circle(screen, "purple", (enemy.x, bulletY), 5))
    print(len(bullet))
    bulletY += 1


    ##### DRAW SPRITES #####
    pygame.draw.circle(screen, enemy.color, (enemy.x, enemy.y), enemy.radius)
    enemy.x += 1
    pygame.draw.circle(screen, player.color, (player.x, player.y), player.radius)
    
   
    if keys[pygame.K_SPACE]:
        #y -= 10 
        player.dy -= player.gravity*1.5

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()