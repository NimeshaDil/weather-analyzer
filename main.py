from request import get_coordinates, get_weather

if __name__ == "__main__":
    city_name = input("Enter City Name: ")
    lat, lon = get_coordinates(city_name)
    if lat and lon:
        get_weather(lat, lon)