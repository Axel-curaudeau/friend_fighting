import pygame
from config import window_size

class player:

    def __init__(self, x, y, asset_path, name):
        self.name = name

        # movement
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.x_drag = 2.5
        self.is_pushed = False

        # stats
        self.health = 100
        self.base_damage = 10
        self.height = 200
        self.width = 200
        self.is_jumping = False
        self.jump_speed = 30
        self.attack_width = 100
        

        # image
        self.image = pygame.image.load(asset_path + "idle.png").convert_alpha()
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.anim_sheet = pygame.image.load(asset_path + "walk_anim.png").convert_alpha()
        self.walk_anim = []
        self.walk_anim_step = 0
        self.walk_anim_update_time = pygame.time.get_ticks()
        for i in range(2):
            temp_image = self.anim_sheet.subsurface((i * 64, 0, 64, 64))
            self.walk_anim.append(pygame.transform.scale(temp_image, (self.width, self.height)))
        self.is_flipped = False
    

    def draw(self, screen):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(screen, (0, 0, 255), self.hitbox)
        screen.blit(self.scaled_image, (self.x, self.y))
    
    
    def border_collision(self, window_size):
        if (self.x < 0):
            self.x = 0
        if (self.x > window_size[0] - self.width):
            self.x = window_size[0] - self.width
        if (self.y > window_size[1] - self.height):
            self.y_speed = 0
            self.is_pushed = False
            self.y = window_size[1] - self.height
            self.is_jumping = False


    def horizontal_drag(self):
        if (self.is_pushed):
            return
        if (self.x_speed > 0):
            self.x_speed -= self.x_drag
        if (self.x_speed < 0):
            self.x_speed += self.x_drag
        if (self.x_speed < self.x_drag and self.x_speed > -self.x_drag):
            self.x_speed = 0


    def update(self, screen):
        self.draw(screen)

        self.x += self.x_speed
        self.y += self.y_speed
        
        self.horizontal_drag()
        self.gravity()
        self.border_collision(window_size)
    

    def gravity(self):
        self.y_speed += 2
        

    def flip_image(self, flip):
            if self.is_flipped != flip:
                self.scaled_image = pygame.transform.flip(self.scaled_image, True, False)
                self.is_flipped = not(self.is_flipped)
    

    def animate(self, cooldown):
        if (self.walk_anim_update_time + cooldown < pygame.time.get_ticks()):
            self.walk_anim_update_time = pygame.time.get_ticks()
            self.walk_anim_step += 1
            if (self.walk_anim_step >= len(self.walk_anim)):
                self.walk_anim_step = 0
            self.scaled_image = self.walk_anim[self.walk_anim_step]
            if (self.is_flipped):
                self.scaled_image = pygame.transform.flip(self.scaled_image, True, False)


    def move_horizontal(self, x_speed):
        if (self.is_pushed and self.x_speed < x_speed):
            self.x_speed += x_speed/10
        else:
            self.x_speed = x_speed
        self.animate(200)
        if (self.x_speed > 0):
            self.flip_image(False)
        elif (self.x_speed < 0):
            self.flip_image(True)

    def move_vertical(self, y_speed):
        if not(self.is_jumping):
            self.y_speed = y_speed
        if (self.y_speed < 0):
            self.is_jumping = True
    
    def get_hitbox(self):
        return self.hitbox
    
    def attack(self, enemy):
        if (self.is_pushed):
            return
        if (self.is_flipped):
            attack_rect = pygame.Rect(self.x - self.attack_width, self.y, self.width + self.attack_width, self.height)
        else:
            attack_rect = pygame.Rect(self.x, self.y, self.width + self.attack_width, self.height)
        if (attack_rect.colliderect(enemy.get_hitbox())):
            enemy.health -= self.base_damage
            enemy.x_speed = 20 * (-1 if self.is_flipped else 1)
            enemy.y_speed = -30
            enemy.is_pushed = True

        #pygame.draw.rect(screen, (255, 0, 0), attack_rect)

    def reset(self, x, y):
        self.health = 100
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.is_jumping = False
        self.walk_anim_step = 0
        self.walk_anim_update_time = pygame.time.get_ticks()
        self.scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        self.is_flipped = False