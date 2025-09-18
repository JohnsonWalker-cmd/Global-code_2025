from pprint import pprint
from dotenv import load_dotenv # type: ignore
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London&APPID={API_KEY}')
pprint(r.json())

