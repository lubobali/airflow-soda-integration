Airflow + Soda Integration for Data Quality Checks

This project integrates Apache Airflow with Soda CLI, an open-source data quality tool, 
to automatically run data quality checks on your database using a DAG pipeline.

🧪 What Is Soda and How Are We Using It Here?

Soda (short for Schema-on-Demand Analytics) is a tool that helps data teams detect problems in their data pipelines early, 
such as missing values, duplicate entries, or row count anomalies. Normally, Soda is run manually or through its cloud UI,
but in this project, we're using Soda CLI—a command-line interface—to automatically run checks as part of a scheduled Airflow workflow.

By integrating Soda CLI with Airflow, we:

Schedule data quality checks to run automatically

Detect issues like empty tables or missing values

Maintain logs of each scan for audit or debugging

Run the entire pipeline in a local Docker environment

🔄 What This Pipeline Does

The pipeline is built as an Airflow DAG (Directed Acyclic Graph), and it automates the following steps:

Start the DAG manually or via schedule.

Run Soda CLI from inside the container using the BashOperator.

Soda scans your PostgreSQL table, using rules defined in the checks.yml file.

Logs are stored and accessible through the Airflow UI.

Example Soda checks:

yaml
Copy
Edit
checks for dag_run:
  - row_count > 0
  - missing_count(dag_id) = 0
  - missing_count(execution_date) = 0
  - duplicate_count(run_id) = 0
    
🧱 Project Structure
.
├── dags/
│   └── soda_scan_dag.py        # DAG that calls Soda CLI using BashOperator
├── soda/
│   ├── checks.yml              # Data quality rules
│   └── configuration.yml       # Connection details for Soda CLI
├── docker-compose.yml          # Multi-service setup: Airflow, Postgres, Soda
├── Dockerfile.airflow          # Docker setup for Airflow
└── logs/                       # Logs from Airflow runs

🛠 How to Set It Up Locally (Full Instructions)
Here’s a step-by-step to replicate what I did to make this work:

Clone the Repo

git clone https://github.com/lubobali/airflow-soda-integration.git
cd airflow-soda-integration

Update Submodules (if needed)

git submodule update --init --recursive
Make sure Docker is installed and running

Start the Airflow Environment
Build and start all services (scheduler, webserver, PostgreSQL):

docker compose up -d --build
Access the Airflow UI
Go to http://localhost:8090
Use airflow / airflow as login credentials.

Run the DAG

Click on the DAG soda_scan_dag

Trigger a manual run

View logs to see the Soda CLI scan output

💬 Notes
Airflow uses the LocalExecutor

Logs are persisted in ./logs

Soda CLI connects to a local PostgreSQL database running in Docker

Scans run inside the container with the volume /soda mounted

📌 Requirements
Docker + Docker Compose

Internet connection to pull base images

Basic understanding of Airflow and command-line tools

🔍 What Else Can You Check?
Soda allows flexible, human-readable rules to be written in YAML. 
You can add more data quality checks by editing soda/checks.yml. Here are some useful examples:

checks for your_table_name:
  - min(age) >= 0                     # No negative ages
  - max(score) <= 100                # Score shouldn't exceed 100
  - avg(price) > 0                   # Price should be greater than zero
  - invalid_count(country) = 0       # All values in 'country' should match a predefined list
  - schema:
      warn:
        - column name must match regex ^[a-z_]+$  # Enforce snake_case column names

These kinds of checks can help you:

Catch data entry errors (like negative values or invalid strings)

Track schema drift or renamed fields

Monitor business logic violations

Keep your pipeline clean and production-grade

To activate them, simply update the checks.yml file and rerun the DAG—no extra code needed!
