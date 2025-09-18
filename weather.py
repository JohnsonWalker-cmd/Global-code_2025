
from pyowm import OWM # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

owm = OWM(API_KEY)
mgr = owm.weather_manager()
location = input("Enter a city: ")
try:
    
    observation = mgr.weather_at_place(location)
    w = observation.weather
    weather_details = {
        "status": w.detailed_status,
        "temperature": w.temperature('celsius')['temp'],
        "humidity": w.humidity,
        "wind": w.wind()['speed']
    }
    weather = f"Weather in {location}:\nStatus: {weather_details['status']}\nTemperature: {weather_details['temperature']}°C\nHumidity: {weather_details['humidity']}%\nWind Speed: {weather_details['wind']} m/s"
    print(weather)
except :
    print("City not found")


