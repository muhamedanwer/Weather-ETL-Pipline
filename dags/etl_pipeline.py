from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.sql import SQLExecuteQueryOperator
from datetime import datetime, timedelta
from etl.extract import extract_all_cities
from etl.transform import transform
from sql.weather_table import weather_table
from etl.load import  load



pipeline_dag = DAG(
    "weather_etl_pipeline",
    default_args={
        "owner": "Anwar",
        "depends_on_past": False,
        "start_date": datetime(2024, 6, 1),
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    schedule_interval="0 * * * *",  # Run every hour
)

t1 = PythonOperator(
    task_id="extract_data",
    python_callable=extract_all_cities,
    dag=pipeline_dag,
)

t2 = PythonOperator(
    task_id="transform",
    pythoncallable=transform,
    op_kwargs={"received_data": t1.output},
    dag=pipeline_dag,       
)  

t3 = SQLExecuteQueryOperator(
    task_id="create_table",
    sql=weather_table,
    conn_id="postgres_default",
    dag=pipeline_dag,
)

t4 = PythonOperator(
    task_id="load_data",
    python_callable=load,
    op_kwargs={"df": t2.output},
    dag=pipeline_dag,
)       


t1 >> t2 >> t3 >> t4 