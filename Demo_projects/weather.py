import streamlit as st
import requests
import json
from geopy.geocoders import Nominatim


def get_weather(latitude, longitude, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def get_location_address(latitude, longitude):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    return location.address if location else ""

def main():
    st.title("Weather App with Location Indication")

    # Get user input for latitude and longitude
    latitude = st.number_input("Enter latitude")
    longitude = st.number_input("Enter longitude")

    if st.button("Get Weather"):
        # Get weather data
        api_key = "3032059c14a17da7f50cc0f98652c704"  # Replace with your OpenWeatherMap API key
        data = get_weather(latitude, longitude, api_key)

        if "main" in data:
            # Display location information
            location_address = get_location_address(latitude, longitude)
            st.subheader("Location")
            st.write(f"Latitude: {latitude}")
            st.write(f"Longitude: {longitude}")
            st.write(f"Address: {location_address}")

            # Display weather information
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            st.subheader("Weather Information")
            st.write(f"Description: {weather_description}")
            st.write(f"Temperature: {temperature} °C")
            st.write(f"Humidity: {humidity}%")
        else:
            st.error("Error fetching weather data. Please try again.")

if __name__ == "__main__":
    main()
