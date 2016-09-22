#!/usr/bin/python3 -u

import time
import requests
import sys

from senio_config import SenioConfig
config = SenioConfig()

humidity, temp = 50.0, 22.0
print('Temp: {} Humidity: {}'.format(temp, humidity))

try:
    response = requests.post(
        config.url,
        headers={
            'Authorization': 'Bearer {}'.format(config.key)
        },
        json={
            'timestamp': time.time()*1000,
            'data': {
                'temp': temp,
                'humidity': humidity
            }
        })
    print('Status: {}'.format(response.status_code))
    print('Content: {}'.format(response.content))
except:
    print('Unexpected error:', sys.exc_info()[0])
