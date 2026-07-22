# E-Commerce End-to-End ETL Pipeline

A production-ready Data Engineering ETL Pipeline built with Python and Microsoft SQL Server to extract, transform, clean, and store a multi-table Brazilian E-Commerce dataset (Olist Dataset).

---

## Pipeline Architecture

[ Raw CSV Files ] ──> [ Python Data Cleaning (Pandas) ] ──> [ Fast Bulk Insertion via PyODBC ] ──> [ MS SQL Server ]

---

## Key Engineering Features

- Automated Data Cleaning: Standardized text strings, converted date columns to unified timestamp formats, and handled missing/null values (NaN & NaT).
- High-Performance Loading: Utilized pyodbc with fast_executemany = True to load 1M+ records across 9 relational tables into MS SQL Server within seconds.
- Relational Schema Design: Structured a normalized database schema with appropriate data types (VARCHAR, DATETIME2, FLOAT, INT) and Primary Keys to maintain data integrity.

---

## Project Structure

- etl_pipeline.py: Main Python script containing Extract, Transform, and Load logic.
- schema.sql: SQL DDL script for database and table creation.
- README.md: Detailed project documentation.

---

## Tech Stack & Tools

- Language: Python 3.x
- Data Transformation: pandas
- Database Driver: pyodbc
- Database System: Microsoft SQL Server (SSMS)
- Version Control: Git & GitHub

---

## Database Tables (9 Relational Tables)

1. Customers: Customer metadata (IDs, city, state, zip prefix).
2. Orders: Purchase timestamps, approval dates, carrier & delivery tracking.
3. Order Items: Item details, prices, freight values, and shipping limits.
4. Order Payments: Payment types, installments, and values.
5. Order Reviews: Review scores, comment titles, messages, and timestamps.
6. Products: Categories, dimensions, weight, and photo counts.
7. Sellers: Seller locations and IDs.
8. Geolocation: Zip code prefixes with geographical coordinates (lat/lng).
9. Category Translation: Portuguese to English category name mappings.

---

## How to Run Locally

1. Prerequisites: Ensure you have Python installed along with the necessary libraries:
   pip install pandas pyodbc

2. Database Setup: Run the schema.sql script in SQL Server Management Studio (SSMS) to create the ECommerceDB database and all required tables.

3. Run the Pipeline: Update the server_name in etl_pipeline.py with your SQL Server instance name, then run:
   python etl_pipeline.py
