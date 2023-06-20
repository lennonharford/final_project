import pygame
import config as conf
from groups import *
import pytmx
from tile import Tile

class Chunk(object):
    def __init__(self, filepath: str) -> None:
        data = pytmx.load_pygame(f"maps/{filepath}")
        
        ground_layer = data.get_layer_by_name("ground")
        wall_layer = data.get_layer_by_name("obstacles")
        
        self.ground = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
                
        for x, y, image in wall_layer.tiles():
            if image:
                self.walls.add(Tile(x, y, image))
                        
        for x, y, image in ground_layer.tiles():
            if image:
                self.ground.add(Tile(x, y, image))