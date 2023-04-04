from time import sleep
from logic.Person import *
from gpiozero import DistanceSensor

def getPos():
    distance = sensor.distance * 100
    distance = round(distance, 2)
    return distance

def getPosition():
    distances = []

    loop = True
    while(loop):
        try:
            distance = sensor.distance * 100
            distance = round(distance, 2)
            if(distance != 1000.0):
                print(distance)
                distances.append(getPos())
                sleep(1)
            else:
                print("Needs to be configured!")
                sleep(1)
                continue

        except KeyboardInterrupt:
            loop = False
            return distances

if __name__ == "__main__":
    sensor = DistanceSensor(23, 24, max_distance=10)

    id = input("ID: \n > ")
    firstName = input("First name: \n > ")
    lastName = input("Last name: \n > ")
    startPos = 100
    print("first question")
    firstQuestion = getPosition();
    print("second question")
    secondQuestion = getPosition();
    print("third question")
    thirdQuestion = getPosition();

    person = Person(
        id,
        firstName,
        lastName,
        startPos,
        firstQuestion,
        secondQuestion,
        thirdQuestion
    )

    try:
        person.writePersonToJson()
        print("Data has been written to JSON!")
    except:
        print("Something went wrong")

