#!/bin/sh
set -e

# Log in to Prefect Cloud
prefect cloud login --key pnu_YTF0qFmhT9pbQqjBvpDH2LUuuftxW7265cTN

# Run the CMD specified in the Dockerfile
exec "$@"