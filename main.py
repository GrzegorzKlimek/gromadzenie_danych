import sqlite3
from typing import List, Tuple
from data_structs import City
from db_connector import DBConnector
from weather_api import get_air_pollution_data 


DB_PATH="air_quality.db"


def refresh_air_data(db_connector: DBConnector):
    cities = db_connector.get_all_cities()
    for city in cities:
        print(get_air_pollution_data(city))


def main():
    db_connector = DBConnector(DB_PATH)
    refresh_air_data(db_connector)


if __name__ == "__main__":
    main()