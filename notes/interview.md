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

**1 Shuffling:**

- `repartition` involves a full shuffle of the data, ensuring that the data is evenly distributed across the new partitions.
- `coalesce` minimizes shuffling by merging existing partitions, which can lead to uneven distribution but is more efficient.

**2 Performance:**

- `repartition` is more computationally and network-intensive due to the shuffle.
- `coalesce` is more efficient as it avoids a full shuffle, making it faster for reducing partitions.

**3 Use Case:**

- Use `repartition` when you need to change the number of partitions significantly and ensure even distribution, especially when increasing partitions.
- Use `coalesce` when reducing the number of partitions, particularly in situations where you want to avoid the overhead of a full shuffle.

In summary, choose `repartition` when you need a balanced number of partitions regardless of performance costs, and use `coalesce` when you need to reduce partitions efficiently with minimal data movement.

### Q3: What's the data skew?

There are more context. Please check: [Data Skew notes](./Data Engineer/Data Skew.md)



### Q4: What you should do when you need to consume Kafka message?

There are more context and codes. Please check: [Streaming notes](./Data Engineer/PySpark Streaming.md)



### Q5: Data Modelling experience.

There is more context. Please check: [Data Modelling notes](./Data Engineer/Data Modelling.md)



## Q6: Concepts: full load, increasement load, slow changing dimensions

### Full load

**Definition**: A full load involves loading the entire dataset from the source into the target system. This process overwrites the existing data in the target system, replacing it with a fresh copy of the data from the source.

**When to Use**:

- When the dataset is relatively small and can be loaded quickly.
- When data needs to be completely refreshed.
- Initial loading of the data warehouse.

**Advantages**:

- Simplicity: Easier to implement and understand.
- Consistency: Ensures the target system is always in sync with the source.

**Disadvantages**:

- Inefficient for large datasets: Can be time-consuming and resource-intensive.
- Overwrites all data: Changes to data in the target system are lost.



### Incremental Load

**Definition**: An incremental load (or delta load) involves loading only the data that has changed (new, updated, or deleted records) since the last load. This approach is more efficient for large datasets, as it minimizes the amount of data transferred and processed.

**When to Use**:

- When working with large datasets.
- When only a portion of the data changes frequently.
- For ongoing data integration where real-time or near-real-time updates are required.

**Advantages**:

- Efficiency: Reduces the amount of data processed and transferred.
- Performance: Faster loading times and lower resource usage.

**Disadvantages**:

- Complexity: More complex to implement and maintain.
- Data Consistency: Requires mechanisms to track changes accurately.

### Slow Changing Dimensions

There is more context. Please check: [SCD notes](./Data Engineer/SCD.md)



## Python Developer

dict[class]: value ?



## Linux

cat, grep, find, `>`, `>>`



## Git

rebase, merge



