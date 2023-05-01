<<<<<<< HEAD
from prefect_dbt.cloud import DbtCloudCredentials, DbtCloudJob
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

DbtCloudCredentials(
    api_key = config['dbt']['api-key'],
    account_id = config['dbt']['account-id']
).save("satellite-dbt-credentials")

# dbt_cloud_credentials = DbtCloudCredentials.load("satellite-dbt-credentials")
# dbt_cloud_job = DbtCloudJob.load(
#     dbt_cloud_credentials=dbt_cloud_credentials,
#     job_id = config['dbt']['job-id']
# )
=======
from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket
import os
import json

GCS_bucket_name = "sat_data_lake_idyllic-aspect-382707"  # insert your GCS bucket name
 
file = open(os.path.abspath('/app/credentials.json'))
service_account_credentials = json.load(file)

credentials_block = GcpCredentials(
    service_account_info= service_account_credentials
)
credentials_block.save("sat-gcp-credentials", overwrite=True)

bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("sat-gcp-credentials"),
    bucket=GCS_bucket_name,
)
bucket_block.save("satproject-storage-bucket", overwrite=True)
>>>>>>> 6468b9b973dd54b26cfffd6f3cd12fd61693c2f8
