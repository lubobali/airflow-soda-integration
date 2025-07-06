from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='soda_scan_example',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    max_active_runs=1
) as dag:

    soda_scan = BashOperator(
        task_id='run_soda_scan',
        bash_command=(
            "export PATH=$PATH:/home/airflow/.local/bin && "
            "/home/airflow/.local/bin/soda scan -d local_postgres "
            "-c /usr/local/soda/config.yml "
            "/usr/local/soda/scan_checks.yml"
        )
    )
