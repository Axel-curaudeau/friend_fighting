import pygame

class joueur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        #self.image = pygame.image.load("assets/player.png")
    
    def draw(self, screen):
        #screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 60, 60))
    
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed