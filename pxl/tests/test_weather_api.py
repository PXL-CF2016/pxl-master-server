# -*- coding:utf-8 -*-
from mock import patch
from django.test import TestCase
from pxl.weather_api import weather_api_call, weather_api_json
from weather_test_data import TEST_OUTPUT
import requests
from pxl.weather_api import WEATHER_URL

RESP_DATA = {
             "location": "Seattle, WA",
             "weather": "partlycloudy",
             "temperature": "76.5 F (24.7 C)"
            }

class TestWeather(TestCase):

    @patch('pxl.weather_api.requests')
    def test_weather_api_call(self, requests):
        """Test expected output of API call."""
        mocked_method = requests.get().json()
        mocked_method.return_value = TEST_OUTPUT
        response = weather_api_call()
        self.assertEqual(response.return_value, TEST_OUTPUT)

    @patch('pxl.weather_api.requests')
    def test_weather_api_call_repsonse_type(self, requests):
        """Test expected output is a dictionary."""
        mocked_method = requests.get().json()
        mocked_method.return_value = TEST_OUTPUT
        response = weather_api_call()
        self.assertEqual(type(response.return_value), type(TEST_OUTPUT))

    @patch('pxl.weather_api.requests')
    def test_weather_api_expected_location(self, requests):
        """Test expected location is Seattle, WA."""
        mocked_method = requests.get().json()
        mocked_method.return_value = TEST_OUTPUT
        response = weather_api_call()
        location = response.return_value['current_observation']['display_location']['full']
        self.assertEqual(location, 'Seattle, WA')

    @patch('pxl.weather_api.requests')
    def test_weather_api_response_length(self, requests):
        """Test if response is the expected length."""
        mocked_method = requests.get().json()
        mocked_method.return_value = TEST_OUTPUT
        response = weather_api_json()
        self.assertEqual(len(response), 3)

    @patch('pxl.weather_api.requests')
    def test_weather_api_response_type(self, requests):
        """Test if the response is a dictionary."""
        mocked_method = requests.get().json()
        mocked_method.return_value = TEST_OUTPUT
        response = weather_api_json()
        self.assertEqual(type(response), type(RESP_DATA))

    @patch('pxl.weather_api.requests')
    def test_weather_api_response_right_keys(self, requests):
        """Ensure keys in dict are the expected data fields."""
        mocked_method = requests.get().json()
        mocked_method.return_value = TEST_OUTPUT
        response = weather_api_json()
        self.assertTrue("weather" in response)
        self.assertTrue("location" in response)
        self.assertTrue("temperature" in response)

    @patch('pxl.weather_api.requests')
    def test_weather_api_response_wrong_keys(self, requests):
        """Test improper key is not in response."""
        mocked_method = requests.get().json()
        mocked_method.return_value = TEST_OUTPUT
        response = weather_api_json()
        self.assertFalse("slurpee" in response)
