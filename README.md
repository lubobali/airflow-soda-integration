# Airflow + Soda Integration Demo

This demo project shows how to integrate **Soda** for data quality checks into an **Apache Airflow** DAG pipeline.

🔧 Tools used:
- Apache Airflow (via Docker Compose)
- Soda CLI
- Postgres (as the sample data source)

🚀 Coming soon:
- A working DAG that runs a Soda scan on a dataset.
- Docker-based setup for local development and testing.

🛠 Status: In progress (initial setup complete)

📁 Project structure:
📁 Project structure:

├── dags/
│   └── soda_scan_dag.py         # Airflow DAG to run Soda scan
├── soda/
│   ├── config.yml               # Soda CLI configuration
│   ├── scan_checks.yml          # Data quality checks
│   └── README.md                # Description of Soda setup
├── docker-compose-LocalExecutor.yml  # Docker setup for Airflow + Postgres
└── README.md                    # Project description and instructions


