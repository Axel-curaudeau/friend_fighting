import pygame
import player

class Fiktou(player.player):

    def __init__(self, x, y):
        super().__init__(x, y, "assets/Fiktou/")
        
    

    def attack(self, screen):
        print("Fiktou attack")