import requests

from data_structs import City


def get_air_pollution_data(city: City):
    api_key = "4fa8dfda83230f7c54614e0774112a23"
    base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
    url = f"{base_url}?lat={city.lat}&lon={city.lon}&appid={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None