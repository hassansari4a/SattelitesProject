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
