import requests
from coordinates import get_coordinates
from datetime import datetime

def get_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        f"&timezone=auto"
    )
    response = requests.get(url)
    data = response.json()

    # print(data)

    if "daily" in data:
        daily = data["daily"]
        print("\n🌤 5-Day Forecast:\n")
        for i in range(5):  # Only next 3 days
            # date = daily["time"][i]
            iso_date = daily["time"][i]
            max_temp = daily["temperature_2m_max"][i]
            min_temp = daily["temperature_2m_min"][i]
            rain = daily["precipitation_sum"][i]
            # Format date nicely
            day = datetime.strptime(iso_date, "%Y-%m-%d").strftime("%A, %b %d")
            print(f"{iso_date}, {day}: {min_temp}°C - {max_temp}°C | 💧 Rain: {rain} mm")
    else:
        print("❌ Forecast data not available.")

