# Docker-workshop
# Docker Workshop: NYC Taxi Data Pipeline

## Overview

This project builds a complete local data engineering workflow using Docker, PostgreSQL, pgAdmin, and Python.

The pipeline:

* Downloads NYC Yellow Taxi trip data
* Reads the data in chunks using Pandas
* Loads the data into PostgreSQL
* Uses Docker Compose for orchestration
* Uses pgAdmin for database management and querying

---

# Tech Stack

* Python
* Pandas
* PostgreSQL 18
* SQLAlchemy
* psycopg
* Docker
* Docker Compose
* pgAdmin 4
* uv package manager

---

# Project Structure

```text
Docker-workshop/
│
├── docker-compose.yaml
├── README.md
│
├── pipeline/
│   ├── Dockerfile
│   ├── ingest_data.py
│   ├── pyproject.toml
│   └── uv.lock
```

---

# Dataset

Source:

NYC TLC Yellow Taxi Trip Records

File used:

```text
yellow_tripdata_2021-01.csv.gz
```

Dataset URL:

```text
https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz
```

---

# Features

* Containerized PostgreSQL database
* Containerized pgAdmin UI
* Dockerized ingestion pipeline
* Chunk-based CSV ingestion
* Automatic schema creation
* Bulk insertion into PostgreSQL
* SQL querying with pgAdmin
* Docker Compose orchestration

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/Wanjala-B/Docker-workshop.git

cd Docker-workshop
```

---

## 2. Build the Ingestion Image

```bash
docker build -t taxi_ingest:v001 ./pipeline
```

---

## 3. Start Services

```bash
docker compose up -d
```

This starts:

* PostgreSQL
* pgAdmin
* Docker network

---

## 4. Run Data Ingestion

```bash
docker compose run --rm ingest
```

---

# pgAdmin Access

Open the forwarded browser URL for port 8085.

Login credentials:

```text
Email: admin@admin.com
Password: root
```

---

# Configure PostgreSQL Server in pgAdmin

## General Tab

```text
Name: ny_taxi
```

## Connection Tab

```text
Host: pgdatabase
Port: 5432
Database: ny_taxi
Username: root
Password: root
```

---

# Example SQL Queries

## Count Total Rows

```sql
SELECT COUNT(*)
FROM yellow_taxi_trips;
```

---

## Preview Data

```sql
SELECT *
FROM yellow_taxi_trips
LIMIT 10;
```

---

## Top Pickup Locations

```sql
SELECT "PULocationID", COUNT(*) AS trips
FROM yellow_taxi_trips
GROUP BY "PULocationID"
ORDER BY trips DESC
LIMIT 10;
```

---

# Docker Commands

## View Running Containers

```bash
docker ps
```

## Stop Containers

```bash
docker compose down
```

## Remove Containers and Volumes

```bash
docker compose down -v
```

## View Logs

```bash
docker compose logs
```

---

# Ingestion Pipeline

The ingestion script:

1. Connects to PostgreSQL
2. Reads the CSV file in chunks
3. Creates the database schema
4. Inserts records in batches
5. Loads the complete dataset into PostgreSQL

Chunk processing helps reduce memory usage during ingestion.

---

# Future Improvements

* Add Apache Airflow orchestration
* Add dbt transformations
* Add automated data quality checks
* Add analytics dashboards
* Add Terraform deployment
* Deploy pipeline to cloud infrastructure

---

# Author

Benson Irungu MSC


GitHub:

[https://github.com/Wanjala-B](https://github.com/Wanjala-B)

