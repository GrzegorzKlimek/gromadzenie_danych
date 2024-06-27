import time
import traceback
from db_connector import DBConnector
from weather_api import get_air_pollution_data 
import sys


DB_PATH="air_quality.db"


def refresh_air_data(db_connector: DBConnector):
    cities = db_connector.get_all_cities()
    for city in cities:
        json_data = get_air_pollution_data(city)
        if json_data:
            db_connector.insert_data_from_json(city, json_data)
            print(json_data)
        else:
            print(f"failed to get data for {city.name}", file=sys.stderr)


def main():
    db_connector = DBConnector(DB_PATH)
    while True:
        time.sleep(5)
        try:
            refresh_air_data(db_connector)
        except:
            traceback.print_exc()


if __name__ == "__main__":
    main()