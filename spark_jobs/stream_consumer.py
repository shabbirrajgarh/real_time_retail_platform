import os

# Hadoop / Winutils
os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"
os.environ["PATH"] += os.pathsep + r"C:\hadoop\bin"

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType
)

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("RetailStreamingConsumer")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.13:4.2.0,"
        "org.postgresql:postgresql:42.7.3"
    )
    .config("spark.driver.extraJavaOptions", "-Duser.timezone=UTC")
    .config("spark.executor.extraJavaOptions", "-Duser.timezone=UTC")
    .config("spark.hadoop.io.native.lib.available", "false")
    .getOrCreate()
)

spark.conf.set("spark.sql.session.timeZone", "UTC")
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("customer_id", IntegerType(), True),
    StructField("product", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("timestamp", StringType(), True)
])

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "retail-transactions")
    .option("startingOffsets", "latest")
    .load()
)

json_df = df.selectExpr("CAST(value AS STRING) as json")

parsed_df = (
    json_df
    .select(from_json(col("json"), schema).alias("data"))
    .select("data.*")
    .withColumnRenamed("timestamp", "transaction_time")
)

def write_to_postgres(batch_df, batch_id):
    print(f"\n===== BATCH {batch_id} =====")

    count = batch_df.count()
    print(f"Rows in batch: {count}")

    if count == 0:
        return

    batch_df.show(5, False)

    (
        batch_df.write
        .format("jdbc")
        .option(
            "url",
            "jdbc:postgresql://localhost:5432/retail_dw?options=-c%20TimeZone=UTC"
        )
        .option("dbtable", "transactions")
        .option("user", "retail_user")
        .option("password", "retail_password")
        .option("driver", "org.postgresql.Driver")
        .mode("append")
        .save()
    )

    print(f"Batch {batch_id} written successfully.")
query = (
    parsed_df.writeStream
    .foreachBatch(write_to_postgres)
    .outputMode("append")
    .option(
        "checkpointLocation",
        "file:///C:/tmp/checkpoint_pg"
    )
    .start()
)

query.awaitTermination()