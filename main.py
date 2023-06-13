import pygame, sys
from pygame import sprite, display, mixer, time
import config as conf
from random import choice, choices
from pytmx.util_pygame import load_pygame
from tile import Tile
        
def game() -> None:
    for x, y, surface in ground.tiles():
        window.blit(surface, (x*conf.tile_size,y*conf.tile_size))
    
    for x, y, surface in walls.tiles():
        window.blit(surface, (x*conf.tile_size,y*conf.tile_size))        

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
    path = "c:/Harford/tiled_project/map_003.tmx"
    clock = time.Clock()
    window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE | pygame.SCALED | pygame.RESIZABLE)
    map = load_pygame(path)
    layers = map.layers
    ground = map.get_layer_by_name("ground")
    walls = map.get_layer_by_name("walls")
    
    print("{} {} {}".format(layers, ground, walls))
    main()