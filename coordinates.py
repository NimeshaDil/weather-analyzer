import requests

def get_coordinates(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}"
    response = requests.get(url)
    data = response.json()
    # print(data)

    if "results" in data and len(data["results"]) > 0:
        city = data["results"][0]
        latitude = city["latitude"]
        longitude = city["longitude"]
        country = city["country"]
        print(f"\n📍 Found: {city['name']}, {country} -> Latitude: {latitude}, Longitude: {longitude}")
        return latitude, longitude
    else:
        print("❌ City not found.")
        return None, None