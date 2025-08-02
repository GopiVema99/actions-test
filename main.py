import logging
import requests
import os

# Set up logger
logger = logging.getLogger("WeatherLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("weather.log", encoding="utf8")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Get API key from environment or hardcode it (not recommended for production)
API_KEY = os.environ.get("WEATHER_API_KEY", "7c863a32153d41a9841125931250208 ")
CITY = "Sydney"
COUNTRY = "Australia"

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    logger.info(f"Sending request to: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Weather in {city}: {data['current']['temp_c']}°C, Condition: {data['current']['condition']['text']}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching weather data: {e}")
    except KeyError as e:
        logger.error(f"Unexpected response structure: {e}")

if __name__ == "__main__":
    logger.info(f"Starting weather fetch for {CITY}")
    get_weather(API_KEY, CITY)
    logger.info("Weather fetch complete")
