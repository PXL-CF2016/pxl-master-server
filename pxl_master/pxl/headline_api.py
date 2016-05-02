import requests
import json


headline_endpoint = 'http://api.npr.org/query?id=1004&fields=title&dateType=story&output=JSON&apiKey=MDI0MTM4NTA1MDE0NjIyMDU0OTM1ZDUwNQ000'


def get_headline_data():
    headline_data = requests.get(headline_endpoint)
    return headline_data.json()['list']['story']
