import re
import requests
import json
import datetime


NFL_ENDPOINT = 'http://www.nfl.com/liveupdate/scorestrip/scorestrip.json'
NHL_ENDPOINT = 'http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp'


def parse_nfl_content(strng):
    regex = re.compile(r'[,]+')
    return re.sub(regex, ',', strng)


def get_nfl_data():
    """Get NFL scores."""
    nfl_dat = requests.get(NFL_ENDPOINT).content.decode()
    parsed_nfl_dat = parse_nfl_content(nfl_dat)
    nfl_json = json.loads(parsed_nfl_dat)
    return nfl_json
