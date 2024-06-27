class City:
    def __init__(self, city_id, name: str, lat: float, lon: float):
        self.city = city_id
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"City(name='{self.name}', lat={self.lat}, lon={self.lon})"