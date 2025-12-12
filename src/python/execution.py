
from packages.packages import add
from pyspark.sql import SparkSession
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "resources", "config.conf")

with open(CONFIG_PATH, "r") as f:
    contents = f.read()

print("=== Contents of config.conf ===")
print(contents)

print("=== Just testing the code for packages.packages ===")
final = add(10,15)
print(final)
   