## Create a config file

You will need to create a `config.ini` file in the root folder of your project in the following format.

```
[spacetrack]
username = <your-spacetrack-email-id>
password = <your-spacetrack-password>
```

## Create a .env file

You will need to create a `.env` file in the root folder of your project in the following format.
Before that, head over to your Prefect Cloud settings and create an API key.

```
PREFECT_CLOUD_API_KEY=<your-prefect-cloud-api-key>
PREFECT_WORKSPACE=<your-prefect-cloud-workspace>

SERVICE_ACCOUNT_CREDENTIALS_GCP=<your-service-account-credentials-json>
```
