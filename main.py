#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"

# By: Lennon, Sali
# Date: 2023-06-20
# Program Details: basic rpg with extensible maps

import pygame, sys
import config as conf
import colors
import sqlite3 as sql
from text import Text
from database import Database, Saves

class Main(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE)
        pygame.display.set_caption(conf.title)
        self.current_menu = Menu()
        self.fps = conf.fps
        self.database = Database("saves.db")
        self.saves = Saves(self.database)
            
    def run(self):
        running = True
        while running:
            keys = pygame.key.get_pressed()
            events = pygame.event.get()
            
            if keys[pygame.K_q]:
                self.exit()
            
            
            self.current_menu.display(self.window)
            
            for event in events:
                if event.type == pygame.QUIT:
                    self.exit()
                next_menu = self.current_menu.handle_event(event)
                
                if next_menu:
                    self.current_menu = next_menu
            
            pygame.display.update()
            self.clock.tick(self.fps)
            
    def exit(self) -> None:
        self.saves.close()
        pygame.mixer.stop()
        pygame.quit()
        sys.exit()
          
class Game(Main):
    def __init__(self, slot, username, playertype) -> None:
        super().__init__()
        self.slot = slot
        self.username = username
        self.playertype = playertype

        self.saves.save(self.slot, self.username, self.playertype)
        # self.player = pygame.sprite.GroupSingle(Player(self.slot, self.username, self.playertype))
    
    def display(self, window):
        window.fill(colors.BLACK)
    
    def handle_event(self, event):
        pass
    
    # def _update_chunks(self) -> None:   
    #     # if player.sprite.rect.x < 0:
    #     #     map_x -= 1
    #     #     player.sprite.rect.x = conf.window_width - conf.tile_size
            
    #     #     player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
    #     #     player.sprite.moving = False 
    #     #     player.sprite.counter = 0 
    #     # elif player.sprite.rect.x > conf.window_width - conf.tile_size: 
    #     #     map_x += 1
    #     #     player.sprite.rect.x = 0
            
    #     #     player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
    #     #     player.sprite.moving = False 
    #     #     player.sprite.counter = 0 
    #     # elif player.sprite.rect.y < 0:
    #     #     map_y -= 1
    #     #     player.sprite.rect.y = conf.window_height - conf.tile_size
            
    #     #     player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
    #     #     player.sprite.moving = False 
    #     #     player.sprite.counter = 0 
    #     # elif player.sprite.rect.y > conf.window_height - conf.tile_size: 
    #     #     map_y += 1
    #     #     player.sprite.rect.y = 0
            
    #     #     player.sprite.destination = player.sprite.rect.x, player.sprite.rect.y
    #     #     player.sprite.moving = False
    #     #     player.sprite.counter = 0 
    #     # chunk = map[map_x][map_y]
    #     pass      
        
