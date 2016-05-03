from django.test import TestCase, Client
from pxl_master.pxl import headline_api
from mock_headline_dat import NPR_RESPONSE, NPR_JSON
from mock import patch


class SportsApiTests(TestCase):
    """Test sports API views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    @patch('pxl_master.pxl.headline_api.requests')
    def test_get_headline_data(self, requests):
        """Test get headline data function."""
        mock_method = requests.get().json
        mock_method.return_value = NPR_RESPONSE
        result = headline_api.get_headline_data()
        self.assertEqual(result, NPR_RESPONSE['list']['story'])

    @patch('pxl_master.pxl.headline_api.get_headline_data')
    def test_form_nfl_json(self, get_headline_data):
        """Test get headline data function."""
        mock_method = get_headline_data
        mock_method.return_value = NPR_RESPONSE['list']['story']
        result = headline_api.form_headline_json()
        self.assertJSONEqual(result, NPR_JSON)
