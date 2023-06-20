#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"

# By: Lennon, Sali
# Date: 2023-06-20
# Program Details: basic rpg with extensible maps

import pygame, sys
from pygame import sprite, display, mixer, time
import config as conf
import pytmx
from tile import Tile
from player import Player
from groups import *
import sqlite3 as sql
from mapchunk import Chunk
import dialogue_map1 as d1
from database import Database, Table

def game() -> None:
    # draws and updates the sprites
    global chunk, map_x, map_y, map    
    chunk.ground.draw(window)
    chunk.walls.draw(window)
        
    player.update()    
    player.draw(window)
    update_chunks()
    player.sprite.chunk = chunk
    
def update_chunks() -> None:
    # responsible for loading new chunks when the player leaves one
    global map_x, map_y, chunk, map
    
    
    # if the player went to the left then decrease the x index of the map 2D list, 
    # and make the players position to be at the right of the screen
    if player.sprite.rect.x < 0:
        map_x -= 1
        player.sprite.rect.x = conf.window_width - conf.tile_size
        
        player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
        player.sprite.moving = False 
        player.sprite.counter = 0 
        
    # if the player went to the right then increase the x index of the map 2D list, 
    # and make the players position to be at the left of the screen
    elif player.sprite.rect.x > conf.window_width - conf.tile_size: 
        map_x += 1
        player.sprite.rect.x = 0
        
        player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
        player.sprite.moving = False 
        player.sprite.counter = 0 
        
    # if the player went up then decrease the y index of the map 2D list, 
    # and make the players position to be at the top of the screen
    elif player.sprite.rect.y < 0:
        map_y -= 1
        player.sprite.rect.y = conf.window_height - conf.tile_size
        
        player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
        player.sprite.moving = False 
        player.sprite.counter = 0 
    
    # if the player went down then increase the y index of the map 2D list, 
    # and make the players position to be at the bottom of the screen
    elif player.sprite.rect.y > conf.window_height - conf.tile_size: 
        map_y += 1
        player.sprite.rect.y = 0
        
        player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
        player.sprite.moving = False
        player.sprite.counter = 0 
    chunk = map[map_x][map_y]
    
def main() -> None:
    display.set_caption(conf.title)
    
    # event loop        
    while True:
        
        # responsible for displaying and updating the sprites
        game()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            exit()

        if player.sprite.chunk == map[0][1] and (player.sprite.rect.x // conf.tile_size, player.sprite.rect.y // conf.tile_size) == (12, 5):
            dialog.main()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()
        clock.tick(conf.fps)
        
def save():
    saves.insert(("x", "y", "map_x", "map_y", "player_type"),(x, y, map_x, map_y, player_type))

def exit() -> None:
    mixer.stop()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init()
    clock = time.Clock()
    window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE)
    pygame.display.set_caption(conf.title)
    
    database = Database("save.db")
    
    saves = Table(
        database,
        "x INTEGER",
        "y INTEGER",
        "map_x INTEGER",
        "map_y INTEGER",
        "player_type INTEGER"
    )
    
    # 2D map to represent the chunks
    map = [
        [Chunk("map00.tmx"), Chunk("map01.tmx"), Chunk("map02.tmx")],
        [Chunk("map10.tmx"), Chunk("map11.tmx"), Chunk("map12.tmx")],
    ]
    
    # values to store currently loaded chunk
    map_x, map_y = 0, 2
    
    # values to store x and y position within loaded chunk
    x, y = 3, 3
    
    # either 1 or 2, changes the sprite images
    player_type = 1
    
    # declaring the current chunk
    chunk = map[map_x][map_y]
    
    # adds Player sprite to the player group single
    player.add(Player(x, y, chunk, player_type))
    
    dialog = d1.Dialogue(*conf.window_dimensions)
    
    main()




