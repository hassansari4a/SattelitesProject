FROM prefecthq/prefect:2.7.7-python3.9

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt --trusted-host pypi-python.org --no-cache-dir

# Copy application code
COPY . /app
WORKDIR /app

# Set the API URL as an environment variable
ENV PREFECT__CLOUD__API="https://api.prefect.cloud/api/accounts/d0d666b0-1c14-4d7a-99cc-204d7c584a02/workspaces/cdf7e9e9-954"

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Set the entrypoint script as the container's entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# COPY prefect/flows /opt/prefect/flows

# ENV PREFECT_API_URL=https://api.prefect.cloud/api/accounts/d0d666b0-1c14-4d7a-99cc-204d7c584a02/workspaces/cdf7e9e9-954

# ENV PREFECT__CLOUD__API="https://api.prefect.cloud/api/accounts/d0d666b0-1c14-4d7a-99cc-204d7c584a02/workspaces/cdf7e9e9-954"

# ENV PREFECT_API_KEY=pnu_YTF0qFmhT9pbQqjBvpDH2LUuuftxW7265cTN

# CMD [ "prefect", "cloud", "login", "--key", "pnu_YTF0qFmhT9pbQqjBvpDH2LUuuftxW7265cTN" ]
