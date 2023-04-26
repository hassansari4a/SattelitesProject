#!/bin/bash
prefect cloud login --key $PREFECT_CLOUD_API_KEY --workspace $PREFECT_WORKSPACE
prefect deployment apply prefect/flows/pipeline-deployment.yaml
prefect agent start -q 'default'