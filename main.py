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

def game() -> None:
    global chunk    
    chunk.ground.draw(window)
    chunk.walls.draw(window)
        
    player.update()    
    player.draw(window)
    update_chunks()
    player.sprite.chunk = chunk
    
def update_chunks():
    global map_x, map_y, chunk
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
        
        if conf.tick == 60:
            conf.tick = 0
        else:
            conf.tick += 1

def exit() -> None:
    mixer.stop()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
    clock = time.Clock()
    window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE)
    
    map = [
        [Chunk("map1.tmx"), Chunk("map2.tmx")],
        [Chunk("map3.tmx"), Chunk("map4.tmx")]
    ]
    map_x, map_y = 0, 0
    chunk = map[map_x][map_y]

    player.add(Player(0, 0, conf.chunk, 1))
    
    main()


