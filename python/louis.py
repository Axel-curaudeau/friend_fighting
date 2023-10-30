import player

class Louis(player.player):
    
    def __init__(self, x, y):
        super().__init__(x, y)

        self.image = pygame.image.load("./assets/brayan.png")
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
    
    def attack():
        print("Louis attack")