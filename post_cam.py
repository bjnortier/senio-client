import picamera
import time
import requests
import json
import sys

URL = 'https://www.senio.io/publish/rpi_demo'
UUID = '48fd7f79-66e9-42ff-b437-9759d38a8f04'

while True:
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.capture('img720x480.jpg')
    camera.close()

    try:
        response = requests.post(
            URL,
            headers={
                'Authorization': 'Bearer {}'.format(UUID)
            },
            files={'cam1': open('img720x480.jpg', 'rb')},
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
