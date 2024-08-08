# PySpark Streaming

## 1 Import Dependences

```python
from pyspark.sql import SparkSession

# pyspark.sql.types used to define Data Schema
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, ArrayType, TimestampType, DateType

# UDF: Use Defined Function
from pyspark.sql.functions import PandasUDFType
from pyspark.sql.functions import pandas_udf
```



## 2 Start Spark Session

```python
spark = SparkSession.Builder() \
    .appName('KafkaStructuredStreaming') \
    .master('local[*]') \
    .getOrCreate()
    
spark.sparkContext.setLogLevel("ERROR")  # suppress some INFO logs
```



## 3 Set Kafka Configuration

```python
kafka_group_id = "qjy20472-spark-app"
stream_df = spark.readStream \
    .format('kafka') \
    .option("kafka.bootstrap.servers", "ip1:host,ip2:host2") \
    .option("subscribe", "your_kafka_topic") \
    .option("startingOffsets", "latest") # latest, earliest, etc \
    .option("group.id", kafka_group_id) \
    .load()
```



## 4 capture & store stream data

```python
# the code does the following:
# 1. Capture the message and select key of message, value of message, partition of kafka and offset of kafka
# 2. Excutes parse_udf on datas. After the execution, udf will return a dataframe whose columns is 
# ['ein', 'clt_timestamp', 'pid', 'value']
# 3. explode the result of udf because result is a dataframe and named as 'datas'.
stream_df = stream_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)", "partition", "offset")\
       .select(
           explode(parse_udf('value')).alias('datas'), col('partition'), col('offset')
       )

# 4 set data type column by column. schema is defined `by data_schema`
for field_name in data_schema.fieldNames():
    stream_df = stream_df.withColumn(field_name, stream_df["datas"][field_name].cast(data_schema[field_name].dataType))
    
# 5 join with other dataframe
# Join streaming dataframe with signal_all_sdf
join_df = parsed_df.join(etl_config_sdf, on=["pid"], how="left")
join_df = join_df.join(signal_all_sdf, on=['pid'], how='left')

# 6 store data
# storing data into database
query = (join_df \
    .writeStream \
    .trigger(processingTime="5 seconds") \
    .foreachBatch(lambda batch, epoch_id: row_write_to_ck(batch, epoch_id, query)) \
    .option("checkpointLocation", checkpoint_location)\
    .start())

# Wait for the stream to finish
query.awaitTermination()
```



## Backup

Some functions

```python
def row_write_to_ck(df, epoch_id, query):
    ck_properties = {
        "driver": "ru.yandex.clickhouse.ClickHouseDriver",
        "socket_timeout": "300000",
        "rewriteBatchedStatements": "true",
        "batchsize": "1000000",
        "numPartitions": "8",
        "user": "*******",
        "password": "*******",
        "ignore": "true"
    }
    
    df = df \
        .withColumn('signal_multiplier', when(col('signal_multiplier').isNull(), 1.0).otherwise(col('signal_multiplier'))) \
        .withColumn('signal_offset', when(col('signal_offset').isNull(), 0).otherwise(col('signal_offset')))

    row_df = df.groupby(['ein', 'clt_timestamp']).apply(format_data_udf)

    row_df.write\
      .option('ignore', 'true') \
      .jdbc(url=f"jdbc:clickhouse://ck_ip:ck_host/ck_database", 
            table="ck_table", mode="append", properties=ck_properties)

```

