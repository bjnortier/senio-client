import time
import requests
import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 7

URL = 'https://www.senio.io/publish/rpi_demo'
UUID = '48fd7f79-66e9-42ff-b437-9759d38a8f04'

while True:
    humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is None:
        continue
    print('Temp: {} Humidity: {}'.format(temp, humidity))

    try:
        response = requests.post(
            URL,
            headers={
                'Authorization': 'Bearer {}'.format(UUID)
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
