# Slow Changing Dimensions

[Jake Roach's Blog](https://www.datacamp.com/tutorial/mastering-slowly-changing-dimensions-scd) helps me a lot and I make a summary and some examples.



**Definition**: Slowly Changing Dimensions (SCD) are a technique used to manage and track changes in dimension data over time in a data warehouse. Dimensions (e.g Detailed information about each item sold in that store; Floor, number of beds, bathrooms for all rooms in the hotel; Patient information, such as address and phone number) are typically descriptive attributes related to fact data (e.g., Transactions at a retail store, Guest reservations at a hotel, Patient visits to the doctor).

**Types of SCDs**:

1. **SCD Type 1**: Overwrites the existing data with new data. **Historical data is not preserved**.

   - **Example**: If a customer's address changes, the old address is **overwritten with the new** address.

     *Before:*

     | customer_id | customer_name | customer_address  |
     | ----------- | ------------- | ----------------- |
     | 1           | Tony          | Lane Cove, Sydney |
     | 2           | Bin           | Lane Cove, Sydney |

     Tony's address has **changed and been overwritten**, *After:*

     | customer_id | customer_name | customer_address  |
     | ----------- | ------------- | ----------------- |
     | 1           | Tony          | Burwood, Sydney   |
     | 2           | Bin           | Lane Cove, Sydney |

     

2. **SCD Type 2**: Adds a new row with the updated data, **preserving the historical data**.

   - **Example**: If a customer's address changes, a new record is added with the new address and a new surrogate key, along with start and end dates to indicate the validity period.

     *Before:*

     | customer_id | customer_name | customer_address  | is_deleted | update_time         | create_time         |
     | ----------- | ------------- | ----------------- | ---------- | ------------------- | ------------------- |
     | 1           | Tony          | Lane Cove, Sydney | 0          | 2024-05-20 12:00:00 | 2024-05-20 12:00:00 |
     | 2           | Bin           | Lane Cove, Sydney | 0          | 2024-05-20 12:00:00 | 2024-05-20 12:00:00 |

     Tony's address **has changed and a new record has been inserted**, *After:*

     | customer_id | customer_name | customer_address  | is_deleted | update_time         | create_time         |
     | ----------- | ------------- | ----------------- | ---------- | ------------------- | ------------------- |
     | 1           | Tony          | Burwood, Sydney   | 1          | 2024-06-20 12:00:00 | 2024-05-20 12:00:00 |
     | 2           | Bin           | Lane Cove, Sydney | 0          | 2024-05-20 12:00:00 | 2024-05-20 12:00:00 |
     | 1           | Tony          | Lane Cove, Sydney | 0          | 2024-06-20 12:00:00 | 2024-06-20 12:00:00 |

     The above table usually stored in the database as row data. It is difficult to use for reports. These dates represent the period of time that a dimension was the most current. It will become:

     | customer_id | customer_name | customer_address  | start_time          | end_time            |
     | ----------- | ------------- | ----------------- | ------------------- | ------------------- |
     | 1           | Tony          | Lane Cove, Sydney | 2024-05-20 12:00:00 | 2024-06-20 12:00:00 |
     | 2           | Bin           | Lane Cove, Sydney | 2024-05-20 12:00:00 | NULL                |
     | 1           | Tony          | Burwood, Sydney   | 2024-06-20 12:00:00 | NULL                |

     Advantages (compare with **TYPE1**):

     - Historical data are saved.

     

3. **SCD Type 3**: Adds a new column to store the previous value of the data.

   - **Example**: If a customer's address changes, a new column (e.g., `Previous Address`) is added to store the old address.

     *Before:*

     | customer_id | customer_name | current_customer_address |
     | ----------- | ------------- | ------------------------ |
     | 1           | Tony          | Lane Cove, Sydney        |
     | 2           | Bin           | Lane Cove, Sydney        |

​		*After:*

| customer_id | customer_name | current_customer_address | previous_customer_address |
| :---------- | ------------- | ------------------------ | ------------------------- |
| 1           | Tony          | Lane Cove, Sydney        | Burwood, Sydney           |
| 2           | Bin           | Lane Cove, Sydney        | NULL                      |

​		TYPE3 only can saved the **most recent value**. If the value changes **frequently**, TYPE3 is not suitable for the scenario.

