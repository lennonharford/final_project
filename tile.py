import pygame
import config as conf

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (conf.tile_size, conf.tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = self.x * conf.tile_size
        self.rect.y = self.y * conf.tile_size