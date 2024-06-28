CREATE TABLE IF NOT EXISTS City (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lat REAL NOT NULL,
    lon REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS AirMetric (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS Measurement (
    measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    metric_id INTEGER,
    value REAL NOT NULL,
    timestamp INTEGER NOT NULL,
    UNIQUE (metric_id, city_id, timestamp),
    FOREIGN KEY (city_id) REFERENCES City(city_id),
    FOREIGN KEY (metric_id) REFERENCES AirMetric(metric_id)
);


-- Insert cities into the City table
INSERT INTO City (name, lat, lon) VALUES ('Wroclaw', 51.107883, 17.038538);
INSERT INTO City (name, lat, lon) VALUES ('Kraków', 50.049683, 19.944544);
INSERT INTO City (name, lat, lon) VALUES ('Warszawa', 52.237049, 21.017532);
INSERT INTO City (name, lat, lon) VALUES ('Katowice', 50.270908, 19.039993);
INSERT INTO City (name, lat, lon) VALUES ('Poznań', 52.409538, 16.931992);
INSERT INTO City (name, lat, lon) VALUES ('Gdańsk', 54.372158, 18.638306);
INSERT INTO City (name, lat, lon) VALUES ('Białystok', 53.1324886, 23.1688403);
INSERT INTO City (name, lat, lon) VALUES ('Łódź', 51.759445, 19.457216);
INSERT INTO City (name, lat, lon) VALUES ('Lublin', 51.246452, 22.568445);
INSERT INTO City (name, lat, lon) VALUES ('Bydgoszcz', 53.123482, 18.008438);
INSERT INTO City (name, lat, lon) VALUES ('Szczecin', 53.428543, 14.552812);
INSERT INTO City (name, lat, lon) VALUES ('Rzeszów', 50.041187, 21.999121);
INSERT INTO City (name, lat, lon) VALUES ('Kielce', 50.866077, 20.628569);
INSERT INTO City (name, lat, lon) VALUES ('Olsztyn', 53.770226, 20.490189);
INSERT INTO City (name, lat, lon) VALUES ('Opole', 50.671062, 17.926126);

-- Insert air metrics into the AirMetric table
INSERT INTO AirMetric (name) VALUES ('co');
INSERT INTO AirMetric (name) VALUES ('no');
INSERT INTO AirMetric (name) VALUES ('no2');
INSERT INTO AirMetric (name) VALUES ('o3');
INSERT INTO AirMetric (name) VALUES ('so2');
INSERT INTO AirMetric (name) VALUES ('pm2_5');
INSERT INTO AirMetric (name) VALUES ('pm10');
INSERT INTO AirMetric (name) VALUES ('nh3');
