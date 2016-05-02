from django.test import TestCase, Client
from pxl_master.pxl import sports_apis
from mock_sports_dat import NFL_RESPONSE, PARSED_NFL_RESPONSE


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
