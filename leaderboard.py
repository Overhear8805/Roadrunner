import pygame
import datetime 
import os
import json

class Leaderboard(pygame.font.Font):
    FILE_NAME = "highscore.json"
    score = None
    font = None
    new_score = None
    new_name = None
    scores = None

    def __init__(self, new_name, new_score):
        self.score = 0
        self.font = pygame.font.SysFont("monospace", 15)
        self.new_score = int(new_score) 
        self.new_name = new_name 

        if not os.path.isfile(self.FILE_NAME):
            self.on_empty_file()

    def on_empty_file(self):
        empty_score_file = open(self.FILE_NAME,"w")
        empty_score_file.write("[]")
        empty_score_file.close()

    def save_score(self):
        if not self.scores == None:
            new_json_score = {
                    "name":self.new_name,
                    "score":self.new_score,
                    "time":str(datetime.datetime.now().time())
                    }

            self.scores.append(new_json_score)

            self.scores = self.sort_scores(self.scores)

            highscore_file = open(self.FILE_NAME, "r+")
            highscore_file.write(json.dumps(self.scores))
        else:
            self.load_previous_scores()
            self.save_score() # ...and lets hope loading works!

    def sort_scores(self, json):
        # A somewhat dirty method for sorting the JSON entries... It works though!
        scores_dict = dict() 
        sorted_list = list()

        for obj in json:
            scores_dict[obj["score"]]=obj

        for key in sorted(scores_dict.keys(), reverse=True):
            sorted_list.append(scores_dict[key])

        return sorted_list 

    def load_previous_scores(self):
        with open(self.FILE_NAME) as highscore_file:
           self.scores = json.load(highscore_file)
           self.scores = self.scores

    def draw(self, screen):
        padding_y = 0
        max_scores = 8
        nbr_scores = 1
        for score in self.scores:
            if nbr_scores <= max_scores:
                screen.blit(self.font.render(str(nbr_scores)+". " +str(score["name"]) +": " + str(score["score"]), 1, (0,0,0)), (220,200 + padding_y))
                padding_y += 20
                nbr_scores += 1
