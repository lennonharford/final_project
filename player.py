__authors__    = "Lennon", "Sali"
__license__    = "Free"
__emails__     = "lennonh45@kprschools.ca", "salmahs24@kprschools.ca"


import pygame
import config as conf
from tiles import Tile, Chunk
import pytmx

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x: int, y: int, chunk: Chunk, player: int) -> None:
        super().__init__()
        
        images_a, images_b = self._get_images(player)
            
        self.directions = {
            conf.up: [images_a[1], images_b[1]],  # Up
            conf.down: [images_a[0], images_b[0]],  # Down
            conf.left: [images_a[2], images_b[2]],  # Left
            conf.right: [images_a[3], images_b[3]]  # Right
        }
        
        self.player = player
        self.chunk = chunk
        self.direction = conf.up 
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
        

    def update(self) -> None:
        self._input()
        self._move()
        
    def _get_images(self, playertype: int) -> tuple[list, list]:
        data = pytmx.load_pygame("maps/players.tmx")
        players = [
            ["player2a", "player2b"],
            ["player1a", "player1b"]
        ] 
        
        images_static = []
        for _, _, surface in data.get_layer_by_name(players[playertype][0]).tiles():
            images_static.append(pygame.transform.scale(surface, conf.tile_dimensions).convert_alpha())

        images_animated = []
        for _, _, surface in data.get_layer_by_name(players[playertype][1]).tiles():
            images_animated.append(pygame.transform.scale(surface, conf.tile_dimensions).convert_alpha())
            
        return images_static, images_animated
                
    def _input(self) -> None:
        keys = pygame.key.get_pressed()

        if not self.moving:
            if keys[conf.up]:
                self.direction = conf.up
                self.destination = (self.rect.x, self.rect.y - conf.tile_size)
                self.moving = True
            elif keys[conf.down]:
                self.direction = conf.down
                self.destination = (self.rect.x, self.rect.y + conf.tile_size)
                self.moving = True
            elif keys[conf.left]:
                self.direction = conf.left
                self.destination = (self.rect.x - conf.tile_size, self.rect.y)
                self.moving = True
            elif keys[conf.right]:
                self.direction = conf.right
                self.destination = (self.rect.x + conf.tile_size, self.rect.y)
                self.moving = True
                
    def _can_move(self) -> bool:
        next_x, next_y = self.destination
        
        for wall in self.chunk.walls.sprites():
            if next_x == wall.rect.x and next_y == wall.rect.y:
                return False
        return True
    
    def _animate(self) -> None:
        self.animation_counter += 1
        
        if self.animation_counter >= self.animation_delay:
            
            # flip state
            self.animation_state = (self.animation_state + 1) % len(self.directions[self.direction])
            
            self.image = self.directions[self.direction][self.animation_state]
            self.mask = pygame.mask.from_surface(self.image)
            self.animation_counter = 0

    def _move(self) -> None:
        if self.moving:
            self.counter += 1

            if self.counter >= self.speed:
                
                if self._can_move():
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
            self._animate()
