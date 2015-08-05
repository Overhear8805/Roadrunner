import pygame
class Intro_Screen(pygame.sprite.Sprite):
    rect = None
    sprite = None
    x = None
    y = None

    def __init__(self, sprite):
#        print("Initiating life meter")
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite 
        self.rect = self.sprite.get_rect()
        self.x = 0
        self.y = 0

    def update(self, speed):
        self.x -= speed
 
    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
