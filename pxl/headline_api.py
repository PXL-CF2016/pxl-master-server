import requests
import os
import json


HEADLINE_ENDPOINT = ''.join([
    'http://api.npr.org/query?id=1004&fields=',
    'title&dateType=story&output=JSON&apiKey=',
    os.environ.get('NPR_KEY')
])


def get_headline_data():
    """Generate a response from the NPR headline endpoint."""
    headline_data = requests.get(HEADLINE_ENDPOINT)
    return headline_data.json()['list']['story']


def form_headline_dict():
    """Form a dict response for the NPR headline data."""
    headlines = get_headline_data()
    headline_json = {'headlines': []}
    for headline in headlines:
        title = headline['title']['$text']
        headline_dict = {
            'title': title
        }
        headline_json['headlines'].append(headline_dict)
    return headline_json

def form_headline_string():
    """Return string for aws iot."""
    headline_dict = form_headline_dict()
    headline_string = 'News: '
    for headline in headline_dict['headlines']:
        headline_data = headline['title'] + ' | '
        headline_string += headline_data
    return headline_string
