# Interview Records

## Data Engineer

### Q1: How to rename a column of a dataframe?

```python
# rename 'ein1' as to 'ein'
snat_sdf = snat_sdf.withColumnRenamed(existing="ein1", new="ein")
```

### Q2: What's the difference between repartition and coalesce?

In PySpark, both `repartition` and `coalesce` are used to change the number of partitions of an RDD or DataFrame.

#### q2.1 Repartition

**Purpose:** To **increase or decrease** the number of partitions.

**Behavior:** Performs a full shuffle of the data across the network, resulting in a **more evenly distributed dataset** across the new partitions.

**Use Case:** Best used when you need to increase the number of partitions or when you want a more balanced distribution of data. It is more computationally expensive due to the shuffling.

```python
# Increase the number of partitions
df = df.repartition(10)

# Decrease the number of partitions
df = df.repartition(1)
```



#### q2.2 Coalesce

**Purpose:** To **decrease** the number of partitions. **Only decrease.**

**Behavior:** Merges the existing partitions into fewer partitions without a full shuffle. It tries to combine the data within the same partition and only moves data between partitions if necessary.

**Use Case:** Best used when you need to reduce the number of partitions for optimization, such as when **writing out to storage** or when performing operations that benefit from fewer partitions. It is **less computationally expensive than repartition** because it minimizes data movement.

```python
# Decrease the number of partitions
df = df.coalesce(2)
```



#### q2.3 Key difference

1 **Shuffling:**

- `repartition` involves a full shuffle of the data, ensuring that the data is evenly distributed across the new partitions.
- `coalesce` minimizes shuffling by merging existing partitions, which can lead to uneven distribution but is more efficient.

**2 Performance:**

- `repartition` is more computationally and network-intensive due to the shuffle.
- `coalesce` is more efficient as it avoids a full shuffle, making it faster for reducing partitions.

3 **Use Case:**

- Use `repartition` when you need to change the number of partitions significantly and ensure even distribution, especially when increasing partitions.
- Use `coalesce` when reducing the number of partitions, particularly in situations where you want to avoid the overhead of a full shuffle.

In summary, choose `repartition` when you need a balanced number of partitions regardless of performance costs, and use `coalesce` when you need to reduce partitions efficiently with minimal data movement.

### Q3: What's the data skew?

Data skew occurs when data is unevenly distributed across partitions, causing some partitions to have significantly more data than others. This imbalance can lead to performance bottlenecks, as some tasks take much longer to process than others, resulting in inefficient use of resources and longer overall job completion times.

#### Cause of data skew

**1 Highly Skewed Data:**

- When certain keys or values are much more frequent than others, leading to partitions with a disproportionately large amount of data.

**2 Improper Partitioning:**

- When data is not partitioned properly, some partitions might end up with much more data than others.

**3 Joins on Skewed Keys:**

- Performing join operations on keys that are not evenly distributed can lead to skewed partitions, especially if a key in one dataset has many corresponding entries in another.

### Q4: What you should do when you need to consume Kafka message?



### Q5: Data Modelling experience.

Please check: [Data Modelling notes](./Data Modelling.md)



## Python Developer



## Linux



## Git







