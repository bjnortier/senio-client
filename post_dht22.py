import time
import requests
import sys
import Adafruit_DHT

from senio_config import SenioConfig
config = SenioConfig()

sensor = Adafruit_DHT.DHT22
pin = 7

while True:
    humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is None:
        continue
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

    time.sleep(60)
