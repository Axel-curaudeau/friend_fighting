import pygame
import end_screen
import main_menu
import fiktou
import louis
import HUD
import config
import pause_menu

class game:

    def __init__(self):
        if (config.fullscreen):
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(config.window_size)
        pygame.display.set_caption("Friend Fighting")
        
        # Create the clock
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.status = "main_menu"

        print("Starting game...")

        #Create the menu
        self.menu = main_menu.main_menu()

        # Create the UI
        self.HUD = HUD.HUD()

        # Create the pause menu
        self.pause_menu = pause_menu.pause_menu()

        # Create the end screen
        self.end_screen = end_screen.end_screen()

         # Create the player
        self.player_left = fiktou.Fiktou(100, 100)
        self.player_right = louis.Louis(config.window_size[0] - 300, 100)
        self.player_right.flip_image(True)


    def run(self):
        while self.running:

            if self.status == "main_menu":
                self.menu.run(self.screen, self)

            elif self.status == "game":
                self.draw_background(self.screen)
                self.input()
                self.HUD.draw(self.screen, self.player_left.health, self.player_right.health)
                self.player_left.update(self.screen)
                self.player_right.update(self.screen)

                # Check if the game is over
                if self.player_left.health <= 0 or self.player_right.health <= 0:
                    self.status = "end_screen"
            
            elif self.status == "pause_menu":
                self.pause_menu.run(self.screen, self)
            
            elif self.status == "end_screen":
                self.end_screen.run(self.player_left, self.player_right, self.screen, self)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            # Limit the frame rate
            self.clock.tick(config.framerate)

    def input(self):
        key = pygame.key.get_pressed()

        # left player controls
        if key[pygame.K_d]:
            self.player_left.move_horizontal(10)
        if key[pygame.K_q]:
            self.player_left.move_horizontal(-10)
        if key[pygame.K_z]:
            self.player_left.move_vertical(-30)

        # right player controls
        if key[pygame.K_RIGHT]:
            self.player_right.move_horizontal(10)
        if key[pygame.K_LEFT]:
            self.player_right.move_horizontal(-10)
        if key[pygame.K_UP]:
            self.player_right.move_vertical(-30)

        else:
            pass
            
        #get key down
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                self.player_left.attack(self.player_right)
            if event.key == pygame.K_RCTRL:
                self.player_right.attack(self.player_left)
            if event.key == pygame.K_ESCAPE:
                self.status = "pause_menu"

# Draw the background
    def draw_background(self, screen):
        background = pygame.image.load("./assets/background_garage.jpg")
        scaled = pygame.transform.scale(background, config.window_size)
        screen.blit(scaled, (0, 0))