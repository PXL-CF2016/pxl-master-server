# -*- coding: utf-8 -*-

import os
from urllib.request import urlopen
import json

WEATHER_URL = os.environ.get('WEATHER_API_URL')


def weather_api_call():
    """API call for current Seattle weather data."""
    weather_data = urlopen(WEATHER_URL)
    json_string = (weather_data.read()).decode('utf-8')
    parsed_json = json.loads(json_string)
    return parsed_json

def weather_api_json():
    """Grab temperature, forecast, and location data and return as json."""
    parsed_json = weather_api_call()
    temp = parsed_json['current_observation']['temperature_string']
    location = parsed_json['current_observation']['display_location']['full']
    weather = parsed_json['current_observation']['icon']
    json_format = {
        'location': location,
        'temperature': temp,
        'weather': weather}
    return print(json_format)
