
import os
from urllib.request import urlopen
import json

WEATHER_URL = os.environ.get('WEATHER_API_URL')


def weather_api():
    """API call for current Seattle weather data."""
    weather_data = urlopen(WEATHER_URL)
    json_string = (weather_data.read()).decode('utf-8')
    parsed_json = json.loads(json_string)
    temp = parsed_json['current_observation']['temperature_string']
    location = parsed_json['current_observation']['display_location']['full']
    weather = parsed_json['current_observation']['icon']
    return print("{} and {} in {}".format(temp, weather, location))

if __name__ == "__main__":
    weather_api()
