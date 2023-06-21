import pygame, sys
import colors
import config as conf

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

class WhateverScreenName(object):    
    def __init__(self): 
        self.font_size = 20 # to get larger font, do 2*font_size
        
        # reference position like this: 9/10ths of the width -> 9*(conf.window_width // 10)
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size, self.exit_color, "EXIT")
    
    def handle_event(self, event):
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            if self.btn_exit.collidepoint(pos):
                self.exit_color = colors.RED3
            else:
                self.exit_color = colors.WHITE 
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.btn_exit.collidepoint(pos):                
                pygame.quit()
                sys.exit()   
    
    def display(self, window: pygame.Surface) -> None:
        self.btn_exit.display(window)