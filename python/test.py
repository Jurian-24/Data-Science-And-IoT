import requests
from prettytable import PrettyTable
import os


def tempTable():
    response = requests.get('https://api.thingspeak.com/channels/2065267/feeds.json?api_key=ZSAX2MQND13YPFWK&results=2')
    data = response.json()

    statisticsTable = PrettyTable(['Id', 'Date', 'temp'])

    for item in data['feeds']:
        statisticsTable.add_row([item['entry_id'], item['created_at'], item['field1']])

    print(statisticsTable, '\n')


def clothes():
    response = requests.get('https://api.thingspeak.com/channels/2065267/feeds.json?api_key=ZSAX2MQND13YPFWK&results=2')
    data = response.json()

    temperature = float(data['feeds'][-1]['field1'])

    if temperature >= 27:
        print('It\'s hot today! You should wear shorts and a t-shirt.')
    elif temperature >= 15:
        print('It\'s a nice day! You can wear jeans and a sweater.')
    elif temperature >= 4:
        print('It\'s a bit chilly! You should wear a jacket or coat.')
    else:
        print('It\'s very cold! You should wear a heavy coat, scarf, and gloves.')

    print('\n')


def main():
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        print('What do you want to see?')
        print('[1] Temp table')
        print('[2] What cloths can i wear')
        print('[3] Exit')

        userInput = input('Enter what you want to do: ')

        if (int(userInput) == 1):
            print('\n')
            tempTable()
        if (int(userInput) == 2):
            print('\n')
            clothes()
        if (int(userInput) == 3):
            break


if __name__ == '__main__':
    main()
