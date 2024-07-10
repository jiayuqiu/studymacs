# Azure Synapse Analytics

## 1 What is Azure Synapse Analytics?

Azure Synapse Analytics provides a cloud platform for all of **these analytical workloads** through support for 
multiple data storage, processing, and analysis technologies in a single, integrated solution. The integrated design of Azure Synapse Analytics enables organizations to leverage investments and skills in multiple commonly used data technologies, including SQL, Apache Spark, and others; while providing a centrally managed service and a single, consistent user interface.


## 2 What are these analytical workloads?

![types of analytical workloads](../images/types-analytics.png)

4 types of analytical workloads in the above picture.

## 3 Serverless SQL pool

Azure Synapse Analytics includes serverless SQL pools, which are tailored for querying data in a data lake.

With a serverless SQL pool you can use SQL code to **query data in files** of various common formats without needing 
to load the file data into database storage.

### Advantage

- Analyze and process data in data lake by SQL, without the need to create or maintain a relational database storage.

### Common use case

- Data exploration: Data exploration involves browsing the data lake to get initial insights about the data, and is easily achievable with Azure Synapse Studio.
- Data transformation: with Synapse Spark, some data engineers might find data transformation easier to achieve using SQL.
- Logical data warehouse: 

### querying from files

- csv
```tsql
-- with explicit column names and data types
SELECT TOP 100 *
FROM OPENROWSET(
        BULK 'https://mydatalake.blob.core.windows.net/data/files/*.csv',
        FORMAT = 'csv',
        PARSER_VERSION = '2.0')
WITH (
    product_id INT,
    product_name VARCHAR(20) COLLATE Latin1_General_100_BIN2_UTF8,
    list_price DECIMAL(5,2)
) AS rows
```
- json
```tsql
-- with extracting data from json by JSON_VALUE
SELECT JSON_VALUE(doc, '$.product_name') AS product,
       JSON_VALUE(doc, '$.list_price') AS price
FROM
    OPENROWSET(
            BULK 'https://mydatalake.blob.core.windows.net/data/files/*.json',
            FORMAT = 'csv',
            FIELDTERMINATOR ='0x0b',
            FIELDQUOTE = '0x0b',
            ROWTERMINATOR = '0x0b'
    ) WITH (doc NVARCHAR(MAX)) as rows
```
- parquet
```tsql
-- with single file
SELECT TOP 100 *
FROM OPENROWSET(
             BULK 'https://mydatalake.blob.core.windows.net/data/files/*.*',
             FORMAT = 'parquet') AS rows

-- with partition data, often from HIVE
SELECT *
FROM OPENROWSET(
             BULK 'https://mydatalake.blob.core.windows.net/data/orders/year=*/month=*/*.*',
             FORMAT = 'parquet') AS orders
WHERE orders.filepath(1) = '2020'
  AND orders.filepath(2) IN ('1','2');
```

## 4 Dedicated SQL pool

Enterprise-scale relational database instances used to host data warehouses in which data is stored in relational tables.

## Backup

### Confused 1 : Using the serverless pool helps when you need to know exact cost for each query executed to monitor and attribute costs.
