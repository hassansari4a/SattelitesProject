from pathlib import Path
from spacetrack import SpaceTrackClient
import pandas as pd
import configparser
import subprocess
import os
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket


@task(log_prints = True, retries=3)
def get_satcat_data(username: str, password: str) -> pd.DataFrame:
    """Read SATCAT Data from Web into Pandas Dataframe"""
    st = SpaceTrackClient(username, password)
    
<<<<<<< HEAD
    csvfile = st.satcat(format='csv', limit=1000)
=======
    csvfile = st.satcat(format='csv')
>>>>>>> 6468b9b973dd54b26cfffd6f3cd12fd61693c2f8
    with open('satcatdata.csv', 'w') as my_file:
        my_file.write(csvfile)
    df = pd.read_csv('satcatdata.csv')
    return df

@task(log_prints = True)
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(['COMMENT', 'COMMENTCODE', 'RCSVALUE', 'RCS_SIZE'], axis=1)
    df['LAUNCH'] = pd.to_datetime(df['LAUNCH'])
    df['DECAY'] = pd.to_datetime(df['DECAY'])
    return df

@task(log_prints = True)
def write_local(df: pd.DataFrame) -> Path:
    print(subprocess.check_output("pwd", shell=True).decode().strip())
    # path = Path('.../app/data/satcatdata/satcatdata.csv')
    path = os.path.abspath('/app/data/satcatdata/satcatdata.csv')
    df.to_csv(path, compression='gzip')
    return path

@task(log_prints = True)
def write_gcs(path: Path) -> None:
    """Uploading local parquet file to GCS"""
    gcp_block = GcsBucket.load("satproject-storage-bucket")
    gcp_block.upload_from_path( # type: ignore
        from_path = path,
        to_path = 'data/satcatdata.satcatdata.csv'
    )
    return

@flow()
def etl_web_to_gcs() -> None:
    """The Main ETL Function"""
    config = configparser.ConfigParser()
<<<<<<< HEAD
    config.read('config.ini')
=======
    config.read(os.path.abspath('/app/config.ini'))
>>>>>>> 6468b9b973dd54b26cfffd6f3cd12fd61693c2f8

    df = get_satcat_data(config['spacetrack']['username'], config['spacetrack']['password'])
    # df = pd.read_csv('prefect/flows/satcatdata.csv')
    df = clean_df(df)
    path = write_local(df)
    write_gcs(path)

if __name__ == "__main__":
    etl_web_to_gcs()
