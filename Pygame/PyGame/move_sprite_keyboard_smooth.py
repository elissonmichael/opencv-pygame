# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame

black = (0,0,0)
white = (255,255,255)

# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):

    # -- Attributes
    # Set speed vector
    change_x=0
    change_y=0

    # -- Methods
    # Constructor function
    def __init__(self,x,y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill((white))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    # Change the speed of the player
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y

    # Find a new position for the player
    def update(self):
        self.rect.top += self.change_y
        self.rect.left += self.change_x


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Test')

# Create the player object
player = Player( 50,50 )
movingsprites = pygame.sprite.RenderPlain((player))

clock = pygame.time.Clock()
done = False

while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

        # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
            if event.key == pygame.K_UP:
                player.changespeed(0,-3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0,3)

        # Reset speed when key goes up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3,0)
            if event.key == pygame.K_UP:
                player.changespeed(0,3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0,-3)

    # This actually moves the player block based on the current speed
    player.update()

    # -- Draw everything
    # Clear screen
    screen.fill(black)

    # Draw sprites
    movingsprites.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(40)

pygame.quit()

