FROM prefecthq/prefect:2.7.7-python3.9

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt --trusted-host pypi-python.org --no-cache-dir

# Copy application code
COPY . /app
WORKDIR /app

COPY setup.sh .

RUN chmod +x setup.sh

ARG PREFECT_CLOUD_API_KEY
ARG PREFECT_WORKSPACE
ARG SERVICE_ACCOUNT_CREDENTIALS_GCP

ENV PREFECT_CLOUD_API_KEY=$PREFECT_CLOUD_API_KEY
ENV PREFECT_WORKSPACE=$PREFECT_WORKSPACE
ENV SERVICE_ACCOUNT_CREDENTIALS_GCP=$SERVICE_ACCOUNT_CREDENTIALS_GCP

ENTRYPOINT [ "./setup.sh" ]
