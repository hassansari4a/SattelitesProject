FROM python:3.9

RUN apt-get install wget
RUN pip install python-dotenv spacetrack

WORKDIR /app
COPY etl_get_data_from_api.py etl_get_data_from_api.py

ENTRYPOINT [ "python", "etl_get_data_from_api.py" ]