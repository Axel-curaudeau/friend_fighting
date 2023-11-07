import pygame
from config import window_size

class end_screen:
    
    def __init__(self):
        self.font = pygame.font.Font('./assets/Sweet Scream Free.ttf', 32)
        self.restart_button_size = (200, 50)
        self.restart_button_coord = (window_size[0] / 2 - self.restart_button_size[0] / 2, window_size[1] / 2 - self.restart_button_size[1] / 2)
        self.restart_button_color = (255, 255, 255)

    def run(self, player_left, player_right, screen, game):
        if player_left.health <= 0:
            text = self.font.render(player_right.name + " wins!", True, (0, 0, 0))
        if player_right.health <= 0:
            text = self.font.render(player_left.name + " wins!", True, (0, 0, 0))
        screen.blit(text, (100, 100))

        pygame.draw.rect(screen, self.restart_button_color, (self.restart_button_coord, self.restart_button_size))
        text = self.font.render('Restart', True, (0, 0, 0))
        screen.blit(text, (self.restart_button_coord[0] + 50, self.restart_button_coord[1] + 10))

        mouse_pos = pygame.mouse.get_pos()
        if (mouse_pos[0] > self.restart_button_coord[0] and mouse_pos[0] < self.restart_button_coord[0] + self.restart_button_size[0] 
            and mouse_pos[1] > self.restart_button_coord[1] and mouse_pos[1] < self.restart_button_coord[1] + self.restart_button_size[1]):
            self.restart_button_color = (255, 0, 0)
            if pygame.mouse.get_pressed()[0]:
                player_left.reset(100, 100)
                player_right.reset(window_size[0] - 300, 100)
                game.status = "game"
        else:
            self.restart_button_color = (255, 255, 255)