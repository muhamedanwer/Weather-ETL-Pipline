import requests
import logging
import sys
import os


sys.path.append(os.getcwd())
from config import BASE_URL, CITIES, START_DATE, END_DATE, TIMEZONE, LOGS_PATH


logging.basicConfig(level=logging.INFO, filename=LOGS_PATH)


def extract(url, params):

    try:
        response = requests.get(url=url, params=params)
        response.raise_for_status()
        logging.info("SUCCESSFULLY RECEIVED DATA FORM SERVICE.")

    except requests.exceptions.Timeout:
        logging.error("Timeout while connecting to service.")
        raise RuntimeError("service timeout.")

    except ConnectionError:
        logging.error("connection error while accessing API.")
        raise ConnectionError("cannot connect to service.")

    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error : {e}")
        raise RuntimeError(f"HTTP Error : {e}")

    return response.json()


def extract_all_cities():
    result = {}
    for city in CITIES:
        params = {
        "latitude": CITIES[city]["latitude"],
        "longitude": CITIES[city]["longitude"],
        "start_date": START_DATE,
        "end_date": END_DATE,
        "hourly": "temperature_2m,rain,relative_humidity_2m,dew_point_2m,apparent_temperature,wind_speed_10m,precipitation_probability,vapour_pressure_deficit,visibility,cloud_cover,wind_direction_10m",
        "timezone": TIMEZONE,
}
        result[city] = extract(BASE_URL, params=params)

    return result


if __name__ == "__main__":
    print(extract_all_cities())