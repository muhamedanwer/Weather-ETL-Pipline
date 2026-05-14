import pandas as pd 


def transform(received_data: dict, city: str | None = None) -> pd.DataFrame:
    """Transform hourly payload into a DataFrame."""
    
    if "hourly" not in received_data or not isinstance(received_data["hourly"], dict):
        raise ValueError("Input payload must contain an 'hourly' dict from the Open-Meteo response.")

    hourly = received_data["hourly"]
    df = pd.DataFrame(hourly)

    if "time" not in df.columns:
        raise ValueError("Hourly payload must include a 'time' field.")

    df["time"] = pd.to_datetime(df["time"])

    if city is not None:
        df["city"] = city

    return df


if __name__ == "__main__":
    from extract import extract_all_cities

    data = extract_all_cities()
    for city_name, payload in data.items():
        print(city_name)
        print(transform(payload, city_name).head(3))