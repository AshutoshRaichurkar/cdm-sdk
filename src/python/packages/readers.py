from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F

def csvReader(spark: SparkSession, path: str) -> dataframe:
    return spark.read.option("header","true").csv(path)