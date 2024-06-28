import time
import traceback
from typing import List, Tuple

from tqdm import tqdm
from db_connector import DBConnector
from weather_api import get_air_pollution_data 
import sys
from charts import plot_data


DB_PATH="air_quality.db"
REFRESH_INTERVAL_SEC = 60
OUTDIR="charts"


def check_air_quality_standards(db_connector: DBConnector) -> List[Tuple[str, str, float, float]]:
    latest_measurements = db_connector.get_latest_measurements()
    exceeded_standards = []

    for city_name, metric_name, _, value, acceptable_level in latest_measurements:
        if value > acceptable_level:
            exceeded_standards.append((city_name, metric_name, value, acceptable_level))

    return exceeded_standards



def refresh_air_data(db_connector: DBConnector):
    cities = db_connector.get_all_cities()
    for city in tqdm(cities):
        json_data = get_air_pollution_data(city)
        if json_data:
            try:
                db_connector.insert_data_from_json(city, json_data)
            except:
                traceback.print_exc()
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
            print(f"Generating charts for each city pollution")
            plot_data(db_connector, output_dir=OUTDIR)
            print(f"Checking if any air quality standarts are exceeded")
            exceeded_standarts = check_air_quality_standards(db_connector) 
            print(exceeded_standarts)
            first_run = False
        except:
            traceback.print_exc()


if __name__ == "__main__":
    main()