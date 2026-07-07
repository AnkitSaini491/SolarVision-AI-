
import requests
from config import WEATHER_API_KEY

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={WEATHER_API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url).json()

    if response.get("cod") != 200:
        return None

    return {

        "city": response["name"],

        "temperature": response["main"]["temp"],

        "humidity": response["main"]["humidity"],

        "weather": response["weather"][0]["main"],

        "description": response["weather"][0]["description"],

        "wind": response["wind"]["speed"]

    }
