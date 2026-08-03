from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[1]")
    .appName("Test")
    .getOrCreate()
)

print("SPARK WORKS")

spark.stop()