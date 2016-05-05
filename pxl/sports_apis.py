import re
import requests
import json
import datetime


NFL_ENDPOINT = 'http://www.nfl.com/liveupdate/scorestrip/scorestrip.json'
NHL_ENDPOINT = 'http://live.nhle.com/GameData/RegularSeasonScoreboardv3.jsonp'


def parse_nfl_content(strng):
    """Parse the NFL content for erroneous commas."""
    regex = re.compile(r'[,]+')
    return re.sub(regex, ',', strng)


def get_nfl_data():
    """Generate response from NFL score endpoint."""
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
    """Generate response from MLB score endpoint."""
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


def form_mlb_json():
    """Form MLB JSON response."""
    mlb_data = get_mlb_data()
    mlb_games = json.loads(mlb_data)['data']['games']['game']
    mlb_json = {'games': []}
    for game in mlb_games:
        home = game['home_team_name']
        away = game['away_team_name']
        time = game['time']
        try:
            home_score = game['linescore']['r']['home']
            away_score = game['linescore']['r']['away']
        except KeyError:
            home_score = '0'
            away_score = '0'
        try:
            winning_pitcher = game['winning_pitcher']['last']
            losing_pitcher = game['losing_pitcher']['last']
        except KeyError:
            winning_pitcher = ''
            losing_pitcher = ''
        try:
            pitching = game['pitcher']['last']
        except KeyError:
            pitching = ''
        try:
            at_bat = game['batter']['last']
        except KeyError:
            at_bat = ''
        game_dict = {
            'home': home,
            'away': away,
            'time': time,
            'home_score': home_score,
            'away_score': away_score,
            'winning_pitcher': winning_pitcher,
            'losing_pitcher': losing_pitcher,
            'pitching': pitching,
            'at_bat': at_bat,
        }
        mlb_json['games'].append(game_dict)
    return mlb_json


def get_nhl_data():
    """Get response from NHL endpoint."""
    nhl_data = requests.get(NHL_ENDPOINT)
    return nhl_data.content.decode()[15:-1]


def form_nhl_json():
    """Form NHL JSON response."""
    nhl_games = json.loads(get_nhl_data())['games']
    nhl_json = {'games': []}
    for game in nhl_games:
        home = game['htn']
        away = game['atn']
        home_score = game['hts']
        away_score = game['ats']
        time = game['bs']
        date = game['ts']
        game_dict = {
            'home': home,
            'away': away,
            'time': time,
            'home_score': home_score,
            'away_score': away_score,
            'time': time,
            'date': date
        }
        nhl_json['games'].append(game_dict)
    return nhl_json
