# By: Lennon, Sali
# Date: 5/29/2023
# Program Details:

# imports
import pygame
from pygame import sprite, display, mixer, time
import sys
import colors
import config as conf
from random import choice, choices
# from pygame.math import Vector2 as Vector
import sqlite3 as sql
from tile import Tile
from vector import Vector



# 16*9\

# returns true if the anything in the group has reached the left or right margin
def reached_margin(group: sprite.Group | sprite.GroupSingle) -> bool:
    if type(group) == sprite.Group:
        for item in group.sprites():
            if item.rect.left == conf.margin_left or item.rect.right == conf.margin_right:
                return True
        return False
    elif type(group) == sprite.GroupSingle:
        return group.sprite.rect.left == conf.margin_left or group.sprite.rect.right == conf.margin_right

# updates the main clock which everything is based on      
def update_tick() -> None:
    if conf.tick == 60:
        conf.tick = 0
    else:
        conf.tick += 1
        
# the main function of this program
def main() -> None:
    # setting and resetting values
    display.set_caption(conf.title)
        
    # main game loop
    while True:
        
        window.fill(colors.BLACK)
        
        
        
        #if conf.gamestate == conf.gamestates[0]:
        #    menu()
        #elif conf.gamestate == conf.gamestates[1]:
        #    game()
        #else:
        #    exit()
                
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # updates the display and advances the clock
        pygame.display.update()
        clock.tick(conf.fps)
        update_tick()
        
def menu() -> None:
    window.fill(colors.BLACK)

def game() -> None:
    pass
    
def exit() -> None:
    # runs when the game is closed
    mixer.stop()
    pygame.quit()
    sys.exit()
    
def populate_chunk() -> None:
    pass


def get_image(x: int, y: int, size: int, path: str) -> pygame.Surface:
    try:
        sheet = pygame.image.load(path).convert()
    except pygame.error as e:
        raise SystemExit(e)
    
    rect = pygame.Rect(x, y, x+size, y+size)
    image = pygame.Surface(rect.size).convert_alpha()
    image.blit(sheet, (0, 0), rect)

    return image

def populate_tiles():
    tiles = []
    chunk = conf.chunk_dimensions
    
    for width in range(chunk.x):
        for height in range(chunk.y):
            tiles[width][height] = f"x: {width}, y: {height}"
        
    return tiles
        
        

if __name__ == "__main__":
    pygame.init()
    
    clock = time.Clock()
    window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE | pygame.SCALED | pygame.RESIZABLE)
    #tiles = []
    # tiles = [
    #     [00, 01, 02],
    #     [10, 11, 12],
    #     [20, 21, 22]
    # ]
    
    # tile[0][2]
    # tile[2][2]
    main()