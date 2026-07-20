# SQL Table Design & Query Practice

This folder contains SQL practice based on a food delivery platform database. It includes table creation, sample data insertion, and SQL queries covering joins, aggregation, grouping, subqueries, and window functions.

## Database Schema

The project consists of four relational tables:

- **Users** – Stores customer details and account information.
- **Restaurants** – Stores restaurant information, cuisine, and ratings.
- **Orders** – Stores order details placed by users.
- **Deliveries** – Stores delivery status and delivery time for each order.

## Topics Covered

- CREATE TABLE
- INSERT INTO
- PRIMARY KEY
- FOREIGN KEY
- INNER JOIN
- LEFT JOIN
- GROUP BY
- HAVING
- Aggregate Functions (`SUM`, `COUNT`, `AVG`)
- DISTINCT
- Subqueries
- Window Functions (`RANK()`)

## Practice Questions

The SQL queries solve the following business scenarios:

1. Display users, restaurants, and bill amounts for all orders.
2. List restaurants that have delivery records.
3. Find orders delivered in more than 35 minutes.
4. Calculate total spending by each user.
5. Count the total number of orders placed by each user.
6. Find restaurants generating more than ₹5000 revenue from Delhi users.
7. Count cancelled orders for each restaurant.
8. Find users whose single-order spending exceeds the platform average.
9. Calculate average delivery time by cuisine for highly rated restaurants.
10. Rank restaurants within each cuisine based on total orders received.

## Files Included

- `queries.sql` – Contains the database schema, sample data, and solutions to all SQL questions.
- `SQL ASSESSMENT.pdf` – Original assignment/problem statement used for this practice.

## Technologies Used

- MySQL
- SQL

## Learning Outcomes

- Designing relational database tables
- Working with primary and foreign keys
- Writing multi-table JOIN queries
- Using aggregate functions and grouping
- Applying subqueries for analytical queries
- Using window functions for ranking

---

**Author:** Diksha Tripathi