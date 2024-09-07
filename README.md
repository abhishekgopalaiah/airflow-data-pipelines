# Airflow Data Pipelines

This repository contains Apache Airflow DAGs created for various data engineering tasks. The project structure was generated using the Astro CLI.

### Prerequisites

- Docker
- Astro CLI


## Project Structure
```
├───.astro
├───dags
│   └───__pycache__
├───include
│   ├───data
│   │   ├───metabase
│   │   └───minio
│   │       └───.minio.sys
│   │           ├───buckets
│   │           │   ├───.bloomcycle.bin
│   │           │   └───.usage.json
│   │           ├───config
│   │           │   ├───config.json
│   │           │   └───iam
│   │           │       └───format.json
│   │           ├───multipart
│   │           ├───pool.bin
│   │           └───tmp
│   │               └───.trash
│   └───helpers
│       └───__pycache__
├───plugins
├───spark
│   ├───master
│   ├───notebooks
│   │   └───stock_transform
│   └───worker
└───tests
    └───dags

```
- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one 
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432.

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.


### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhishekgopalaiah/airflow-data-pipelines
   cd your-repo-name


2. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

3. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432.

4. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.