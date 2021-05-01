# env
import os
from os.path import join, dirname
from dotenv import load_dotenv
# helpers
from time import sleep
from playsound import playsound
# requests
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Session

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=MATIC'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    data = json.loads(response.text)['data']['MATIC']
    price = data['quote']['USD']['price']

    while price < 0.8:
        print(round(price, 4))
        sleep(.75)

    print('its at .8')
    playsound('alarm.mp3')
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
