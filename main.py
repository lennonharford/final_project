#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"

import pygame, sys
from pygame import sprite, display, mixer, time
import config as conf
import pytmx
from tile import Tile
from player import Player
from groups import *
import sqlite3 as sql
from mapchunk import Chunk


def game() -> None:
    global chunk, map_x, map_y, map    
    chunk.ground.draw(window)
    chunk.walls.draw(window)
        
    player.update()    
    player.draw(window)
    update_chunks()
    player.sprite.chunk = chunk
    
def update_chunks():
    global map_x, map_y, chunk, map
    if player.sprite.rect.x < 0:
        map_x -= 1
        player.sprite.rect.x = conf.window_width - conf.tile_size
        
        player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
        player.sprite.moving = False 
        player.sprite.counter = 0 
        
    elif player.sprite.rect.x > conf.window_width - conf.tile_size: 
        map_x += 1
        player.sprite.rect.x = 0
        
        player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
        player.sprite.moving = False 
        player.sprite.counter = 0 
    elif player.sprite.rect.y < 0:
        map_y -= 1
        player.sprite.rect.y = conf.window_height - conf.tile_size
        
        player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
        player.sprite.moving = False 
        player.sprite.counter = 0 
        
    elif player.sprite.rect.y > conf.window_height - conf.tile_size: 
        map_y += 1
        player.sprite.rect.y = 0
        
        player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
        player.sprite.moving = False
        player.sprite.counter = 0 
    chunk = map[map_x][map_y]
    
def main() -> None:
    display.set_caption(conf.title)
        
    while True:
        
        game()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        pygame.display.update()
        clock.tick(conf.fps)

def exit() -> None:
    mixer.stop()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
    clock = time.Clock()
    window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE)
    pygame.display.set_caption(conf.title)
    
    map = [
        [Chunk("map00.tmx"), Chunk("map01.tmx"), Chunk("map02.tmx")],
        [Chunk("map10.tmx"), Chunk("map11.tmx"), Chunk("map12.tmx")],
    ]
    map_x, map_y = 0, 2
    x, y = 3, 3
    player_type = 1
    chunk = map[map_x][map_y]
    
    player.add(Player(x, y, chunk, player_type))
    main()




