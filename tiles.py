__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"


import pygame
import config as conf
import pytmx

class Tile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, image: pygame.surface.Surface) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (conf.tile_size, conf.tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x * conf.tile_size
        self.rect.y = self.y * conf.tile_size
        
class Chunk(object):
    def __init__(self, filepath: str) -> None:
        data = pytmx.load_pygame(f"maps/{filepath}")
        
        ground_layer = data.get_layer_by_name("ground")
        wall_layer = data.get_layer_by_name("walls")
        
        self.ground = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
                
        for x, y, image in wall_layer.tiles():
            if image:
                self.walls.add(Tile(x, y, image))
                        
        for x, y, image in ground_layer.tiles():
            if image:
                self.ground.add(Tile(x, y, image))