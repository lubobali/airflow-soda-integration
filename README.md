Airflow + Soda Integration Demo
This project demonstrates how to integrate Soda data quality checks into an Apache Airflow DAG pipeline, using Postgres as the sample data source.

🔧 Tools Used
Apache Airflow (via Docker Compose)

Soda CLI for data quality checks

Postgres (sample data source)

🚀 Current Status
Fully working DAG that runs a Soda scan on a dataset

Docker-based setup for local development and testing

Automated data quality validation as part of the Airflow pipeline

📁 Project Structure
bash
Copy
├── dags/
│   └── soda_scan_dag.py            # Airflow DAG to run Soda scan
├── soda/
│   ├── config.yml                  # Soda CLI configuration
│   ├── scan_checks.yml             # Data quality checks definitions
│   └── README.md                   # Soda setup description
├── docker-compose.yml              # Docker Compose setup for Airflow + Postgres
└── README.md                      # Project description and instructions
⚙️ Setup Instructions
Clone this repo

bash
Copy
git clone https://github.com/lubobali/airflow-soda-integration.git
cd airflow-soda-integration
Start the Airflow + Postgres stack

bash
Copy
docker compose up -d
Access the Airflow Web UI
Open your browser and go to:
http://localhost:8090

Trigger the DAG

Find the DAG named soda_scan_example in the Airflow UI

Trigger it manually or wait for the scheduled run

Monitor the run

Check the task logs in the Airflow UI

Look for the Soda scan output, which should report passed checks

✅ What Happens
The DAG executes a BashOperator task that runs the Soda CLI command

Soda connects to the Postgres database

It performs data quality checks defined in scan_checks.yml

Results are shown in Airflow task logs

📖 Additional Notes
The Postgres service runs with default credentials set in soda/config.yml

Update the config if your database setup changes

Extend scan_checks.yml to add more data quality rules as needed
