from django.test import TestCase, Client
from pxl import sports_apis
from mock_sports_dat import NFL_RESPONSE, PARSED_NFL_RESPONSE, MOCK_NFL_DATA, NFL_JSON, MLB_RESPONSE, NHL_RESPONSE, NHL_JSON, NFL_DICT, MLB_DICT, NHL_DICT
from mock import patch


class SportsApiTests(TestCase):
    """Test sports API views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_parse_nfl_content(self):
        """Test parser for nfl content."""
        strng = NFL_RESPONSE
        nfl_parsed = sports_apis.parse_nfl_content(strng)
        self.assertEqual(nfl_parsed, PARSED_NFL_RESPONSE)

    def test_parse_nfl_content_small_string(self):
        """Test parser for nfl content."""
        strng = 'test,,, nfl ,,,,,response'
        nfl_parsed = sports_apis.parse_nfl_content(strng)
        self.assertEqual(nfl_parsed, 'test, nfl ,response')

    @patch('pxl.sports_apis.requests')
    def test_get_nfl_data(self, requests):
        """Test get nfl data function."""
        mock_method = requests.get().content.decode
        mock_method.return_value = NFL_RESPONSE
        result = sports_apis.get_nfl_data()
        self.assertEqual(result, MOCK_NFL_DATA)

    @patch('pxl.sports_apis.get_nfl_data')
    def test_form_nfl_json(self, get_nfl_data):
        """Test get nfl data function."""
        mock_method = get_nfl_data
        mock_method.return_value = MOCK_NFL_DATA
        result = sports_apis.form_nfl_json()
        self.assertDictEqual(result, NFL_DICT)

    @patch('pxl.sports_apis.requests')
    def test_get_mlb_data(self, requests):
        """Test get mlb data function."""
        mock_method = requests.get().content.decode
        mock_method.return_value = MLB_RESPONSE
        result = sports_apis.get_mlb_data()
        self.assertEqual(result, MLB_RESPONSE)

    @patch('pxl.sports_apis.get_mlb_data')
    def test_form_mlb_json(self, get_mlb_data):
        """Test form mlb json."""
        mock_method = get_mlb_data
        mock_method.return_value = MLB_RESPONSE
        result = sports_apis.form_mlb_json()
        self.assertDictEqual(result, MLB_DICT)

    @patch('pxl.sports_apis.requests')
    def test_get_nhl_data(self, requests):
        """Test get nhl data function."""
        mock_method = requests.get().content.decode
        mock_method.return_value = NHL_RESPONSE
        result = sports_apis.get_nhl_data()
        self.assertEqual(result, NHL_RESPONSE[15:-1])

    @patch('pxl.sports_apis.get_nhl_data')
    def test_form_nhl_json(self, get_nhl_data):
        """Test form nhl json."""
        mock_method = get_nhl_data
        mock_method.return_value = NHL_RESPONSE[15:-1]
        result = sports_apis.form_nhl_json()
        self.assertDictEqual(result, NHL_DICT)
