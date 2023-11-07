import pygame

class UI:

    def __init__(self, window_size):
        self.health_bar_width = 400
        self.health_bar_height = 20
        self.health_bar_x_offset = 10
        self.health_bar_y_offset = 10
        self.left_player_health_bar = pygame.Rect(self.health_bar_x_offset, self.health_bar_y_offset, self.health_bar_width, self.health_bar_height)
        self.right_player_health_bar = pygame.Rect(window_size[0] - self.health_bar_width - self.health_bar_x_offset, self.health_bar_y_offset, self.health_bar_width, self.health_bar_height)
        
        self.health_bar_border_width = 3
        self.health_bar_border_color = (0, 0, 0)
        self.left_player_health_bar_border = pygame.Rect(self.health_bar_x_offset - self.health_bar_border_width, self.health_bar_y_offset - self.health_bar_border_width, self.health_bar_width + self.health_bar_border_width * 2, self.health_bar_height + self.health_bar_border_width * 2)
        self.right_player_health_bar_border = pygame.Rect(window_size[0] - self.health_bar_width - self.health_bar_x_offset - self.health_bar_border_width, self.health_bar_y_offset - self.health_bar_border_width, self.health_bar_width + self.health_bar_border_width * 2, self.health_bar_height + self.health_bar_border_width * 2)



    def draw(self, screen, left_player_health, right_player_health):
        pygame.draw.rect(screen, (0, 255, 0), (self.left_player_health_bar.x, self.left_player_health_bar.y, self.left_player_health_bar.width * (left_player_health / 100), self.left_player_health_bar.height))
        pygame.draw.rect(screen, (255, 0, 0), (self.right_player_health_bar.x, self.right_player_health_bar.y, self.right_player_health_bar.width * (right_player_health / 100), self.right_player_health_bar.height))
        pygame.draw.rect(screen, self.health_bar_border_color, self.left_player_health_bar_border, self.health_bar_border_width)
        pygame.draw.rect(screen, self.health_bar_border_color, self.right_player_health_bar_border, self.health_bar_border_width)