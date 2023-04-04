import requests

class API:
    @staticmethod
    def write(value, field = 1):
        requests.post(f"https://api.thingspeak.com/update?api_key=N7QUSQSDA8IUJM89&field2={value}")

    def get(field = 2):
        response = requests.get("https://api.thingspeak.com/channels/2094803/feeds.json?api_key=X6OZE8XX2HH3L7VF&results=8000")
        response = response.json()

        data = response['feeds']

        test = []
        for item in data:
            test.append(item[f'field{field}'])

        return test[::-1]

test = API.get()

print(test)
