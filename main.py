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
import pytmx
from tiles import Tile, Chunk
from player import Player

class Main(object):
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(conf.window_dimensions, pygame.HWSURFACE)
        pygame.display.set_caption(conf.title)
        self.current_menu = Menu()
        self.fps = conf.fps
        self.database = Database("saves.db")
        self.saves = Saves(self.database)
                
    def run(self) -> None:
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
                
                if next_menu is not None:
                    self.current_menu = next_menu
            
            pygame.display.update()
            self.clock.tick(self.fps)
            
    def exit(self) -> None:
        self.saves.close()
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()
        
class Game(Main):
    def __init__(self, slot, username, playertype, chunk_x, chunk_y, world_x, world_y) -> None:
        super().__init__()
            
        self.slot = slot
        self.username = username 
        self.playertype = playertype
        self.chunk_x = chunk_x
        self.chunk_y = chunk_y
        self.world_x = world_x
        self.world_y = world_y

        self.saves.save(self.slot, self.username, self.playertype, (self.chunk_x, self.chunk_y), (self.world_x, self.world_y))
        self.world_map = [
            ["map00.tmx", "map01.tmx", "map02.tmx"],
            ["map10.tmx", "map11.tmx", "map12.tmx"]
        ]
        self.chunk = Chunk(self.world_map[self.world_x][self.world_y])

        self.player = pygame.sprite.GroupSingle(Player(self.chunk_x, self.chunk_y, self.chunk, self.playertype))
    
    def display(self, window: pygame.surface.Surface) -> None:
        window.fill(colors.BLACK)
        
        self.player.update()
        
        self.chunk.ground.draw(window)
        self.chunk.walls.draw(window)
            
        self.player.draw(window)
        self.player.update()    
        
        self._update_chunks()
        self.player.sprite.chunk = self.chunk
    
    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return GameOver()

    def _update_chunks(self) -> None:
        # responsible for loading new chunks when the player leaves one
                
        # if the player went to the left then decrease the x index of the map 2D list, 
        # and make the players position to be at the right of the screen
        if self.player.sprite.rect.x < 0:
            self.world_x -= 1
            self.player.sprite.rect.x = conf.window_width - conf.tile_size
            
            self.player.sprite.destination = self.player.sprite.rect.x, self.player.sprite.rect.y
            self.player.sprite.moving = False 
            self.player.sprite.counter = 0 
        
        # if the player went to the right then increase the x index of the map 2D list, 
        # and make the players position to be at the left of the screen
        elif self.player.sprite.rect.x > conf.window_width - conf.tile_size: 
            self.world_x += 1
            self.player.sprite.rect.x = 0
            
            self.player.sprite.destination = self.player.sprite.rect.x, self.player.sprite.rect.y
            self.player.sprite.moving = False 
            self.player.sprite.counter = 0 
        
        # if the player went up then decrease the y index of the map 2D list, 
        # and make the players position to be at the top of the screen
        elif self.player.sprite.rect.y < 0:
            self.world_y -= 1
            self.player.sprite.rect.y = conf.window_height - conf.tile_size
            
            self.player.sprite.destination = self.player.sprite.rect.x, self.player.sprite.rect.y
            self.player.sprite.moving = False 
            self.player.sprite.counter = 0 
        
        # if the player went down then increase the y index of the map 2D list, 
        # and make the players position to be at the bottom of the screen
        elif self.player.sprite.rect.y > conf.window_height - conf.tile_size: 
            self.world_y += 1
            self.player.sprite.rect.y = 0
            
            self.player.sprite.destination = self.player.sprite.rect.x, self.player.sprite.rect.y
            self.player.sprite.moving = False
            self.player.sprite.counter = 0 
        self.chunk = Chunk(self.world_map[self.world_x][self.world_y])
            
