import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]


@click.command()
@click.option("--pg-user", default="root")
@click.option("--pg-pass", default="root")
@click.option("--pg-host", default="localhost")
@click.option("--pg-port", default=5432, type=int)
@click.option("--pg-db", default="ny_taxi")
@click.option("--target-table", default="yellow_taxi_trips")
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):

    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"
    file_name = "yellow_tripdata_2021-01.csv.gz"

    print("Connecting to Postgres...")

    engine = create_engine(
        f"postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}"
    )

    print("Reading CSV in chunks...")

    df_iter = pd.read_csv(
        url + file_name,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=1000
    )

    first_chunk = next(df_iter)
    print("First chunk rows:", len(first_chunk))

    print("Creating table schema...")
    first_chunk.head(0).to_sql(
        name=target_table,
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Inserting first chunk...")
    first_chunk.to_sql(
        name=target_table,
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    total_rows = len(first_chunk)

    for df_chunk in tqdm(df_iter):
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            index=False,
            method="multi"
        )
        total_rows += len(df_chunk)

    print("Ingestion complete. Total rows inserted:", total_rows)


if __name__ == "__main__":
    run()