import pygame, sys
import config as conf
import colors
import sqlite3 as sql
from text import Text
from database import Database, Saves
import pytmx
from tiles import Tile, Chunk
from player import Player
from math import dist

class Npc(pygame.sprite.Sprite):
    def __init__(self, chunk_x, chunk_y, world_x, world_y, imagepath) -> None:
        super().__init__()
        self.world_x = world_x
        self.world_y = world_y
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self.image = pygame.transform.scale(pygame.image.load(imagepath), conf.tile_dimensions).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(chunk_x*conf.tile_size, chunk_y*conf.tile_size))
        
    def update(self):
        pass
    
    def player_close(self, player, world_pos):
        if dist((player.sprite.rect.x, player.sprite.rect.y), (self.rect.x, self.rect.y)) == conf.tile_size and (self.world_x, self.world_y) == world_pos:
            return True
        else:
            return False