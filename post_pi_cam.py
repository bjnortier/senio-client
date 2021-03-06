#!/usr/bin/env python3

import picamera
import time
import requests
import json
import sys

from senio_config import SenioConfig
config = SenioConfig()

while True:
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.hflip = True
    camera.capture('img720x480.jpg')
    camera.close()

    try:
        response = requests.post(
            config.url,
            headers={
                'Authorization': 'Bearer {}'.format(config.key)
            },
            files={
                config.values['camera_field']: open('img720x480.jpg', 'rb')
            },
            data={
                'json': json.dumps({
                    'timestamp': time.time()*1000
                })
            })
        print('Status: {}'.format(response.status_code))
        print('Content: {}'.format(response.content))
    except:
        print('Unexpected error:', sys.exc_info()[0])

    time.sleep(600)
