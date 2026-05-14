BASE_URL = "https://historical-forecast-api.open-meteo.com/v1/forecast"

PARAMS = {}

CITIES = {
    "Cairo": {"latitude": 30.062, "longitude": 31.2497, "country": "EG"},
    "Alexaderia": {"latitude": 31.2018, "longitude": 29.9158, "country": "EG"},
    "Mansoura": {"latitude": 31.0364, "longitude": 31.3807, "country": "EG"},
    "Tunnamil": {"latitude": 30.836, "longitude": 31.2617, "country": "EG"},
}

START_DATE = "2026-04-21"
END_DATE = "2026-05-05"

TIMEZONE = "Africa/Cairo"

LOGS_PATH = "logs/ETL.log"


