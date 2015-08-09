import pygame
import random
from itertools import chain

'
 Class responsible for showing the question dialog
 and randomizing the order of the answers.
 
'
class Question_Dialog(pygame.sprite.Sprite):
    font = None
    rect = None
    sprite = None
    x = None
    y = None
    question = None
    correct = None
    incorrect = None
    padding_y = None

    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite 
        self.rect = self.sprite.get_rect()
        self.font = pygame.font.SysFont("monospace", 12)
        self.x = 80
        self.y = 60
        self.padding_y = 90
    
    def set_question(self, question_tuple):
        # Swap places randomly
        nbr_correct = random.getrandbits(1)
        if nbr_correct == 1:
            self.correct = "1. " + question_tuple[1] 
            self.incorrect = "2. " + question_tuple[2] 
        else:
            self.correct = "1. " + question_tuple[2] 
            self.incorrect = "2. " + question_tuple[1] 


        self.question = question_tuple[0]
        self.question = wrapline(self.question, self.font, 400) 
        self.correct = wrapline(self.correct, self.font, 400)
        self.incorrect = wrapline(self.incorrect, self.font, 400)
        return nbr_correct

    def draw(self, screen):
        screen.blit(self.sprite, (self.x,self.y))

        line_padding = 0 
        for line in self.question:
            screen.blit(self.font.render(line, 1, (0,0,0)), (40+self.x,40+self.y+(self.padding_y*0) + line_padding))
            line_padding += 20
        line_padding = 0

        for line in self.correct:
            screen.blit(self.font.render(line, 1, (0,0,0)), (40+self.x,40+self.y+(self.padding_y*1) + line_padding))
            line_padding += 20
        line_padding = 0

        for line in self.incorrect:
            screen.blit(self.font.render(line, 1, (0,0,0)), (40+self.x,40+self.y+(self.padding_y*2) + line_padding))
            line_padding += 20
        line_padding = 0

'''

  The following chunk of code is in full 
  stolen from http://www.pygame.org/wiki/TextWrapping

'''
def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped
 
 
def wrap_multi_line(text, font, maxwidth):
    """ returns text taking new lines into account.
    """
    lines = chain(*(wrapline(line, font, maxwidth) for line in text.splitlines()))
    return list(lines)