class Menu(object):
    def __init__(self):
        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.title = Text((conf.window_width // 2, 1*(conf.window_height // 8)), self.font_size*3, self.exit_color, "THE SHADOWS OF WAR")
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.exit_color, "EXIT")
        self.btn_start = Text((conf.window_width // 2, 3*(conf.window_height // 8)), self.font_size*3, self.text_color, "START")
        self.btn_settings = Text((conf.window_width // 2, 5*(conf.window_height // 8)),  self.font_size*3, self.text_color, "SETTINGS")
        self.btn_tutorial = Text((conf.window_width // 2, 7*(conf.window_height // 8)), self.font_size*3, self.text_color, "HOW TO PLAY")

    def handle_event(self, event):
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEMOTION:
            
            if self.btn_exit.collides(pos):
                self.btn_exit.color = self.exit_color
            else:
                self.btn_exit.color = self.text_color
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if self.btn_exit.collides(pos):
                pygame.quit()
                sys.exit()
            elif self.btn_start.collides(pos):
                return Slots()
            elif self.btn_settings.collides(pos):
                print("GOTO settings")
            elif self.btn_tutorial.collides(pos):
                print("GOTO tutorial")

    def display(self, window) -> None:
        window.fill(colors.BLACK)

        self.title.display(window) 
        self.btn_exit.display(window)
        self.btn_start.display(window)
        self.btn_settings.display(window) 
        self.btn_tutorial.display(window) 
        
class Player_Choice(object):
    def __init__(self, slot, username):
        self.slot = slot
        self.username = username
        
        self.images = [
            pygame.transform.scale(pygame.image.load('assets/images/player1.png'), (conf.window_width // 6, conf.window_width // 6)),
            pygame.transform.scale(pygame.image.load('assets/images/player2.png'), (conf.window_width // 6, conf.window_width // 6))
        ]
        
        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size, self.exit_color, "EXIT")
        self.btn_back = Text((1*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size, self.text_color, "BACK")
        
        self.choose_character = Text((conf.window_width // 2, 1*(conf.window_height // 8)), 2*self.font_size, self.text_color, "CHOOSE A CHARACTER:")

        
    def display(self, window) -> None:
        window.fill(colors.BLACK)
        
        
        self.btn_back.display(window)
        self.btn_exit.display(window)
        self.choose_character.display(window)
        
        self.players = [
            window.blit(self.images[0], (1*(conf.window_width // 6), 3*(conf.window_height // 8))),
            window.blit(self.images[1], (4*(conf.window_width // 6), 3*(conf.window_height // 8)))
        ]
                
    def handle_event(self, event):
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:  
                      
            if self.btn_exit.collides(pos):
                self.btn_exit.color = self.exit_color
            else:
                self.btn_exit.color = self.text_color
                
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if self.btn_exit.collides(pos):                
                pygame.quit()
                sys.exit()
            
            if self.btn_back.collides(pos):
                return Input(self.slot)
                
            for i, player in enumerate(self.players):
                if player.collidepoint(pos):
                    return Game(self.slot, self.username, i)
                
class Input(object):
    def __init__(self, slot):
        self.slot = slot
        
        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.input_box = pygame.Rect(1*(conf.window_width // 4), conf.window_height // 2, conf.window_width // 2, 1*(conf.window_height // 8))
        
        self.exit_color = colors.RED1
        self.color_inactive = colors.WHITE
        self.color_active = colors.RASPBERRY
        self.color = self.color_inactive
        self.active = False
        self.done = False
        self.text = ""
        
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.exit_color, "EXIT")
        self.btn_back = Text((1*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.text_color, "BACK")
        self.enter_name = Text((conf.window_width // 2, 2*(conf.window_height // 8)), self.font_size*3, self.text_color, "ENTER CHARACTER NAME:")

        
    def display(self, window):
        window.fill(colors.BLACK)

        self.enter_name.display(window)
        self.btn_exit.display(window)
        self.btn_back.display(window)
        
        window.blit(pygame.font.Font("fonts/font.ttf", self.font_size*2).render(self.text, True, self.color), (self.input_box.x+(conf.window_width // 50), self.input_box.y+(conf.window_width // 50)))

        pygame.draw.rect(window, self.color, self.input_box, (conf.window_width // 250))

    def handle_event(self, event):
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            
            if self.btn_exit.collides(pos):
                self.btn_exit.color = self.exit_color 
            else:
                self.btn_exit.color = self.text_color 

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if self.btn_exit.collides(pos):                
                pygame.quit()
                sys.exit()   
            
            if self.btn_back.collides(pos):
                return Slots()
            # If the user clicked on the input_box rect.        
            if self.input_box.collidepoint(pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
                
            # Change the current color of the input box.
            if self.active:
                self.color = self.color_active
            else:
                self.color = self.color_inactive
                
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return Player_Choice(self.slot, self.text)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if pygame.font.Font("fonts/font.ttf", self.font_size*2).size(self.text + event.unicode)[0] < self.input_box.width - (conf.window_width // 50):
                        self.text += event.unicode

class Slots(Main):    
    def __init__(self): 
        super().__init__() 
                
        self.slot_width = conf.window_width // 4
        self.slot_gap = (conf.window_width - 3*self.slot_width) // 4
        self.slot_height = conf.window_height // 2

        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.btns_clear = [None, None, None]
        self.save_list = self.saves.load_all()

        self.images = [
            pygame.image.load('assets/images/player1.png'),
            pygame.image.load('assets/images/player2.png')
        ]
        
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.exit_color, "EXIT")
        self.btn_back = Text((1*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.text_color, "BACK")
        self.choose_slot = Text((conf.window_width // 2, 1*(conf.window_height // 8)), self.font_size*3, self.text_color, "CHOOSE A SLOT:")
    
    def handle_event(self, event):
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:
            
            if self.btn_exit.collides(pos):
                self.btn_exit.color = self.exit_color 
            else:
                self.btn_exit.color = self.text_color 

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            if self.btn_exit.collides(pos):                
                pygame.quit()
                sys.exit()   
            
            if self.btn_back.collides(pos):
                return Menu()
            
            for i, btn in enumerate(self.btns_clear):
                if btn is not None:
                    if btn.collides(pos):
                        self.saves.delete(i)
                        self.save_list = self.saves.load_all()
                        
            for slot_index, slot in enumerate(self.slots):
                if slot.collidepoint(pos):
                    save = self.saves.load(slot_index)
                    
                    if save:
                        username, playertype = save
                        return Game(slot_index, username, playertype)
                    else:
                        return Input(slot_index)
    
    def display(self, window: pygame.Surface) -> None:
        window.fill(colors.BLACK)
        
        self.btn_exit.display(window)
        self.btn_back.display(window)
        self.choose_slot.display(window)
        
        self.slots = [
            pygame.draw.rect(window, colors.GRAY10, (self.slot_gap, (conf.window_height - self.slot_height) // 2, self.slot_width, self.slot_height)),
            pygame.draw.rect(window, colors.GRAY10, (2*self.slot_gap+self.slot_width, (conf.window_height - self.slot_height) // 2, self.slot_width, self.slot_height)),
            pygame.draw.rect(window, colors.GRAY10, (3*self.slot_gap+2*self.slot_width, (conf.window_height - self.slot_height) // 2, self.slot_width, self.slot_height))
        ]
        
        saves_used = [None, None, None]
        
        for i, save in enumerate(self.save_list):
            save_index, username, playertype = save
            saves_used[save_index] = save_index
        
        for i, rect in enumerate(self.slots):
            if saves_used[i] is not None:
                username, playertype = self.saves.load(i)
                
                image = pygame.transform.scale(self.images[playertype], (rect.width, rect.width))
                username_text = Text((rect.centerx, rect.bottom + 1*(conf.window_height // 10)), self.font_size*2, self.text_color, username)
                clear_text = Text((rect.centerx, rect.bottom + 2*(conf.window_height // 10)), self.font_size*2, self.text_color, "CLEAR")
                
                window.blit(image, (rect.x, rect.y))
                username_text.display(window)
                clear_text.display(window)
                self.btns_clear[i] = clear_text
            else:
                slot_text = Text((rect.centerx, rect.bottom + 1*(conf.window_height // 10)), self.font_size*2, self.text_color, f"SLOT {i+1}")
                slot_text.display(window)
     

if __name__ == "__main__":
    pygame.init()
    main = Main()
    main.run()


	# Click on empty box
	# Put in information
	# information for slot1 is uploaded to database
	# close program

	# open again, pull data from database and make slot1 full of player info
	# when slot clicked, load game directly with playerdata