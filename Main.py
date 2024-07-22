import pygame

# pygame setup
SCREEN_SIZE = 500
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Gravity Simulation")
clock = pygame.time.Clock()
running = True

color = "black"
radius = 25

x, y = SCREEN_SIZE/2 , SCREEN_SIZE/2    # middle of the screen
dy = 0  # vertical speed, starts at 0 since circle is not moving
gravity = 0.5 # gravity multipler
damping = 0.7 # damping for bounce, when ball bounce it doesn't bounce back as high

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    dy += gravity # increase y down force by gravity
    y += dy # updates y position

    # checks for colision with the ground
    if (y + radius > SCREEN_SIZE):
        y = SCREEN_SIZE - radius
        dy = -dy * damping

    pygame.draw.circle(screen, color, (x, y), radius)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()