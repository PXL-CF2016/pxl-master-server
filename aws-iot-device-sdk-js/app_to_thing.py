# coding=utf-8
import boto3

# https://aqy9q7jfavde2.iot.us-west-2.amazonaws.com/things/PXL-CF2016/shadow

client = boto3.client('iot-data', region_name='us-west-2')

response = client.update_thing_shadow(
    thingName='PXL-CF2016',
    payload=b'{ \
    "state": { \
        "desired": { \
            "message_1": "My Name Is Joe" \
            } \
        } \
    }'
)
