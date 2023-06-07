import pygame
import sys
import config as conf
from vector import Vector

class Chunk(pygame.sprite.Sprite):
    def __init__(self, sheet, array) -> None:
        super().__init__()
        self.margin_left: int = conf.margin_left
        self.margin_top: int = conf.margin_top
        self.margin = conf.window_margin
        self.size: Vector = Vector(2*conf.window_margin + conf.chunk_dimensions.x*conf.tile_size, 2*conf.window_margin + conf.chunk_dimensions.y*conf.tile_size)
        
        self.load(sheet, array)

    def load(self, sheet, array):
        self.sheet: str = sheet   
        self.array = array     
        self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(self.sheet), (self.size.x, self.size.y)).convert_alpha()
        self.mask: pygame.mask.Mask = pygame.mask.from_surface(self.image)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x: float = self.margin
        self.rect.y: float = self.margin
        # self.rect.x: float = self.margin_left
        # self.rect.y: float = self.margin_top