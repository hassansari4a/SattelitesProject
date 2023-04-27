# Satellite Project

This is an end-to-end data engineering project, This project uses [Space-track](https://www.space-track.org/)'s Satellite Catalog dataset.

## Problem Description

The purpose of this project is to make an end-to-end data pipeline that extracts satellite data from [Space-track](https://www.space-track.org/)'s web API and loads this data in Google Cloud Storage and Big Query, apply Kimbal's Dimensional Modeling(Fact and Dimension tables) to the data using dbt and visualize the transformed data using Looker Studio.

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
