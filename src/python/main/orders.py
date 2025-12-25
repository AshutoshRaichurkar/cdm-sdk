import initialization
from readers   import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("app").getOrCreate()
path = "/Users/ashutoshraichurkar/Documents/repos/cdm-sdk/test/csv/orders.csv"

df = csvReader(spark, path)
df.show()
spark.stop()
