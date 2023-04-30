from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket
import os

GCS_bucket_name = "sat_data_lake_idyllic-aspect-382707"  # insert your GCS bucket name
service_account_credentials = os.environ['SERVICE_ACCOUNT_CREDENTIALS_GCP']


credentials_block = GcpCredentials(
    service_account_info= service_account_credentials
)
credentials_block.save("sat-gcp-credendials", overwrite=True)

bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("sat-gcp-credendials"),
    bucket=GCS_bucket_name,
)
bucket_block.save("satproject-storage-bucket", overwrite=True)