class Menu(object):
    def __init__(self) -> None:
        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.title = Text((conf.window_width // 2, 1*(conf.window_height // 8)), self.font_size*3, self.exit_color, "THE SHADOWS OF WAR")
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.exit_color, "EXIT")
        self.btn_start = Text((conf.window_width // 2, 3*(conf.window_height // 8)), self.font_size*3, self.text_color, "START")
        self.btn_settings = Text((conf.window_width // 2, 5*(conf.window_height // 8)),  self.font_size*3, self.text_color, "SETTINGS")
        self.btn_tutorial = Text((conf.window_width // 2, 7*(conf.window_height // 8)), self.font_size*3, self.text_color, "HOW TO PLAY")

    def handle_event(self, event: pygame.event.Event):
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
                return Settings()
            elif self.btn_tutorial.collides(pos):
                return Tutorial()

    def display(self, window: pygame.surface.Surface) -> None:
        window.fill(colors.BLACK)

        self.title.display(window) 
        self.btn_exit.display(window)
        self.btn_start.display(window)
        self.btn_settings.display(window) 
        self.btn_tutorial.display(window) 

class Player_Choice(object):
    def __init__(self, slot, username) -> None:
        self.slot = slot
        self.username = username
        
        self.images = [
            pygame.transform.scale(pygame.image.load('assets/images/player1.png'), (conf.window_width // 6, conf.window_width // 6)),
            pygame.transform.scale(pygame.image.load('assets/images/player2.png'), (conf.window_width // 6, conf.window_width // 6))
        ]
        
        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.exit_color, "EXIT")
        self.btn_back = Text((1*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.text_color, "BACK")
        
        self.choose_character = Text((conf.window_width // 2, 1*(conf.window_height // 8)), self.font_size*3, self.text_color, "CHOOSE A CHARACTER:")

        
    def display(self, window: pygame.surface.Surface) -> None:
        window.fill(colors.BLACK)
        
        
        self.btn_back.display(window)
        self.btn_exit.display(window)
        self.choose_character.display(window)
        
        self.players = [
            window.blit(self.images[0], (1*(conf.window_width // 6), 3*(conf.window_height // 8))),
            window.blit(self.images[1], (4*(conf.window_width // 6), 3*(conf.window_height // 8)))
        ]
                
    def handle_event(self, event: pygame.event.Event):
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
                
            for playertype, player in enumerate(self.players):
                if player.collidepoint(pos):                            
                    chunk_x, chunk_y = 3, 3
                    world_x, world_y = 0, 2
            
                    return Game(self.slot, self.username, playertype, chunk_x, chunk_y, world_x, world_y)
                
class Input(object):
    def __init__(self, slot: int) -> None:
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

        
    def display(self, window: pygame.surface.Surface) -> None:
        window.fill(colors.BLACK)

        self.enter_name.display(window)
        self.btn_exit.display(window)
        self.btn_back.display(window)
        
        window.blit(pygame.font.Font("fonts/font.ttf", self.font_size*2).render(self.text, True, self.color), (self.input_box.x+(conf.window_width // 50), self.input_box.y+(conf.window_width // 50)))

        pygame.draw.rect(window, self.color, self.input_box, (conf.window_width // 250))

    def handle_event(self, event: pygame.event.Event):
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
    def __init__(self) -> None: 
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
    
    def handle_event(self, event: pygame.event.Event) -> Menu | Game | Input:
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
                        username, playertype, chunk_x, chunk_y, world_x, world_y = save
                        return Game(slot_index, username, playertype, chunk_x, chunk_y, world_x, world_y)
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
            save_index, username, playertype, _, _, _, _ = save
            saves_used[save_index] = save_index
        
        for i, rect in enumerate(self.slots):
            if saves_used[i] is not None:
                username, playertype, _, _, _, _ = self.saves.load(i)
                
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

class Tutorial(object):
    def __init__(self) -> None:        
        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.exit_color, "EXIT")
        self.btn_back = Text((1*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.text_color, "BACK")
        self.title = Text((conf.window_width // 2, 1*(conf.window_height // 8)), self.font_size*3, self.text_color, "TUTORIAL")

        
    def display(self, window: pygame.surface.Surface) -> None:
        window.fill(colors.BLACK) 
        
        self.btn_back.display(window)
        self.btn_exit.display(window)
        self.title.display(window)
                
    def handle_event(self, event: pygame.event.Event) -> Menu:
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

class Settings(object):
    def __init__(self) -> None:        
        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.exit_color, "EXIT")
        self.btn_back = Text((1*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.text_color, "BACK")
        self.title = Text((conf.window_width // 2, 1*(conf.window_height // 8)), self.font_size*3, self.text_color, "SETTINGS")
        
    def display(self, window: pygame.surface.Surface) -> None:
        window.fill(colors.BLACK) 
        
        self.btn_back.display(window)
        self.btn_exit.display(window)
        self.title.display(window)
                
    def handle_event(self, event: pygame.event.Event) -> Menu:
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

class GameOver(object):
    def __init__(self) -> None:        
        self.exit_color = colors.RED1
        self.text_color = colors.WHITE
        self.font_size = conf.pixel_size*4
        
        self.btn_exit = Text((9*(conf.window_width // 10), 1*(conf.window_height // 10)), self.font_size*2, self.exit_color, "EXIT")
        self.btn_back = Text((conf.window_width // 2, 3*(conf.window_height // 4)), self.font_size*3, self.exit_color, "BACK TO MAIN MENU")
        self.title = Text((conf.window_width // 2, 1*(conf.window_height // 8)), self.font_size*3, self.text_color, "GAME OVER!")
        
    def display(self, window: pygame.surface.Surface) -> None:
        window.fill(colors.BLACK) 
        
        self.btn_back.display(window)
        self.btn_exit.display(window)
        self.title.display(window)
                
    def handle_event(self, event: pygame.event.Event) -> Menu:
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



if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(conf.volume)
    pygame.mixer.music.load("sounds/soundtrack.mp3")
    pygame.mixer.music.play(-1)
    
    main = Main()
    main.run()