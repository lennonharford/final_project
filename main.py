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
from pygame.math import Vector2 as Vector

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
        
        if conf.gamestate == conf.gamestates[0]:
            menu()
        elif conf.gamestate == conf.gamestates[1]:
            game()
        else:
            exit()
                
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

if __name__ == "__main__":
    pygame.init()
    
    clock = time.Clock()
    window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE | pygame.SCALED | pygame.RESIZABLE)
        
    main()