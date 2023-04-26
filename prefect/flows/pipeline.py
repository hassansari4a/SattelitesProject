from prefect import flow, task

# from .prefect.flows import etl_gcs_to_bq
# from .prefect.flows import etl_local_to_gcs

import etl_gcs_to_bq
import etl_local_to_gcs


@flow()
def data_to_gcs() -> None:
    etl_local_to_gcs.etl_web_to_gcs()
    return 

@flow()
def data_to_bq() -> None:
    etl_gcs_to_bq.etl_gcs_to_bq()

@flow()
def pipeline():
    data_to_gcs()
    data_to_bq()
    

if __name__ == '__main__':
    pipeline()