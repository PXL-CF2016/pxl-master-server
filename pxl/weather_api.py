# -*- coding: utf-8 -*-

import os
import requests
import json

WEATHER_URL = os.environ.get('WEATHER_API_URL')


def weather_api_call():
    """API call for current Seattle weather data in JSON."""
    weather_data = requests.get(WEATHER_URL).json()
    return weather_data

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
    return json_format
