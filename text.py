__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"


import pygame, sys

class Text:
    def __init__(self, position: tuple, size: int, color, text: str=""):
        self.x, self.y = position
        self.size = size
        self.color = color
        self.font = pygame.font.Font("fonts/font.ttf", size)
        self.surface = None
        self.rect = None
        self.set_text(text)

    def set_text(self, text: str):
        self.text = text
        self.surface = self.font.render(text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.x, self.y))

    def display(self, window):
        window.blit(self.surface, self.rect)

    def collides(self, point: tuple) -> bool:
        return self.rect.collidepoint(point)