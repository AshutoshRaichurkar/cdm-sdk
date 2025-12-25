# from pyspark.sql import SparkSession
# spark = SparkSession.builder.getOrCreate()

# class Greeter:
#     def __init__(self, name: str = "Ashutosh"):
#         self.name = name

#     def greet(self):
#         print(f"Hello from cdm-sdk, {self.name}!")


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    g = Greeter()
    g.greet()
    print("2 + 3 =", add(2, 3))



