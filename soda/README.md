# Soda Configurations

This folder contains the configuration files used by Soda Core for data quality checks.

- `config.yml` — Defines the data source connection settings for Soda to connect to the Postgres database inside Docker.
- `scan_checks.yml` — Contains the data quality checks applied to the `dag_run` table in Airflow.
- `README.md` — This file, providing context for the folder.

These files are mounted into the Airflow container and executed as part of the DAG.
