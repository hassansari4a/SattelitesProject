terraform {
    required_version = ">= 1.0"
    backend "local" {}
    required_providers {
        google = {
        source = "hashicorp/google"
        }
    }
}

provider "google" {
    project = var.project
    region = var.region

}

resource "google_storage_bucket" "data-lake-bucket" {
    name = "${local.data_lake_bucket}_${var.project}"
    location = var.region

    storage_class = var.storage_class
    uniform_bucket_level_access = true
    
    versioning {
      enabled = true
    }

    lifecycle_rule {
        action {
          type= "Delete"
        }
        condition {
          age = 30 //days
        }
    }

    force_destroy = true
}

resource "google_bigquery_dataset" "dataset" {
    dataset_id = var.BQ_DATASET
    project = var.project
    location = var.region
<<<<<<< HEAD
=======
}

resource "google_bigquery_dataset" "production" {
    dataset_id = "production"
    project = var.project
    location = var.region
}

resource "google_bigquery_dataset" "staging" {
    dataset_id = "staging"
    project = var.project
    location = var.region
>>>>>>> 6468b9b973dd54b26cfffd6f3cd12fd61693c2f8
}