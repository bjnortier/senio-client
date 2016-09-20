# senio-client

This repo contains Python3 example code for posting sensor data to Senio.

## Getting started

- Clone this repo to you Raspberry Pi:

    $ git clone https://github.com/bjnortier/senio-client.git

- Create your sensor on [https://www.senio.io](senio.io). The rest of this document assumes you have a sensor with "temp" and "humidity" scalar fields, and a "cam1" image field defined on a sensor called "rpi". Copy the device key
to the clipboard.

- Copy the senio.ini.UPDATE_ME_WITH_SENSOR_VALUES to senio.ini


    $ cp senio.ini.UPDATE_ME_WITH_SENSOR_VALUES senio.ini

- Update the sensor name and key to the values from senio.io:


    [sensor]
    name=rpi
    key=aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa

- Check your setup by running the check.py script:


    $ ./check_config.py
    ----- CONFIG -----
    url: https://www.senio.io/publish/rpi
    key: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
    -------------------
    Status: 200
    Content: b'"Valid sensor and key"'

- Try posting dummy scalar values:


    $ ./post_dummy_dht22.py
    ----- CONFIG -----
    url: https://www.senio.io/publish/rpi
    key: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
    -------------------
    Temp: 22.0 Humidity: 50.0
    Status: 201
    Content:     b'{"timestamp":1474383378795.2,"data":{"temp":22,"humidity":50},"tags":null}'

- Try post an image **note the file argument**


    $ ./post_image.py img720x480.jpg
    ----- CONFIG -----
    url: https://www.senio.io/publish/rpi
    key: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
    -------------------
    image file: img720x480.jpg
    Status: 201
    Content:     b'{"timestamp":1474383509403.66,"data":{"cam1":"98c499c05bc8fcc440f8d4e5b7a74e80    ce6f3ae1"},"tags":null}'


- Post data from a DHT22 sensor once per minute:


    $ ./post_dht22.py
    ----- CONFIG -----
    url: https://www.senio.io/publish/rpi
    key: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
    -------------------
    Temp: 26.399999618530273 Humidity: 31.700000762939453
    Status: 201
    Content:     b'{"timestamp":1474383665737.89,"data":{"humidity":31.700000762939453,"temp":26.    399999618530273},"tags":null}'

- Post an image from the Pi camera every 10 minutes:


    $ ./post_pi_cam.py
    ----- CONFIG -----
    url: https://www.senio.io/publish/rpi
    key: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
    -------------------
    Status: 201
    Content:     b'{"timestamp":1474383732160.25,"data":{"cam1":"b6d0125a6be3e4d59ac437fb3b8c98ec    529853f6"},"tags":null}'
