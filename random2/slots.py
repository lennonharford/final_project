import pygame,sys
import colors
from input import Input

class Slots(object):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):  
        self.window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
        self.font = pygame.font.Font('assets/fonts/font.ttf', 40)
        self.font2 = pygame.font.Font('assets/fonts/font.ttf', 20)
        self.font3 = pygame.font.Font('assets/fonts/font.ttf', 28)
        self.clock = pygame.time.Clock()
        self.exit_color=colors.RED1
        self.choose = False
        self.clock = pygame.time.Clock()
        self.input_obj = Input(WINDOW_WIDTH, WINDOW_HEIGHT)


    
    def display(self) -> None:
        self.window.fill(colors.BLACK)
        self.window.blit(self.font.render("CHOOSE A SLOT:", True, (colors.WHITE)), (30, 60))
        self.btn=self.window.blit(self.font2.render("EXIT", True, (self.exit_color)), (730, 20))
        self.slot1=pygame.draw.rect(self.window,(colors.GRAY10),(40,130,200,300))
        self.slot2=pygame.draw.rect(self.window,(colors.GRAY10),(300,130,200,300))
        self.slot3=pygame.draw.rect(self.window,(colors.GRAY10),(560,130,200,300))
        self.slot1_text=self.window.blit(self.font3.render("SLOT ONE", True, (colors.WHITE)), (40, 260))
        self.slot2_text=self.window.blit(self.font3.render("SLOT TWO", True, (colors.WHITE)), (300, 260))
        self.slot3_text=self.window.blit(self.font3.render("SLOT THREE", True, (colors.WHITE)), (560, 260))


    def main(self) -> None:
        while True:
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
                    if self.btn.collidepoint(self.pos):                
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.pos = pygame.mouse.get_pos()
                    if self.slot1.collidepoint(self.pos):
                        print("1") 
                        self.choosen=True
                    elif self.slot2.collidepoint(self.pos):
                        print("2") 
                        self.choose=True
                    elif self.slot3.collidepoint(self.pos):
                        print("3") 
                        self.choose=True
                    
            if self.choose==True:
                self.window.fill(colors.BLACK)
                self.input_obj.main()
                
            pygame.display.flip()
            
            
            