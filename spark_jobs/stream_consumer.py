import os

os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("RetailStreamingConsumer")
    .config("spark.hadoop.io.native.lib.available", "false")
    .config(
    "spark.jars.packages",
    "org.apache.spark:spark-sql-kafka-0-10_2.13:4.2.0"
)
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "retail-transactions")
    .option("startingOffsets", "latest")
    .load()
)

output = df.selectExpr(
    "CAST(key AS STRING) as key",
    "CAST(value AS STRING) as value",
    "timestamp"
)

query = (
    output.writeStream
    .format("console")
    .outputMode("append")
    .option("checkpointLocation", "checkpoint")
    .start()
)

query.awaitTermination()