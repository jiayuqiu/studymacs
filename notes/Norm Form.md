Normal forms are a set of guidelines used in database normalization to organize the data in a database to reduce redundancy and improve data integrity. Here’s a breakdown of the different normal forms and what they entail:

### First Normal Form (1NF)

**1NF Rule**: Ensure that each table column contains atomic (indivisible) values, and each column contains values of a single type.

- **Atomic Values**: Each field should contain only one value, not a set of values or a list.
- **Unique Columns**: All entries in a column should be of the same data type.
- **Unique Rows**: Each row must be unique, identifiable by a primary key.

**Example**: A table with customer information:

| CustomerID | CustomerName | PhoneNumbers       |
| ---------- | ------------ | ------------------ |
| 1          | John Doe     | 123-4567, 987-6543 |

This table is not in 1NF because the `PhoneNumbers` column contains multiple values. To convert it to 1NF:

| CustomerID | CustomerName | PhoneNumber |
| ---------- | ------------ | ----------- |
| 1          | John Doe     | 123-4567    |
| 1          | John Doe     | 987-6543    |

### Second Normal Form (2NF)

**2NF Rule**: Ensure the table is in 1NF and all non-key attributes are fully dependent on the primary key.

- **Full Functional Dependency**: Every non-key column must depend on the whole primary key, not just part of it.
- **Composite Key**: If the primary key is a combination of columns, each non-key column should be dependent on the entire combination.

**Example**: Consider a table with a composite key:

| OrderID | ProductID | ProductName |
| ------- | --------- | ----------- |
| 1       | 101       | Widget A    |
| 1       | 102       | Widget B    |

`ProductName` depends only on `ProductID`, not `OrderID`. To convert it to 2NF, separate it into two tables:

**Orders Table**:

| OrderID | ProductID |
| ------- | --------- |
| 1       | 101       |
| 1       | 102       |

**Products Table**:

| ProductID | ProductName |
| --------- | ----------- |
| 101       | Widget A    |
| 102       | Widget B    |

### Third Normal Form (3NF)

**3NF Rule**: Ensure the table is in 2NF and all non-key attributes are not only fully dependent on the primary key but also non-transitively dependent.

- **Non-Transitive Dependency**: No non-key column should depend on another non-key column.

**Example**: Consider the following table:

| EmployeeID | DepartmentID | DepartmentName |
| ---------- | ------------ | -------------- |
| 1          | 10           | Sales          |
| 2          | 20           | Marketing      |

`DepartmentName` depends on `DepartmentID`, which is not a primary key. To convert it to 3NF, split it into two tables:

**Employees Table**:

| EmployeeID | DepartmentID |
| ---------- | ------------ |
| 1          | 10           |
| 2          | 20           |

**Departments Table**:

| DepartmentID | DepartmentName |
| ------------ | -------------- |
| 10           | Sales          |
| 20           | Marketing      |

### Higher Normal Forms

There are higher normal forms beyond 3NF, such as BCNF (Boyce-Codd Normal Form), 4NF, and 5NF, which further reduce redundancy and handle more complex dependencies. However, 1NF, 2NF, and 3NF are usually sufficient for most practical purposes.

### Summary

- **1NF**: Ensure atomicity and uniqueness.
- **2NF**: Ensure full dependency on the entire primary key.
- **3NF**: Eliminate transitive dependencies. 

Understanding and applying these normal forms help create efficient and scalable databases that **maintain data integrity and reduce redundancy.**