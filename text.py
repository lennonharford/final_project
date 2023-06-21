__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"


import pygame, sys

class Text(object):
    def __init__(self, position: tuple, size: int, color: pygame.color.Color, text: str=""):
        self.x, self.y = position
        self.size = size
        self.color = color
        self.font = pygame.font.Font("fonts/font.ttf", size)
        self.surface = None
        self.rect = None
        self.set_text(text)

    def set_text(self, text: str) -> None:
        self.text = text
        self.surface = self.font.render(text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.x, self.y))

    def display(self, window: pygame.surface.Surface) -> None:
        window.blit(self.surface, self.rect)

    def collides(self, point: tuple[int, int]) -> bool:
        return self.rect.collidepoint(point)