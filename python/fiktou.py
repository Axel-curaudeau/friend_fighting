import pygame
import player

class Fiktou(player.player):

    def __init__(self, x, y, enemy):
        super().__init__(x, y, "assets/Fiktou/")
        self.attack_width = 100
        self.enemy = enemy
        
    

    def attack(self, screen):
        attack_rect = pygame.Rect(self.x, self.y, self.width + self.attack_width, self.height)
        if (attack_rect.colliderect(self.enemy)):
            print("hit")

        pygame.draw.rect(screen, (255, 0, 0), attack_rect)