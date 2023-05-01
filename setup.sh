#!/bin/bash
prefect cloud login --key $PREFECT_CLOUD_API_KEY --workspace $PREFECT_WORKSPACE
<<<<<<< HEAD
=======
python prefect/blocks/prefect-blocks.py
>>>>>>> 6468b9b973dd54b26cfffd6f3cd12fd61693c2f8
prefect deployment apply prefect/flows/pipeline-deployment.yaml
prefect agent start -q 'default'