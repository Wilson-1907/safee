import os
from dotenv import load_dotenv

load_dotenv()  # loads the .env file

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Example function
def get_weather(city):
    import requests
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {temp}°C with {desc}."
    return "Could not fetch weather."