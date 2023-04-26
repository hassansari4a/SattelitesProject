from prefect_dbt.cloud import DbtCloudJob, DbtCloudCredentials
from prefect_dbt.cloud.jobs import trigger_dbt_cloud_job_run_and_wait_for_completion
from prefect import flow, task
import configparser

@flow()
def run_dbt_job(job_id: str) -> None:
    dbt_cloud_credentials = DbtCloudCredentials.load("satellite-dbt-credentials")
    
    result = trigger_dbt_cloud_job_run_and_wait_for_completion(
        dbt_cloud_credentials=dbt_cloud_credentials,
        job_id=job_id
    )
    
    print(result)  

@flow()
def dbt_transformations() -> None:
    config = configparser.ConfigParser()
    config.read('config.ini')

    run_dbt_job(config['dbt']['job-id'])
                
if __name__ == '__main__':
    dbt_transformations()
