# By: Lennon Harford
# Date: 2023-05-05
# Program Details: class for the button object

import pygame
import sys

class Button(pygame.sprite.Sprite):
    def __init__(self, centerx: int, y: int, size_x: int, size_y: int, image_path: str) -> None:
        super().__init__()
        # defines class variables
        self.image = pygame.transform.scale(pygame.image.load(image_path), (size_x, size_y)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.y = y
        
    def clicked(self) -> bool:
        x, y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and self.rect.collidepoint((x, y)):
            return True
        return False