import sqlite3
from typing import Dict, List, Optional, Tuple

from data_structs import City


class DBConnector:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def get_all_cities(self) -> List[City]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT city_id, name, lat, lon FROM City')
        rows = cursor.fetchall()
        return [City(city_id=row[0], name=row[1], lat=row[2], lon=row[3]) for row in rows]
    
    def get_all_metrics(self) -> List[str]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT name FROM AirMetric')
        rows = cursor.fetchall()
        return [row[0] for row in rows]

    def get_measurements(self, city_id: int, metric_id: int) -> List[Tuple[int, float]]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT timestamp, value FROM Measurement WHERE city_id=? AND metric_id=? ORDER BY timestamp', (city_id, metric_id))
        rows = cursor.fetchall()
        return rows


    def get_metric_id(self, metric_name: str) -> Optional[int]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT metric_id FROM AirMetric WHERE name=?', (metric_name,))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None

    def insert_measurement(self, city_id: int, metric_id: int, value: float, timestamp: int):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT OR IGNORE INTO Measurement (city_id, metric_id, value, timestamp) VALUES (?, ?, ?, ?)',
            (city_id, metric_id, value, timestamp)
        )
        self.conn.commit()

    def insert_data_from_json(self,city: City, json_data: Dict):

        measurement = json_data["list"][0]
        timestamp = measurement["dt"]
        components = measurement["components"]

        for metric_name, value in components.items():
            metric_id = self.get_metric_id(metric_name)
            if metric_id is not None:
                self.insert_measurement(city.city_id, metric_id, value, timestamp)
            else:
                print(f"No metric found with name {metric_name}")
