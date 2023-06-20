import pygame,sys
import colors
from player_choice import Player_Choice


class Input(object):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):  
        self.window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE)
        self.font = pygame.font.Font('assets/fonts/font.ttf', 40)
        self.font2 = pygame.font.Font('assets/fonts/font.ttf', 20)
        self.clock = pygame.time.Clock()
        self.input_box = pygame.Rect(139, 251, 500, 55)
        self.color_inactive = colors.WHITE
        self.color_active = colors.RASPBERRY
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.done = False
        self.exit_color=colors.RED1
        self.p_choice = Player_Choice(WINDOW_WIDTH, WINDOW_HEIGHT)


    def main(self) -> None:
        while not self.done:
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if self.input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        self.active = not self.active
                    else:
                        self.active = False
                    # Change the current color of the input box.
                    self.color = self.color_active if self.active else self.color_inactive
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            print(self.text)
                            self.text = ''
                            #self.window.fill(colors.BLACK)
                            self.done=True
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            if self.font.size(self.text + event.unicode)[0] < self.input_box.width - 10:
                                self.text += event.unicode

            self.window.fill(colors.BLACK)
            # Render the current text.
            txt_surface = self.font.render(self.text, True, self.color)
            # Blit the text.
            self.window.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
            self.window.blit(self.font.render("ENTER CHARACTER NAME:", True, (colors.WHITE)), (89, 191))
            self.btn=self.window.blit(self.font2.render("EXIT", True, (self.exit_color)), (730, 20))

            # Blit the input_box rect.
            pygame.draw.rect(self.window, self.color, self.input_box, 2)

            pygame.display.flip()
            self.clock.tick(30)

            if self.done == True:
                self.window.fill(colors.BLACK)
                self.p_choice.main()
