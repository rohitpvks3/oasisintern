import requests

def get_weather(api_key, location):
    """
    Fetch weather data for the specified location using the OpenWeatherMap API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    """
    Display weather data in a readable format.
    """
    if data.get("cod") != 200:
        print(f"Error: {data.get('message')}")
        return

    city = data['name']
    country = data['sys']['country']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description.capitalize()}")

def main():
    api_key = "6cee1f9c3a221e1ddd8d4b6b36b65768"  # Replace with your OpenWeatherMap API key
    location = input("Enter a city name or ZIP code: ")

    if not location:
        print("Location cannot be empty.")
        return

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
