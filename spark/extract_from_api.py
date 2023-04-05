from spacetrack import SpaceTrackClient
import pandas as pd
from pyspark.sql import SparkSession, types

def get_data():
    st = SpaceTrackClient('hassansari4a@gmail.com', '9817377317NCELL')
    csvfile = st.satcat(format='csv')
    with open('my_file.csv', 'w') as my_file:
        my_file.write(csvfile)
    df = pd.read_csv('my_file.csv')
    df.to_csv('satcatdata.csv', index=False)

def create_spark_session():
    spark = SparkSession.builder.appName('SattelitesProject').getOrCreate()
    return spark

def read_data(spark):
    dfspark = spark.read.format("csv") \
                   .option("delimiter", ",") \
                   .option("header", "true") \
                   .option("inferSchema", "true") \
                   .load("satcatdata.csv")
    return dfspark
    
def clean_data(dfspark):
    dfspark = dfspark.drop('COMMENT', 'COMMENTCODE', 'RCSVALUE', 'RCS_SIZE')
    return dfspark

def write_data(dfspark):
    dfspark.coalesce(1).write.parquet("../data/satcatdata")
    return

