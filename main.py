import sqlite3
from typing import List, Tuple
from data_structs import City
from weather_api import get_air_pollution_data 


DB_PATH="air_quality.db"

def get_all_cities(conn: sqlite3.Connection) -> List[Tuple[int, str, float, float]]:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM City')
    rows = cursor.fetchall()

    cities = [City(city_id=row[0], name=row[1], lat=row[2], lon=row[3]) for row in rows]

    return cities

def main():
    conn = sqlite3.connect(DB_PATH)
    cities = get_all_cities(conn=conn) 
    for city in cities:
        print(get_air_pollution_data(city))


if __name__ == "__main__":
    main()