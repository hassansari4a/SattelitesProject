
# SATELLITEX


This is an end-to-end data engineering project, This project uses [Space-track](https://www.space-track.org/)'s Satellite Catalog dataset.

## Problem Description

The purpose of this project is to make an end-to-end data pipeline that extracts satellite data from [Space-track](https://www.space-track.org/)'s web API and loads this data in Google Cloud Storage and Big Query, apply Kimball Dimensional Modeling(Fact and Dimension tables) to the data using dbt and visualize the transformed data using Looker Studio.

## Dashboard
Check out the interactive dashboard [here](https://lookerstudio.google.com/reporting/9cb38815-937c-4bf6-909d-50074cb9aa0d).
![satellitex_dashboard.png](/images/satellitex_dashboard.png)


## Technology Stack

The following technologies are used to build this project.
- Google Cloud Storage - Data Lake
- Big Query - Data Warehouse
- Terraform - Infrastructure as Code tool
- Prefect - Workflow Orchestration
- dbt - Transformation and Data modeling
- Looker Studio - Visualization tool

## Data Pipeline Architecture
![data_pipeline_architecture.png](/images/Data_Pipeline_Architechture_small.png)

## Data Dictionary

| Column | Description |
|--|--|
| sat_id | Surrogate key that combines `intldes_id` and `norad_id` |
| intldes_id| International Designator: Also known as COSPAR designation or NSSDC ID, this is one format for uniquely identifying an object. |
| norad_id| Sequential number assigned by the US Space Force as objects are cataloged. |
| satellite_name| Name of the satellite/object |
| object_id | The CCSDS's name for International Designator |
| object_name | Name of the satellite/object |
| object_number | The same as norad_id. Synonyms: Satellite Catalog Number, NORAD_CAT_ID, Object Number |
| object_type | Classification of the object as **PAYLOAD**, **ROCKET BODY**, **DEBRIS** OR **UNKNOWN**  |
| country | The nation or group that has responsibility for an object |
| country_id | Abbreviated form of `country` |
| geo_code | Country codes conforming to the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) format |
| launch_date | Date object was launched in *YYYY-MM-DD* format |
| decay_date | Date object reentered the earth's atmosphere in *YYYY-MM-DD* format |
| is_orbiting | Takes values **Y** or **N** to represent the object's orbiting status|
| launch_site | Location from where the object was launched |
| launch_num | A three-letter code representing the sequential identifier of a piece in a launch |
| launch_piece | Part of the satellite that connects it to the launch vehicle |
| launch_year | Year object was launched |
| period | The number of minutes an object takes to make one full orbit |
| apogee | Point in the orbit where an Earth satellite is farthest from the Earth. Units are kilometers |
| inclination | The angle between the equator and the orbit plane |
| perigee | Point in the orbit where an Earth satellite is closest to the Earth. Units are kilometers |
| file | The unique identifying number of the source file for a particular object's data - higher numbers are more recent uploads |

## Prerequisites
- [Docker](https://www.docker.com/)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install#installation_instructions)
- [Terraform](https://developer.hashicorp.com/terraform/downloads?product_intent=terraform)
- 

## Reproduce it yourself

1. Clone this repository in your local environment
```bash
git clone https://github.com/hassansari4a/SattelitesProject.git
```
2. Set up your Google Cloud environment
	- Create a GCP Project
	- Configure Identity and Access Management (IAM) for the service account, giving it the following privileges:
		- Viewer
		- Storage Admin
		- Storage Object Admin
		- BigQuery Admin
	- Create a key and download the JSON credentials
	- Let the  [environment variable point to your GCP key](https://cloud.google.com/docs/authentication/application-default-credentials#GAC), authenticate it and refresh the session token
```bash
export GOOGLE_APPLICATION_CREDENTIALS=<path_to_your_credentials.json>
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
gcloud auth application-default login
```
3. Setup your infrastructure
	- Change the [variables.tf](/terraform/variables.tf) file with your corresponding variables, I would recommend to leave the name of the dataset, table and bucket as they are; otherwise you need to change them in the prefect flows and dbt.
	- Run the following Terraform commands:
	```bash
	terraform init
	terraform plan
	terraform apply
	```
4. Setup your orchestration
	-	Sign-up for Prefect Cloud and create a workspace [here](https://app.prefect.cloud/auth/login)
5. Set up dbt

6. [Create environment files](/examples/README.md)

7. Build your docker image:
```bash
docker build --build-arg PREFECT_CLOUD_API_KEY=$(cat .env | grep PREFECT_CLOUD_API_KEY | cut -d= -f2) \
--build-arg PREFECT_WORKSPACE=$(cat .env | grep PREFECT_WORKSPACE | cut -d= -f2) \
--build-arg SERVICE_ACCOUNT_CREDENTIALS_GCP=$(cat .env | grep SERVICE_ACCOUNT_CREDENTIALS_GCP | cut -d= -f2) \
-t <your-image-name>:<tag> .
```
8. Run the docker image:
```bash
docker run --platform linux/amd64 -it <your-image-name>:<tag>
```
