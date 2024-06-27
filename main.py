import time
import traceback

from tqdm import tqdm
from db_connector import DBConnector
from weather_api import get_air_pollution_data 
import sys


DB_PATH="air_quality.db"
REFRESH_INTERVAL_SEC = 60


def refresh_air_data(db_connector: DBConnector):
    cities = db_connector.get_all_cities()
    for city in tqdm(cities):
        json_data = get_air_pollution_data(city)
        if json_data:
            db_connector.insert_data_from_json(city, json_data)
            # print(json_data)
        else:
            print(f"failed to get data for {city.name}", file=sys.stderr)


def main():
    db_connector = DBConnector(DB_PATH)
    first_run = True
    while True:
        if not first_run:
            print(f"Waiting {REFRESH_INTERVAL_SEC} s...")
            time.sleep(REFRESH_INTERVAL_SEC)
        try:
            print("Refreshing air data of cities")
            refresh_air_data(db_connector)
            first_run = False
        except:
            traceback.print_exc()


if __name__ == "__main__":
    main()