
from packages.packages import add
from pyspark.sql import SparkSession
import os
from pyhocon import ConfigFactory
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "resources", "config.conf")

with open(CONFIG_PATH, "r") as f:
    contents = f.read()

    print(contents["app"]["name"])

# print("=== Contents of config.conf ===")
# print(contents)

# print("===Tetsing Hocon=================")

# config_path = Path(__file__).resolve().parents[1] / "resources" / "config.conf"
# cfg = ConfigFactory.parse_file(str(config_path))


# print(cfg["app"]["name"])               # orders-service
# print(cfg["app"]["db"]["host"])         # localhost
# print(cfg["app"]["features"]["retries"])# 3
# print(cfg["app"]["allowed_countries"])  # ['US', 'CA', 'IN']
   