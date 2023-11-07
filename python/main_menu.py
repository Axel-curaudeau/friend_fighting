import pygame
import game
from config import window_size

class main_menu:

    def __init__(self):

        self.font = pygame.font.Font('./assets/Sweet Scream Free.ttf', 32)

        self.button_size = (200, 50)
        self.play_button_coord = (window_size[0] / 2 - self.button_size[0] / 2, window_size[1] / 2 - self.button_size[1] / 2)
        self.play_button_color = (255, 255, 255)


    def run(self, screen, game):
        game.draw_background(screen)
        pygame.draw.rect(screen, self.play_button_color, (self.play_button_coord, self.button_size))
        text = self.font.render('Play', True, (0, 0, 0))
        screen.blit(text, (self.play_button_coord[0] + 50, self.play_button_coord[1] + 10))

        mouse_pos = pygame.mouse.get_pos()
        if (mouse_pos[0] > self.play_button_coord[0] and mouse_pos[0] < self.play_button_coord[0] + self.button_size[0] 
            and mouse_pos[1] > self.play_button_coord[1] and mouse_pos[1] < self.play_button_coord[1] + self.button_size[1]):
            self.play_button_color = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                game.player_left.reset(100, 100)
                game.player_right.reset(window_size[0] - 300, 100)
                game.status = "game"
                #screen.fill((0, 0, 0))
        else:
            self.play_button_color = (255, 255, 255)