import pygame
from config import window_size

class pause_menu:

    def __init__(self):

        self.font = pygame.font.Font('./assets/Sweet Scream Free.ttf', 40)
        self.button_size = (200, 50)
        self.text_color = (0, 0, 0)
        self.base_button_color = (255, 255, 255)
        self.hover_button_color = (180, 180, 180)

        self.resume_button_rect = pygame.rect.Rect(window_size[0] / 2 - self.button_size[0] / 2, window_size[1] / 2 - self.button_size[1] / 2, self.button_size[0], self.button_size[1])
        self.resume_button_color = self.base_button_color

        self.settings_button_rect = pygame.rect.Rect(window_size[0] / 2 - self.button_size[0] / 2, window_size[1] / 2 + self.button_size[1], self.button_size[0], self.button_size[1])
        self.settings_button_color = self.base_button_color

        self.return_main_menu_button_rect = pygame.rect.Rect(window_size[0] / 2 - self.button_size[0] / 2, window_size[1] / 2 + 2.5 * self.button_size[1], self.button_size[0], self.button_size[1])
        self.return_main_menu_button_color = self.base_button_color
    
    def run(self, screen, game):

        #draw resume button
        pygame.draw.rect(screen, self.resume_button_color, self.resume_button_rect)
        text = self.font.render('Resume', True, self.text_color)
        screen.blit(text, (self.resume_button_rect.x - text.get_width() / 2 + self.button_size[0] / 2, self.resume_button_rect.y))

        #draw settings button
        pygame.draw.rect(screen, self.settings_button_color, self.settings_button_rect)
        text = self.font.render('Settings', True, self.text_color)
        screen.blit(text, (self.settings_button_rect.x - text.get_width() / 2 + self.button_size[0] / 2, self.settings_button_rect.y))

        pygame.draw.rect(screen, self.return_main_menu_button_color, self.return_main_menu_button_rect)
        text = self.font.render('Main menu', True, self.text_color)
        screen.blit(text, (self.return_main_menu_button_rect.x - text.get_width() / 2 + self.button_size[0] / 2, self.return_main_menu_button_rect.y))


        #get mouse position and react
        mouse_pos = pygame.mouse.get_pos()
        event = pygame.event.poll()
        if (self.resume_button_rect.collidepoint(mouse_pos)):
            self.resume_button_color = self.hover_button_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.status = "game"
        else:
            self.resume_button_color = self.base_button_color
        
        if (self.settings_button_rect.collidepoint(mouse_pos)):
            self.settings_button_color = self.hover_button_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('settings')
        else:
            self.settings_button_color = self.base_button_color
        
        if (self.return_main_menu_button_rect.collidepoint(mouse_pos)):
            self.return_main_menu_button_color = self.hover_button_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.status = "main_menu"
                game.clock
        else:
            self.return_main_menu_button_color = self.base_button_color
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.status = "game"
