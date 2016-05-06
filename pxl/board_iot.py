# coding=utf-8
import boto3
from pxl.sports_apis import form_mlb_string, form_nhl_string, form_nfl_string
from pxl.weather_api import form_weather_string
from pxl.headline_api import form_headline_string


# https://aqy9q7jfavde2.iot.us-west-2.amazonaws.com/things/PXL-CF2016/shadow


def generate_display(params):
    """Takes the params dictionary and returns the appropriate response for iot."""
    message_string = ''
    mlb_string = form_mlb_string()
    nhl_string = form_nhl_string()
    nfl_string = form_nfl_string()
    weather_string = form_weather_string()
    headline_string = form_headline_string()
    data_dict = {'mlb': mlb_string, 'nhl': nhl_string, 'nfl': nfl_string, 'weather': weather_string, 'headlines': headline_string}

    for key in params:
        if params[key] == 'true':
            message_string += data_dict[key]
    boto_response(message_string)

def boto_response(message):
    """Send a new message to the IOT device."""
    part_1 = '{ "state": { "desired": { "message_1": "'
    part_3 = '" } } }'
    final_message = ''.join([part_1, message, part_3])
    final_message = final_message.encode('utf-8')
    client = boto3.client('iot-data', region_name='us-west-2')
    response = client.update_thing_shadow(
        thingName='PXL-CF2016',
        payload=final_message
    )
