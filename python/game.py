import pygame
import player
import menu
import fiktou

class game:

    def __init__(self):
        self.window_size = (1280, 720)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Friend Fighting")

        # Set up the game loop
        self.clock = pygame.time.Clock()
        self.running = True
        self.status = "main_menu"

        print("Starting game...")

        #Create the menu
        self.menu = menu.main_menu(self.window_size)

        # Create the player
        self.player_left = fiktou.Fiktou(100, 100)
        self.player_right = player.player(200, 100)

    def run(self):
        while self.running:
            if self.status == "main_menu":
                self.menu.run(self.screen, self.window_size, self)
            elif self.status == "game":
                self.input()
                self.draw_background(self.screen, self.window_size)
                self.player_left.update(self.window_size, self.screen)
                self.player_right.update(self.window_size, self.screen)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

        # Limit the frame rate
        self.clock.tick(60)

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.player_left.move_horizontal(10)
        if key[pygame.K_q]:
            self.player_left.move_horizontal(-10)
        if key[pygame.K_z]:
            self.player_left.move_vertical(-30)
        if key[pygame.K_g]:
            self.player_left.attack()
        else:
            pass

# Draw the background
    def draw_background(self, screen, window_size):
        background = pygame.image.load("./assets/background_garage.jpg")
        scaled = pygame.transform.scale(background, window_size)
        screen.blit(scaled, (0, 0))