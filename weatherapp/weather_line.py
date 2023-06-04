import requests
import json

def get_weather(city):
    """Get the weather for the specified city.

    Args:
        city (str): The name of the city.

    Returns:
        A dictionary containing the weather data.
    """

    # Create the API request URL.
    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}".format(
        city=city, api_key= '79ca906c37275a2e7d76e4e232cfd4f3'
    )

    # Make the API request.
    response = requests.get(url)

    # Check the response status code.
    if response.status_code != 200:
        raise Exception("API request failed: {}".format(response.status_code))

    # Parse the JSON response.
    weather_data = json.loads(response.content)

    return weather_data

def main():
    """The main function."""

    # Get the city name from the command line arguments.
    city = input("Enter the city name: ")

    # Get the weather data for the city.
    weather_data = get_weather(city)
    temp = weather_data["main"]["temp"]
    temp = temp - 275

    # Display the weather data.
    print("The weather in {} is:".format(city)) 
    print("- Temperature: {} degrees Celsius".format(temp))
    print("- Humidity: {}%".format(weather_data["main"]["humidity"]))
    print("- Wind speed: {} kilometers per hour".format(weather_data["wind"]["speed"]))

if __name__ == "__main__":
    main()