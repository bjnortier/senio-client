#!/usr/bin/env python3

import time
import requests
import json
import sys

from senio_config import SenioConfig
config = SenioConfig()

image_file = sys.argv[1]
print('image file: {}'.format(image_file))

try:
    response = requests.post(
        config.url,
        headers={
            'Authorization': 'Bearer {}'.format(config.key)
        },
        files={'cam1': open(image_file, 'rb')},
        data={
            'json': json.dumps({
                'timestamp': time.time()*1000
            })
        })
    print('Status: {}'.format(response.status_code))
    print('Content: {}'.format(response.content))
except:
    print('Unexpected error:', sys.exc_info()[0])
