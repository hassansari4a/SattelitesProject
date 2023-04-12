from pathlib import Path

from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket

from ...spark.extract_from_api import * 

@task(retries=3)
def get_satcat_data():
    """Read Taxi Data from Web into Pandas Dataframe"""
    download_data()
    df = read_data()
    return df

@task(log_prints = True)
def clean_df(df):
    return clean_data(df)

@task(log_prints = True)
def write_local(df) -> Path:
    """Write DataFrame out as a parquet file"""
    path = write_data(df) 
    # pathdir = Path(f"data/{color}")
    # if not os.path.exists(pathdir):
    #     os.makedirs(pathdir)
    # path = Path(f"data/{color}/{dataset_file}.parquet")
    # df.to_parquet(path, compression="gzip")
    return path

@task(log_prints = True)
def write_gcs(path: Path) -> None:
    """Uploading local parquet file to GCS"""
    gcp_block = GcsBucket.load("satcatgcs")
    gcp_block.upload_from_path( # type: ignore
        from_path=f'{path}/*.parquet',
        to_path='data/satcatdata'
    )
    return

@flow()
def etl_web_to_gcs() -> None:
    """The Main ETL Function"""

    df = get_satcat_data()
    df = clean_df(df)
    path = write_local(df)
    write_gcs(path)

if __name__ == "__main__":
    etl_web_to_gcs()
