# By: Lennon Harford
# Date: 2023-05-05
# Program Details:  The player controls a turret which shoots at aliens. 
#                   If he or the aliens hit the bunkers, they lose health, and eventually break down. 
#                   The player needs to shoot all of the aliens before they shoot him or reach earth

# imports
import pygame
from pygame import sprite, display, mixer, time
import sys
import colors
import config
from random import choice


# returns true if the anything in the group has reached the left or right margin
def reached_margin(group: sprite.Group | sprite.GroupSingle) -> bool:
    if type(group) == sprite.Group:
        for item in group.sprites():
            if item.rect.left == config.margin_left or item.rect.right == config.margin_right:
                return True
        return False
    elif type(group) == sprite.GroupSingle:
        return group.sprite.rect.left == config.margin_left or group.sprite.rect.right == config.margin_right

# updates the main clock which everything is based on      
def update_tick() -> None:
    if tick == 60:
        tick: int = 0
    else:
        tick += 1
        
# the main function of this program
def main() -> None:
    # setting and resetting values
    display.set_caption(config.title)

    won: bool | None = None
    
    # main game loop
    while True:
        window.fill(colors.BLACK)
                
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # updates the display and advances the clock
        pygame.display.update()
        clock.tick(config.fps)
        update_tick()
    
    # secondary game loop for winning/losing screen
    while True:
        # clears the window
        window.fill(colors.BLACK)    
        
        # draws the you lose or you win
        if won:
            you_won_btn.draw(window)
        else:
            game_over_btn.draw(window)
            
        # draws the restart button
        restart_btn.draw(window)
        
        # exits the loop if the button is clicked
        if restart_btn.sprite.clicked():
            break
            
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # updates the display and advances the clock
        display.update()
        clock.tick(config.fps)
        
    # recurses back to the main function if restart has been clicked
    main()
    
def exit() -> None:
    # runs when the game is closed
    mixer.stop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()
    
    clock = time.Clock()
    window = display.set_mode(config.window_dimensions, pygame.HWSURFACE)
    tick: int = 0
    gamestates: tuple[str, ...] = 'start', 'main', 'end'
    
    main()