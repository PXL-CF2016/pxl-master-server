-*- coding:utf-8 -*-
from mock import patch
from django.test import TestCase
from pxl import weather_api
from weather_test_data import TEST_OUTPUT
import requests

RESP_DATA = {
             "location": "Seattle, WA",
             "weather": "partlycloudy",
             "temperature": "76.5 F (24.7 C)"
            }

class TestWeather(TestCase):

    @patch('pxl.weather_api')
    def test_weather_api_output_type(self, weather_api_call):
        mocked_api = weather_api.weather_api_call()
        self.assertEqual(type(TEST_OUTPUT), type(mocked_api))

    @patch('pxl.weather_api')
    def test_weather_api_output_length(self, weather_api_call):
        mocked_api = weather_api.weather_api_call()
        self.assertEqual(len(TEST_OUTPUT), len(mocked_api))

    @patch('pxl.weather_api')
    def test_weather_api_expected_location(self, weather_api_call):
        mocked_api = weather_api.weather_api_call()
        location = mocked_api['current_observation']['display_location']['full']
        self.assertEqual(location, 'Seattle, WA')

    @patch('pxl.weather_api')
    def test_weather_api_response_length(self, weather_api_json):
        mocked_json = weather_api.weather_api_json()
        self.assertEqual(len(RESP_DATA), len(mocked_json))

    @patch('pxl.weather_api')
    def test_weather_api_response_type(self, weather_api_json):
        mocked_json = weather_api.weather_api_json()
        self.assertEqual(type(RESP_DATA), type(mocked_json))
