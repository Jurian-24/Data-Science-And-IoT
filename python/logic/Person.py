import os
import json

class Person:
    def __init__(self, id, firstName, lastName, startPosition, posFirstQuestion, posSecondQuestion, posThirdQuestion):
        self.id = id;
        self.firstName = firstName;
        self.LastName = lastName;
        self.startPosition = startPosition;
        self.posFirstQuestion = posFirstQuestion;
        self.posSecondQuestion = posSecondQuestion;
        self.posThirdQuestion = posThirdQuestion;

    def writePersonToJson(self):
        person = {}
        person[self.id] = []
        person[self.id].append({
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.LastName,
            "startpos": self.startPosition,
            "firstQuestion": self.posFirstQuestion,
            "secondQeustion": self.posSecondQuestion,
            "thirdQuestion": self.posThirdQuestion
        })


        path = os.path.abspath("data/persons.json")

        with open(path) as f:
            obj = json.load(f)

        obj["data"].append(person);

        with open(path, 'w+') as outfile:
            json.dump(obj, outfile)


