# -*- coding: utf-8 -*-

import os
import requests
import json

WEATHER_URL = os.environ.get('WEATHER_API_URL')


def weather_api_call():
    """API call for current Seattle weather data in JSON."""
    weather_data = requests.get(WEATHER_URL).json()
    return weather_data

def weather_api_dict():
    """Grab temperature, forecast, and location data and return as dict."""
    parsed_json = weather_api_call()
    temp = parsed_json['current_observation']['temperature_string']
    location = parsed_json['current_observation']['display_location']['full']
    weather = parsed_json['current_observation']['icon']
    dictionary_format = {
        'location': location,
        'temperature': temp,
        'weather': weather}
    return dictionary_format

def form_weather_string():
    weather_dict = weather_api_dict()
    weather_string = 'Weather: '
    weather_data = weather_dict['temperature'] + ' and ' + weather_dict['weather'] + ' in ' + weather_dict['location'] + ' | '
    weather_string += weather_data
    return weather_string
