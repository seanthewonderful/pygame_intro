# Import and initialize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


pygame.init()

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instatiate player. Right now, this is just a rectangle.
player = Player()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill((0, 0, 0))

    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50, 50))

    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    # This line says 'Draw surf onto the screen at the center'
    # 2 args - the surface to draw, the location at which to draw it on the source surface
    screen.blit(surf, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    pygame.display.flip()

# Put the center of the surf at the center of the display
surf_center = (
    (SCREEN_WIDTH - surf.get_width()) / 2,
    (SCREEN_HEIGHT - surf.get_height()) / 2,
)

# Draw surf at the new coordinates
screen.blit(surf, surf_center)
pygame.display.flip()
