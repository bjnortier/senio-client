import configparser


class SenioConfig:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('senio.ini')
        default_url = 'https://www.senio.io/publish/'
        if 'base_url' in config['sensor']:
            base_url = config['sensor']['base_url']
        else:
            base_url = default_url
        url = '{}{}'.format(base_url, config['sensor']['name'])
        key = config['sensor']['key']
        print('----- CONFIG -----')
        print('url: {}'.format(url))
        print('key: {}'.format(key))
        print('-------------------')
        self.url = url
        self.key = key
