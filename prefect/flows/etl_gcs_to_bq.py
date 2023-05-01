from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
import os

import schema

@task(retries = 3)
def extract_from_gcs() -> Path:
    gcs_path = f"data/satcatdata/satcatdata.csv"
    gcs_block = GcsBucket.load("satproject-storage-bucket")
<<<<<<< HEAD
    local_path = path = os.path.abspath('/app/data/tmp')
=======
    local_path = os.path.abspath('/app/data/tmp')
>>>>>>> 6468b9b973dd54b26cfffd6f3cd12fd61693c2f8
    gcs_block.get_directory(from_path = gcs_path, local_path = local_path)
    return Path(f"{local_path}/{gcs_path}")

@task()
def read_data(path: Path) -> pd.DataFrame:
    """Data Loading into Pandas Dataframe"""
    df = pd.read_csv(path, compression="gzip")
    df.drop('Unnamed: 0', axis=1, inplace=True)
    print(df.head(5))
    return df

@task()
def write_bq(df: pd.DataFrame, table_schema: list[dict[str, str]]) -> None:
    """Write Dataframe into BigQuery"""
<<<<<<< HEAD
    gcp_credentials_block = GcpCredentials.load("sat-gcp-credendials")
=======
    gcp_credentials_block = GcpCredentials.load("sat-gcp-credentials")
>>>>>>> 6468b9b973dd54b26cfffd6f3cd12fd61693c2f8

    df.to_gbq(
        destination_table= "sat_data_all.satcatdata",
        project_id= "idyllic-aspect-382707",
        credentials= gcp_credentials_block.get_credentials_from_service_account(),
        chunksize= 500_000,
        table_schema= table_schema,
        if_exists= "append"
    )

@flow()
def etl_gcs_to_bq():
    """Main ETL flow to load data into Big Query"""
    table_schema = schema.schema
    path = extract_from_gcs()
    print(path)
    df= read_data(path )
    write_bq(df, table_schema)

if __name__ == "__main__":
    etl_gcs_to_bq()