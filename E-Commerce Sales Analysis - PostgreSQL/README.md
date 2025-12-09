# 🛒 E-Commerce Sales Analysis  
**Final Project – SQL, Data Cleaning & Business Insights**

---

## 📌 1. Project Overview

This project simulates a complete **E-Commerce Sales Database** that tracks customers, products, orders, and order items.

### 🔧 Project Objectives
- Design a **normalized relational database (3NF)**
- Insert **clean sample data**
- Perform **data cleaning**
- Run **analytical SQL queries**
- Generate **KPIs & business insights**

The database is structured to answer essential business questions such as:
- Who are the **top customers**?
- Which products generate the **most revenue**?
- What is the **sales trend over time**?
- How often do customers **return**?
- Which product **categories perform best**?

---

## 🗂️ 2. Database Schema

### 2.1 Entity-Relationship Diagram (ERD)
*(Add diagram if available)*

### 2.2 Tables & Fields

#### **customers**
- customer_id (PK)  
- first_name  
- last_name  
- email  
- phone  
- address  

#### **products**
- product_id (PK)  
- product_name  
- category  
- price  

#### **orders**
- order_id (PK)  
- customer_id (FK → customers)  
- order_date  
- payment_method  
- order_status  
- total_amount  

#### **order_items**
- order_item_id (PK)  
- order_id (FK → orders)  
- product_id (FK → products)  
- quantity  
- price  

---

## 💾 3. SQL Code

### 3.1 Create Tables
```sql
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date DATE,
    payment_method VARCHAR(50),
    order_status VARCHAR(20),
    total_amount NUMERIC(10,2)
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    price NUMERIC(10,2)
);
