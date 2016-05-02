from django.test import TestCase, Client
from pxl_master.pxl import sports_apis
from mock_sports_dat import NFL_RESPONSE, PARSED_NFL_RESPONSE, MOCK_NFL_DATA, NFL_JSON
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

    @patch('pxl_master.pxl.sports_apis.requests')
    def test_get_nfl_data(self, requests):
        """Test get nfl data function."""
        mock_method = requests.get().content.decode
        mock_method.return_value = NFL_RESPONSE
        result = sports_apis.get_nfl_data()
        self.assertEqual(result, MOCK_NFL_DATA)

    @patch('pxl_master.pxl.sports_apis.get_nfl_data')
    def test_form_nfl_json(self, get_nfl_data):
        """Test get nfl data function."""
        mock_method = get_nfl_data
        mock_method.return_value = MOCK_NFL_DATA
        result = sports_apis.form_nfl_json()
        self.assertJSONEqual(result, NFL_JSON)
