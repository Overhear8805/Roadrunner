import json
from pprint import pprint

class Question_Loader():
    questions_json = None
    counter = -1

    def __init__(self):
        self.counter = -1
        with open("questions.json") as questions_file:
            self.questions_json = json.load(questions_file)

    def get_next_question(self):
        self.counter += 1

        if self.counter > (len(self.questions_json["questions"])-1):
            self.counter = 0
        
        question = self.questions_json["questions"][self.counter]
        return (question["question"], question["correct"], question["incorrect"])

    def check_answer(self, guess):
        pass
        # Check if guess (1, x, 2) is the same as the answer in the JSON file

