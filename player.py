import pygame
import config as conf
from groups import *
import pytmx

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, chunk, player):
        super().__init__()
        data = pytmx.load_pygame("maps/players.tmx")
        
        player_names = {
            1: ["player1a", "player1b"],
            2: ["player2a", "player2b"]
        }    
            
        images_a = []
        for _, _, surface in data.get_layer_by_name(player_names[player][0]).tiles():
            images_a.append(pygame.transform.scale(surface, conf.tile_dimensions).convert_alpha())

        images_b = []
        for _, _, surface in data.get_layer_by_name(player_names[player][1]).tiles():
            images_b.append(pygame.transform.scale(surface, conf.tile_dimensions).convert_alpha())
            
            
        self.directions = {
            pygame.K_w: [images_a[1], images_b[1]],  # Up
            pygame.K_s: [images_a[0], images_b[0]],  # Down
            pygame.K_a: [images_a[2], images_b[2]],  # Left
            pygame.K_d: [images_a[3], images_b[3]]  # Right
        }
        
        self.chunk = chunk
        self.direction = pygame.K_s  
        self.animation_state = 0  
        self.image = self.directions[self.direction][self.animation_state]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(x*conf.tile_size, y*conf.tile_size)) 

        self.destination = x*conf.tile_size, y*conf.tile_size 
        self.moving = False 
        self.speed = 1 

        self.counter = 0 
        self.animation_counter = 0  
        self.animation_delay = 10 
        
        self.step = conf.pixel_size

    def update(self):
        self.input()
        self.move()
                
    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moving:
            if keys[pygame.K_w]:
                self.direction = pygame.K_w
                self.destination = (self.rect.x, self.rect.y - conf.tile_size)
                self.moving = True
            elif keys[pygame.K_s]:
                self.direction = pygame.K_s
                self.destination = (self.rect.x, self.rect.y + conf.tile_size)
                self.moving = True
            elif keys[pygame.K_a]:
                self.direction = pygame.K_a
                self.destination = (self.rect.x - conf.tile_size, self.rect.y)
                self.moving = True
            elif keys[pygame.K_d]:
                self.direction = pygame.K_d
                self.destination = (self.rect.x + conf.tile_size, self.rect.y)
                self.moving = True
                
    def can_move(self):
        next_x, next_y = self.destination
        
        for wall in self.chunk.walls.sprites():
            if next_x == wall.rect.x and next_y == wall.rect.y:
                return False
        return True
    
    def animate(self):
        self.animation_counter += 1
        
        if self.animation_counter >= self.animation_delay:
            
            # flip state
            self.animation_state = (self.animation_state + 1) % len(self.directions[self.direction])
            
            self.image = self.directions[self.direction][self.animation_state]
            self.mask = pygame.mask.from_surface(self.image)
            self.animation_counter = 0

    def move(self):
        if self.moving:
            self.counter += 1

            if self.counter >= self.speed:
                
                if self.can_move():
                    dx = self.destination[0] - self.rect.x
                    dy = self.destination[1] - self.rect.y
                                        
                    if dx != 0: # is the rect on the desired pos
                        if abs(dx) <= self.step: # is it less than or equal to a step size? (is it close enough?)
                            self.rect.x, _ = self.destination# set the rect to the desired pos
                            self.moving = False # player is not moving (open for new desired pos)
                        else:
                            # move the rect to the side by a step
                            self.rect.x += self.step if dx > 0 else -self.step
                    elif dy != 0:
                        if abs(dy) <= self.step:
                            _, self.rect.y = self.destination
                            self.moving = False
                        else:
                            self.rect.y += self.step if dy > 0 else -self.step
                else:
                    self.destination = self.rect.x, self.rect.y
                    self.moving = False
                
                self.counter = 0  # Reset the counter after movement
            self.animate()
