import pygame,sys
import colors


class Player_Choice(object):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
        img1 = pygame.image.load('assets/images/player1.png') #with .png or .jpb included in the name
        self.img1 = pygame.transform.scale(img1, (200, 200))  #resize image Where 35 ,35 is the size, (x,y)
        img2 = pygame.image.load('assets/images/player2.png') #with .png or .jpb included in the name
        self.img2 = pygame.transform.scale(img2, (200, 200))  #resize image Where 35 ,35 is the size, (x,y)
        self.font = pygame.font.Font('assets/fonts/font.ttf', 40)
        self.font2 = pygame.font.Font('assets/fonts/font.ttf', 20)
        self.exit_color=colors.RED1
        self.choosen = False

        
    def display(self) -> None:
        self.player1=self.window.blit(self.img1,(150, 191))
        self.player2=self.window.blit(self.img2,(450, 191))
        self.btn=self.window.blit(self.font2.render("EXIT", True, (self.exit_color)), (730, 20))
        self.window.blit(self.font.render("CHOOSE A CHARACTER:", True, (colors.WHITE)), (30, 60))


    def main(self) -> None:
        while not self.choosen:
            self.display()
            for event in pygame.event.get():
            # if user  QUIT then the screen will close
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    self.pos = pygame.mouse.get_pos()
                    if self.btn.collidepoint(self.pos):
                        self.exit_color=colors.RED3
                    else:
                        self.exit_color=colors.WHITE 
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.pos = pygame.mouse.get_pos()
                            if self.btn.collidepoint(self.pos):                
                                pygame.quit()
                                sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.pos = pygame.mouse.get_pos()
                    if self.player1.collidepoint(self.pos):
                        print("1") 
                        self.choosen=True
                    if self.player2.collidepoint(self.pos):
                        print("2") 
                        self.choose=True
 
                        
            pygame.display.flip()
           