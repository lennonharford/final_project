import pygame
import config as conf
from groups import *
import pytmx
from mapchunk import Chunk

class Npc(pygame.sprite.Sprite):
    
    def __init__(self, x: int, y: int, chunk: Chunk, image_path: str) -> None:
        super().__init__()
        
        self.image_path = image_path
        self.chunk = chunk
        self.direction = pygame.K_s  
        self.animation_state = 0  
        self.image = pygame.transform.scale(pygame.image.load(self.image_path), conf.tile_dimensions).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x*conf.tile_size, y*conf.tile_size)) 