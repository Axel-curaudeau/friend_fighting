import pygame

class joueur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.x_drag = 2
        self.y_drag = 1
        self.health = 100
        self.base_damage = 10
        self.height = 100
        self.width = 100
        self.image = pygame.image.load("./assets/brayan.jpg")
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.is_jumping = False
        self.jump_speed = 20
    
    def draw(self, screen):
        screen.blit(self.scaled_image, (self.x, self.y))
    
    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.x_speed = 5
        if key[pygame.K_q]:
            self.x_speed = -5
        if key[pygame.K_z] and not(self.is_jumping):
            self.y_speed = -self.jump_speed
            self.is_jumping = True

    def border_collision(self, window_size):
        if (self.x < 0):
            self.x = 0
        if (self.x > window_size[0] - self.width):
            self.x = window_size[0] - self.width
        if (self.y > window_size[1] - self.height):
            self.y_speed = 0
            self.y = window_size[1] - self.height
            self.is_jumping = False

    def horizontal_drag(self):
        if (self.x_speed > 0):
            self.x_speed -= self.x_drag
        if (self.x_speed < 0):
            self.x_speed += self.x_drag
        if (self.x_speed < self.x_drag and self.x_speed > -self.x_drag):
            self.x_speed = 0

    def move(self, window_size):
        self.input()

        self.x += self.x_speed
        self.y += self.y_speed
        
        self.horizontal_drag()
        self.gravity()
        self.border_collision(window_size)
    
    def gravity(self):
        self.y_speed += 1
        

        