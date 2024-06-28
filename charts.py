import datetime
from db_connector import DBConnector
import matplotlib.pyplot as plt
def plot_data(db_connector: DBConnector ):
    cities = db_connector.get_all_cities()
    metrics = db_connector.get_all_metrics()

    for city in cities:
        for metric in metrics:
            metric_id = db_connector.get_metric_id(metric)
            if metric_id is not None:
                measurements = db_connector.get_measurements(city.city_id, metric_id)
                if measurements:
                    timestamps, values = zip(*measurements)
                    dates = [datetime.datetime.fromtimestamp(ts) for ts in timestamps]

                    plt.figure(figsize=(10, 6))
                    plt.plot(dates, values, marker='o')
                    plt.title(f'{metric} Levels in {city.name}')
                    plt.xlabel('Time')
                    plt.ylabel(f'{metric} Value')
                    plt.grid(True)
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.savefig(f'{city.name}_{metric}.png')
                    plt.close()
