import pygame

class ScoreCounter(pygame.font.Font):
    score = None
    font = None

    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("monospace", 15)

    def update(self, score):
        self.score = score

    def reset(self):
        self.score = 0

    def draw(self, screen):
        screen.blit(self.font.render(str(self.score), 1, (255,255,0)), (40,20))
