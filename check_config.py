#!/usr/bin/env python3

import requests
import sys

from senio_config import SenioConfig
config = SenioConfig()

try:
    response = requests.get(
        config.url,
        headers={
            'Authorization': 'Bearer {}'.format(config.key)
        })
    print('Status: {}'.format(response.status_code))
    print('Content: {}'.format(response.content))
except:
    print('Unexpected error:', sys.exc_info()[0])
