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

- Try post an image **NOTE THE ARGUMENT**


    $ ./post_image.py img720x480.jpg
    ----- CONFIG -----
    url: https://www.senio.io/publish/rpi
    key: aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa
    -------------------
    image file: img720x480.jpg
    Status: 201
    Content:     b'{"timestamp":1474383509403.66,"data":{"cam1":"98c499c05bc8fcc440f8d4e5b7a74e80    ce6f3ae1"},"tags":null}'


-

1 post_dht22.py: Post scalar measurement data
1 post_photo.py: Post an image
1 post_pi_cam.py: Post the image form the Pi camera once per minute
