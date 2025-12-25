import initialization
from readers   import *
from pyspark.sql import SparkSession


# print(add(5,6))

print(println())

spark = SparkSession.builder.master("local[*]").appName("demo").getOrCreate()
df = spark.range(10)
df.show()
spark.stop()
