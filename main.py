import pygame, sys
from pygame import sprite, display, mixer, time
import config as conf
from random import choice, choices
from pytmx.util_pygame import load_pygame
from tile import Tile
        
def game() -> None:
    pass
        
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
    window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE | pygame.SCALED | pygame.RESIZABLE)
    map = load_pygame("map.tmx")
    
    
    #print(dir(map))
    
    
    # #print(dir(tile_data))
    # print(tmx.layers)
    #  = tmx.get_layer_by_name("Floor")
    # #walls = tmx.get_layer_by_name("Walls")
    # #player = tmx.get_layer_by_name("Player")
    # tiles = list(floor.tiles())
    
    # pygame_surface = tile_map.get_tile_image(x, y, layer)
    
    # # for x, y, surface in floor.tiles():
    # #     floor_tiles.append((x,y,surface))
    
    # # for tile in floor_tiles:
    # #     print(tile)

    main()