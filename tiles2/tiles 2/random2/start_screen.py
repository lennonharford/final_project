import colors
import pygame, sys
from slots import Slots

pygame.init()

# Game Setup
font = pygame.font.Font('assets/fonts/font.ttf', 40)
font2 = pygame.font.Font('assets/fonts/font.ttf', 20)
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 798
WINDOW_HEIGHT = 462
exit_color=colors.RED1
startx=329
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("SHADOW OF WAR")
slots_obj = Slots(WINDOW_WIDTH, WINDOW_HEIGHT)


def display() -> None:
    global btn, start
    window.fill(colors.BLACK)
    start=window.blit(font.render("START", True, (colors.WHITE)), (startx, WINDOW_HEIGHT/2))
    btn=window.blit(font2.render("EXIT", True, (exit_color)), (730, 20))


while True:
    display()
    for event in pygame.event.get():
    # if user  QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if btn.collidepoint(pos):
                exit_color=colors.RED3
            else:
                exit_color=colors.WHITE 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if btn.collidepoint(pos):                
                        pygame.quit()
                        sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start.collidepoint(pos):
                startx=1000
                if startx==1000:
                    slots_obj.main()
            
            
            
    
       
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw