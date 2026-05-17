

-- Normalize weather storage into entities and relationships for ERD compliance.
-- city: stores each location once.
-- weather_data: stores hourly observations linked to a city.

CREATE TABLE IF NOT EXISTS city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    country CHAR(2),
    latitude NUMERIC(8,5),
    longitude NUMERIC(8,5),
    timezone VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL REFERENCES city(id) ON DELETE CASCADE,
    observation_time TIMESTAMP NOT NULL,
    temperature_2m REAL NOT NULL,
    rain REAL NOT NULL,
    relative_humidity_2m REAL NOT NULL,
    dew_point_2m REAL NOT NULL,
    apparent_temperature REAL NOT NULL,
    wind_speed_10m REAL NOT NULL,
    precipitation_probability REAL NOT NULL,
    vapour_pressure_deficit REAL NOT NULL,
    visibility REAL NOT NULL,
    cloud_cover REAL NOT NULL,
    wind_direction_10m REAL NOT NULL,
    UNIQUE (city_id, observation_time)
);




