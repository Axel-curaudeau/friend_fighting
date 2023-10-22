import pygame
import joueur

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Friend Fighting")

# Set up the game loop
clock = pygame.time.Clock()
running = True

# Create the player
player = joueur.joueur(100, 100)

# Game loop
while running:

    player.draw(screen)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
