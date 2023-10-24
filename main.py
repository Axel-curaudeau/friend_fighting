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

# Draw the background
def draw_background():
    background = pygame.image.load("./assets/background_garage.jpg")
    scaled = pygame.transform.scale(background, window_size)
    screen.blit(scaled, (0, 0))

# Create the player
player = joueur.joueur(100, 100)

# Game loop
while running:
    draw_background()
    player.draw(screen)
    player.move(window_size=window_size)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
