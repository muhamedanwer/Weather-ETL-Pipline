import sqlalchemy 
import pandas as pd

        
        
def load(df: pd.DataFrame):
    """Load the DataFrame into the weather_data table."""
    engine = sqlalchemy.create_engine("docker-postgres:5432/weather_db")    
    df.to_sql("weather_data", con=engine, if_exists="append", index=False)
    
    