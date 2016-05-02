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


def form_nfl_json():
    """Form NFL JSON response."""
    nfl_games = get_nfl_data()['ss']
    nfl_json = {'games': []}
    for game in nfl_games:
        day = game[0]
        time = game[1]
        home = game[3]
        away = game[4]
        home_score = '0'
        away_score = '0'
        game_dict = {
            'home': home,
            'away': away,
            'day': day,
            'time': time,
            'home_score': home_score,
            'away_score': away_score
        }
        nfl_json['games'].append(game_dict)
    return nfl_json


def get_mlb_data():
    day = str(datetime.date.today().day)
    month = str(datetime.date.today().month)
    year = str(datetime.date.today().year)
    if int(month) < 10:
        month = '0' + month
    if int(day) < 10:
        day = '0' + day
    mlb_endpoint = ''.join(
        ['http://mlb.mlb.com/gdcross/components/game/mlb/year_',
            year,
            '/month_',
            month,
            '/day_',
            day,
            '/master_scoreboard.json']
        )
    return requests.get(mlb_endpoint).content.decode()
