# Weather ETL Pipeline

ETL pipeline that fetches historical weather data from the [Open-Meteo API](https://open-meteo.com/), transforms it, and loads it into a PostgreSQL database. Orchestrated with Apache Airflow and containerized with Docker.

## Architecture

```
Open-Meteo API  →  Extract  →  Transform  →  Load  →  PostgreSQL
                                      ↓
                                Airflow DAG
```

## Project Structure

```
├── etl/                   # ETL modules
│   ├── extract.py         # Fetches hourly weather data from Open-Meteo
│   ├── transform.py       # Converts API responses into DataFrames
│   └── load.py            # Loads data into PostgreSQL
├── dags/
│   └── etl_pipeline.py    # Airflow DAG definition
├── sql/
│   └── weather_table.sql  # Database schema
├── notebooks/             # Jupyter notebooks for analysis
├── data/                  # Raw/processed data storage
├── logs/                  # Application logs
├── config.py              # Cities, API params, date ranges
├── main.py                # CLI entry point
├── requirements.txt
├── docker-compose.yml     # PostgreSQL service
└── .env                   # Environment variables (not tracked)
```

## Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Apache Airflow (if running outside Docker)

## Setup

1. **Clone and create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure cities and dates**

   Edit `config.py` to set your desired cities, date range, and timezone.

3. **Start PostgreSQL**

   ```bash
   docker compose up -d
   ```

4. **Create the database table**

   ```bash
   psql -h localhost -U weather_user -d weather_db -f sql/weather_table.sql
   ```

## Usage

### Run manually

```bash
python main.py
```

### Run via Airflow

The DAG in `dags/etl_pipeline.py` schedules the pipeline to run hourly. Deploy it to your Airflow instance's `dags/` directory.

## Data

### Source

[Open-Meteo Historical Forecast API](https://open-meteo.com/en/docs/historical-weather-api) — no API key required.

### Extracted fields (hourly)

`temperature_2m`, `rain`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `wind_speed_10m`, `precipitation_probability`, `vapour_pressure_deficit`, `visibility`, `cloud_cover`, `wind_direction_10m`

### Schema

The database is modeled with two related entities:

- `city`: stores each location once
- `weather_data`: stores hourly observations linked to a city

| Table | Columns |
|-------|---------|
| `city` | `id`, `name`, `country`, `latitude`, `longitude`, `timezone` |
| `weather_data` | `id`, `city_id`, `observation_time`, `temperature_2m`, `rain`, `relative_humidity_2m`, `dew_point_2m`, `apparent_temperature`, `wind_speed_10m`, `precipitation_probability`, `vapour_pressure_deficit`, `visibility`, `cloud_cover`, `wind_direction_10m` |

## Customization

- **Cities**: Add entries to the `CITIES` dict in `config.py`
- **Weather variables**: Modify the `hourly` parameter in `etl/extract.py`
- **Transformation logic**: Edit `etl/transform.py`
- **Analysis**: Use `notebooks/` for exploratory work
- **Dashboard**: Connect Streamlit to the PostgreSQL database

## License

MIT
