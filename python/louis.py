import player
import pygame

class Louis(player.player):

    def __init__(self, x, y):
        super().__init__(x, y, "assets/Louis/", "Louis")