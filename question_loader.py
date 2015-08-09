import json
from pprint import pprint

'
 A class that fetches questions (and corresponding answers) from a JSON-file.
 
'

class Question_Loader():
    questions_json = None
    counter = -1

    def __init__(self):
        self.counter = -1
        with open("questions.json") as questions_file:
            self.questions_json = json.load(questions_file)

    # Returns the next question. Will start to repeat questions when it has read every question.
    def get_next_question(self):
        self.counter += 1

        if self.counter > (len(self.questions_json["questions"])-1):
            self.counter = 0
        
        question = self.questions_json["questions"][self.counter]
        return (question["question"], question["correct"], question["incorrect"])
