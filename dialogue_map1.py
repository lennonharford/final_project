import pygame
import sys
import colors

class Dialogue(object):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.HWSURFACE)
        self.font_size = 20
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('assets/fonts/font.ttf', 12)

        self.exit_color = colors.RED1
        self.player_name = "bob"
        self.dialogue_box_rect = pygame.Rect(0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 100)

        self.dialogue_texts = [
            "CHINO: HELLO THERE, CAN I HELP YOU WITH SOMETHING?",
            f"{self.player_name}: YES, I'M LOOKING FOR RUST BOWL!",
            "CHINO: RUST BOWL? SURE, IT'S LOCATED IN THE NORTHERN PART OF THE CITY.",
            f"{self.player_name}: THANK YOU!",
            "CHINO: YOU'RE WELCOME! HAVE A GREAT DAY!"
        ]
        self.dialogue_index = 0  # initialize the index to 0
        self.show_press_n_text = True  # Flag to show the "Press 'N' to continue" text
        self.selected_option_text = ""  # Selected option text
        self.option_y = self.dialogue_box_rect.bottom - 60

    def display(self) -> None:
        pygame.draw.rect(self.window, colors.BLACK, self.dialogue_box_rect)

        while True:
            dialogue_text_surface = pygame.font.Font('assets/fonts/font.ttf', self.font_size).render(
                self.dialogue_texts[self.dialogue_index], True, colors.WHITE)
            dialogue_text_rect = dialogue_text_surface.get_rect()
            if dialogue_text_rect.width < self.dialogue_box_rect.width - 20 and dialogue_text_rect.height < self.dialogue_box_rect.height - 20:
                break
            self.font_size -= 1

        dialogue_text_rect.center = self.dialogue_box_rect.center
        self.window.blit(dialogue_text_surface, dialogue_text_rect)

        if self.show_press_n_text:
            self.small_text_surface = self.font.render("PRESS 'N' TO CONTINUE..", True, colors.WHITE)
            self.small_text_rect = self.small_text_surface.get_rect()
            self.small_text_rect.bottomright = (self.dialogue_box_rect.right - 10, self.dialogue_box_rect.bottom - 10)
            self.window.blit(self.small_text_surface, self.small_text_rect)

    def main(self) -> None:
        running = True
        while running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                exit() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n and self.show_press_n_text:
                        if self.dialogue_index < len(self.dialogue_texts) - 1:
                            self.dialogue_index += 1  # Increment the dialogue index
                        else:
                            running=False
                
            self.display()
            pygame.display.update()
            self.clock.tick(60)

