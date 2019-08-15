
from datetime import datetime
import requests
"""
Script to read current date and time
"""

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Get the current weather in Nairobi with API


def get_weather():
    """
    Script to check the current weather of Nairobi from API
    """
    api_url = "https://api.apixu.com/v1/current.json?key=47c95a23235f41fdbdf63941191408&q={}"
    city_name = input("City Name : ")

    url = api_url + city_name

    json_data = requests.get(url).json()

    location = json_data['location']['name']
    region = json_data['location']['region']
    temp = json_data['current']['temp_c']
    condition = json_data['current']['condition']['text']
    humidity = json_data['current']['humidity']

    print('Location : {}'.format(location))
    print('Region : {}'.format(region))
    print('Temperature: {}'.format(temp))
    print('Condition: {}'.format(condition))
    print('Humidity : {}'.format(humidity))


get_weather()
# Send a HTTP POST REQUEST


def send_post():

    api_endpoint = "https://hooks.zapier.com/hooks/catch/3078109/oo8v4wd/"

    payload = {
        'name': "Xavier Frankline",
        'temperature_celcius': 21,
        'humidity': 53
    }

    r = requests.post(url=api_endpoint, data=payload)
    print(r.status_code, r.reason)
    pastebin_url = r.text
    print("The pastebin_url is : {}".format(pastebin_url))


send_post()
