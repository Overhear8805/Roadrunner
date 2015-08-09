import pygame
import random

'
 A class representing an obsticle on the road.
 Collision detection is done in main.py, but this
 class holds the neccesary properties and methods
 to make it possible to detect.

'
class Obsticle(pygame.sprite.Sprite):
    rect = None
    sprite = None
    x = None
    y = None

    def __init__(self, sprite):
#        print("Initiating obsticle")
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite 
        self.rect = self.sprite.get_rect()
        self.rect.inflate(-10,-10) # Shrinks the collision rectangle to make the game a little easier.
        self.x = 640
        self.y = 320
    
    def reset(self):
        self.x = random.randint(640, 640*3)
        self.y = 320

    def update(self, dx, dy):
        self.x -= dx
        self.y -= dy
        self.rect[0] = self.x
        self.rect[1] = self.y 
        
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
