Airflow + Soda Integration Demo

This project demonstrates how to integrate Soda data quality checks into an Apache Airflow DAG pipeline, using Postgres as the sample data source.

🔧 Tools Used

Apache Airflow (via Docker Compose)

Soda CLI for data quality checks

Postgres (sample data source)

🚀 Current Status

✅ Fully working Airflow DAG that runs a Soda scan on a dataset
✅ Docker-based setup for local development and testing
✅ Automated data quality validation as part of the Airflow pipeline

📁 Project Structure

bash
Copy
Edit
├── dags/
│   └── soda_scan_dag.py           # Airflow DAG to run Soda scan
├── soda/
│   ├── config.yml                 # Soda CLI configuration
│   ├── scan_checks.yml           # Data quality checks
│   └── README.md                 # Soda setup description (optional)
├── docker-compose.yml            # Docker Compose setup for Airflow + Postgres
└── README.md                     # Project overview and setup instructions
⚙️ Setup Instructions
Clone the repo

bash
Copy
Edit
git clone https://github.com/lubobali/airflow-soda-integration.git
cd airflow-soda-integration
Start the Airflow + Postgres stack

bash
Copy
Edit
docker compose up -d
Access Airflow UI
Open your browser and go to:
http://localhost:8090

🧪 Run the Soda Scan DAG

In the Airflow UI, find the DAG named soda_scan_example

Trigger it manually or wait for the scheduled run

Monitor the task logs to view Soda scan output

✅ What Happens Behind the Scenes

The DAG uses a BashOperator to execute a Soda CLI command

Soda connects to the Postgres database defined in config.yml

Soda runs data quality checks from scan_checks.yml

Results are shown directly in the Airflow task logs

📖 Notes
Postgres runs with default credentials (airflow/airflow)

You can update config.yml if your database changes

Add more checks to scan_checks.yml as needed

🧠 Requirements

Docker installed locally

No other dependencies — everything runs inside containers
