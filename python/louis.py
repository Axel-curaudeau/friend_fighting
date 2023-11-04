import player
import pygame

class Louis(player.player):

    def __init__(self, x, y):
        super().__init__(x, y, "assets/Louis/")
    
    def attack(self, screen):
        attack_rect = pygame.Rect(self.x, self.y, 2 * self.width, self.height)

        pygame.draw.rect(screen, (255, 0, 0), attack_rect)
        print("Louis attack")