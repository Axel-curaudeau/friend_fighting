import pygame
import game
from config import window_size

class main_menu:

    def __init__(self):

        self.font = pygame.font.Font('./assets/Sweet Scream Free.ttf', 40)
        self.button_size = (200, 50)
        self.text_color = (0, 0, 0)
        self.base_button_color = (255, 255, 255)
        self.hover_button_color = (180, 180, 180)

        self.play_button_coord = (window_size[0] / 2 - self.button_size[0] / 2, window_size[1] / 2 - self.button_size[1] / 2)
        self.play_button_color = self.base_button_color

        self.settings_button_coord = (window_size[0] / 2 - self.button_size[0] / 2, window_size[1] / 2 + self.button_size[1])
        self.settings_button_color = self.base_button_color

        self.quit_button_rect = pygame.rect.Rect(window_size[0] / 2 - self.button_size[0] / 2, window_size[1] / 2 + 2.5 * self.button_size[1], self.button_size[0], self.button_size[1])
        self.quit_button_color = self.base_button_color

    def run(self, screen, game):
        game.draw_background(screen)

        #draw play button
        pygame.draw.rect(screen, self.play_button_color, (self.play_button_coord, self.button_size))
        text = self.font.render('Play', True, self.text_color)
        screen.blit(text, (self.play_button_coord[0] - text.get_width() / 2 + self.button_size[0] / 2, self.play_button_coord[1]))

        #draw settings button
        pygame.draw.rect(screen, self.settings_button_color, (self.settings_button_coord, self.button_size))
        text = self.font.render('Settings', True, self.text_color)
        screen.blit(text, (self.settings_button_coord[0] - text.get_width() / 2 + self.button_size[0] / 2, self.settings_button_coord[1]))

        pygame.draw.rect(screen, self.quit_button_color, self.quit_button_rect)
        text = self.font.render('Quit', True, self.text_color)
        screen.blit(text, (self.quit_button_rect.x - text.get_width() / 2 + self.button_size[0] / 2, self.quit_button_rect.y))


        #get mouse position and react
        mouse_pos = pygame.mouse.get_pos()
        event = pygame.event.poll()
        if (pygame.rect.Rect((self.play_button_coord, self.button_size)).collidepoint(mouse_pos)):
            self.play_button_color = self.hover_button_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.player_left.reset(100, 100)
                game.player_right.reset(window_size[0] - 300, 100)
                game.status = "game"
        else:
            self.play_button_color = self.base_button_color
        
        if (pygame.rect.Rect((self.settings_button_coord, self.button_size)).collidepoint(mouse_pos)):
            self.settings_button_color = self.hover_button_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('settings')
        else:
            self.settings_button_color = self.base_button_color
        
        if (self.quit_button_rect.collidepoint(mouse_pos)):
            self.quit_button_color = self.hover_button_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.running = False
        else:
            self.quit_button_color = self.base_button_color