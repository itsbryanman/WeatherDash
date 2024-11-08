import requests
import json

# Get your API key from OpenWeatherMap and replace "YOUR_API_KEY_HERE"
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # For Celsius, use "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data.")
        return None

def display_weather(data):
    if data:
        city = data["name"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Use emojis or icons to represent weather
        weather_icon = ""
        if "cloud" in weather_desc:
            weather_icon = "☁️"
        elif "rain" in weather_desc:
            weather_icon = "🌧️"
        elif "clear" in weather_desc:
            weather_icon = "☀️"
        elif "snow" in weather_desc:
            weather_icon = "❄️"
        else:
            weather_icon = "🌡️"

        print(f"\nWeather in {city} {weather_icon}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_desc.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")
    else:
        print("Weather data not available.")

def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
