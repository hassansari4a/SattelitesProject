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