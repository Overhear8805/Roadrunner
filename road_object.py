import pygame

'
 A class that represents the road. For now it does almost nothing.

'

class Road_Object(pygame.sprite.Sprite):
    rect = None
    sprite = None
    x = None
    y = None
    offset = None

    def __init__(self, sprite, offset):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite 
        self.rect = self.sprite.get_rect()
        self.x = 0 + offset 
        self.y = 0
        self.offset = offset 
    
    def update(self, speed):
        if self.x - speed <= ((-640/2) + self.offset):
            self.x = self.offset 
        else:
            self.x -= speed
        
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
