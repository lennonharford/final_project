# By: Lennon Harford
# Date: 2023-05-05
# Program Details: class for the turret object, controlled by the player

import pygame
import sys
import config as conf
from pygame.math import Vector2 as Vector


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: Vector, image_path: str) -> None:
        super().__init__()
        self.size: int = conf.tile_size
        self.pixel: int = conf.pixel_size
        self.margin_left: int = conf.margin_left
        self.margin_top: int = conf.margin_top
        self.image_path: str = image_path
        self.pos: Vector = pos
        self.update()
        
    def update(self) -> None:
        self.image = pygame.transform.scale(pygame.image.load(self.image_path), self.size).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.margin_left + self.size * self.pos.x
        self.rect.y = self.margin_top + self.size * self.pos.y
