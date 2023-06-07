# By: Lennon Harford
# Date: 2023-05-05
# Program Details: class for the turret object, controlled by the player

import pygame
import sys
import config as conf
from vector import Vector

# class Tile(pygame.sprite.Sprite):
#     def __init__(self, pos: Vector, image_path: str) -> None:
#         super().__init__()
#         self.size: int = conf.tile_size
#         self.margin_left: int = conf.margin_left
#         self.margin_top: int = conf.margin_top
#         self.image_path: str = image_path
#         self.pos: Vector = pos
#         self.update()
        
#     def update(self) -> None:
#         self.image = pygame.transform.scale(pygame.image.load(self.image_path), self.size).convert_alpha()
#         self.mask = pygame.mask.from_surface(self.image)
#         self.rect = self.image.get_rect()
#         self.rect.x = self.margin_left + self.size * self.pos.x
#         self.rect.y = self.margin_top + self.size * self.pos.y

def get_image(x: int, y: int, size: int, path: str) -> pygame.Surface:
    try:
        sheet = pygame.image.load(path).convert()
    except pygame.error as e:
        raise SystemExit(e)
    
    rect = pygame.Rect(x, y, x+size, y+size)
    image = pygame.Surface(rect.size).convert_alpha()
    image.blit(sheet, (0, 0), rect)

    return image 

class Tile(pygame.sprite.Sprite):
    def __init__(self, tilex, tiley) -> None:
        super().__init__()
        self.pos = Vector(tilex, tiley)
        self.size: int = conf.tile_size
        self.margin_left: int = conf.margin_left
        self.margin_top: int = conf.margin_top
        
    # def update(self) -> None:
    #     self.image = pygame.transform.scale(pygame.image.load(self.image_path), self.size).convert_alpha()
    #     self.mask = pygame.mask.from_surface(self.image)
    #     self.rect = self.image.get_rect()
    #     self.rect.x = self.margin_left + self.size * self.pos.x
    #     self.rect.y = self.margin_top + self.size * self.pos.y
    
    def draw_1(self, sheet: str):
        #self.image = pygame.transform.scale(pygame.image.load(self.image_path), self.size).convert_alpha()
        self.sheet: str = sheet
        self.image: pygame.Surface = get_image(self.pos.x, self.pos.y, self.size, sheet)
        self.mask: pygame.mask.Mask = pygame.mask.from_surface(self.image)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x: float = self.margin_left + self.size * self.pos.x
        self.rect.y: float = self.margin_top + self.size * self.pos.y
    
    def draw(self, sheet, tile):
        pass