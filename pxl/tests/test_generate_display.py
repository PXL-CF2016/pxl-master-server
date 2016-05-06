from pxl.board_iot import generate_display, boto_response
from mock import patch
from django.test import TestCase, Client
from pxl.tests.string_generator_test_data import MLB_STRING, NFL_STRING, NHL_STRING, HEADLINE_STRING, WEATHER_STRING



class TestDisplayGenerator(TestCase):

    @patch('pxl.board_iot.form_mlb_string')
    @patch('pxl.board_iot.form_nhl_string')
    @patch('pxl.board_iot.form_weather_string')
    @patch('pxl.board_iot.form_nfl_string')
    @patch('pxl.board_iot.form_headline_string')
    @patch('pxl.board_iot.boto_response')
    def test_display(self, boto_response, form_headline_string, form_nfl_string, form_weather_string, form_nhl_string, form_mlb_string):
        """Test proper return string from user selections."""
        mocked_mlb = form_mlb_string
        mocked_nhl = form_nhl_string
        mocked_weather = form_weather_string
        mocked_headline = form_headline_string
        mocked_nfl = form_nfl_string
        mocked_mlb.return_value = MLB_STRING
        mocked_nhl.return_value = NHL_STRING
        mocked_weather.return_value = WEATHER_STRING
        mocked_headline.return_value = HEADLINE_STRING
        mocked_nfl.return_value = NFL_STRING
        selection_dict = {'mlb': '', 'nhl': '', 'nfl': '', 'weather': 'true', 'headlines': ''}
        response = generate_display(selection_dict)
        self.assertEqual(response, WEATHER_STRING)
