# By: Lennon Harford
# Date: 2023-05-05
# Program Details: class for the turret object, controlled by the player

import pygame
import sys
from game import Game

class Turret(pygame.sprite.Sprite):
    def __init__(self, game: Game) -> None:
        super().__init__()
        self.game = game
        self.size = self.game.sprite_size
        self.pixel = self.game.pixel_size
        image_path = "assets/images/turret.png"
        self.image = pygame.transform.scale(pygame.image.load(image_path), (self.size, self.size)).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.game.window_width/2
        self.rect.y = self.game.window_height - self.game.window_margin - self.game.sprite_size
        self.move = 2
        self.shot = False
        self.clock_speed = 1
        self.timer = self.clock_speed
        self.move_x = 0
        
    def update(self) -> None:
        self.shot = False
        keys = pygame.key.get_pressed()
        
        is_moving_left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        is_moving_right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        
        self.move_x = (is_moving_left * -(self.move * self.pixel)) + (is_moving_right * (self.move * self.pixel))
        self.rect.x += self.move_x
        
        if self.timer == 0:
            if keys[pygame.K_SPACE]:
                self.shot = True
                self.timer = self.clock_speed
        else:
            self.timer -= 1
