import pygame

class UI:

    def __init__(self, window_size):
        self.left_player_health_bar = pygame.Rect(0, 0, 200, 20)
        self.right_player_health_bar = pygame.Rect(window_size[0] - 200, 0, 200, 20)


    def draw(self, screen, left_player_health, right_player_health):
        pygame.draw.rect(screen, (0, 255, 0), (self.left_player_health_bar.x, self.left_player_health_bar.y, self.left_player_health_bar.width * (left_player_health / 100), self.left_player_health_bar.height))
        pygame.draw.rect(screen, (255, 0, 0), (self.right_player_health_bar.x, self.right_player_health_bar.y, self.right_player_health_bar.width * (right_player_health / 100), self.right_player_health_bar.height))