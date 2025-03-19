import requests
import json

lat = 41.2646 # for Tashkent
lon = 69.2163
API_key = 'f082e45d66926670cfb8349a251e2ba5' # personal API key

def wdata_for_city(lat, lon, api):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}'
    weather = requests.get(url)

    if weather.status_code == 200:
        city = weather.json()
        # to make it easy to read, creating variables. If unnecessary, the next commented line should be used instead:
    #   print(city) 
        city_weather = city['weather']
        city_main = city['main']
        city_wind = city['wind']
        print('Weather in', city['name'], 'is', city_weather[0]['main'].lower(), 'with', city_weather[0]['description'])
        print("Temperature is", city_main['temp'], 'and feels like', city_main['feels_like'], ' with humidity of', city_main['humidity'])
        print("The speed of the wind is", city_wind['speed'])

    elif weather.status_code == 401:
        print("Error: Unauthorized. Check your API key.")
    elif weather.status_code == 404:
        print("Error: City not found. Check the coordinates.")
    else:
        print(f"Error {weather.status_code}: {weather.text}")

wdata_for_city(lat, lon, API_key)