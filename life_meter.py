import pygame
class Life_Meter(pygame.sprite.Sprite):
    rect = None
    sprite = None
    x = None
    y = None
    lifes_left = None
    max_lives = None

    def __init__(self, sprite):
#        print("Initiating life meter")
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite 
        self.rect = self.sprite.get_rect()
        self.x = 600
        self.y = 20
        self.lifes_left = 3 
        self.max_lives = self.lifes_left 

    def reset(self):
        self.lifes_left = self.max_lives
    
    def lose_life(self):
        self.lifes_left -= 1
        
    def draw(self, screen):
        padding_x = 0
        for lifes in range(0, self.lifes_left):
            screen.blit(self.sprite, (self.x - padding_x, self.y))
            padding_x += 40
