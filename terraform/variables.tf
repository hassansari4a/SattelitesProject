locals {
    data_lake_bucket = "sat_data_lake"
}

variable "project" {
    description = "Your gcp project id"
    default = "idyllic-aspect-382707"
    type = string
    
}

variable "region" {
    description = "Region for GCP resources. asia-south2(delhi)"
    default = "asia-south2"
    type = string
}

variable "bucket_name" {
    description = "The name of the GCS bucket. Must be globally unique"
    default = ""
}

variable "storage_class" {
    description = "Storage class type for your bucket. Check official docs for more info"
    default = "STANDARD"
}

variable "BQ_DATASET" {
    description = "BigQuery Dataset that raw data (from GCS) wil be written to"
    type = string
    default = "sat_data_all"
}

variable "TABLE_NAME" {
    description = "BigQuery Table"
    type = string
    default = "satcat"
}