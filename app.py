import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Step 1: Create DataFrames

# Customers DataFrame
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'country': ['USA', 'Canada', 'USA', 'Canada', 'USA']
})

# Orders DataFrame
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 2, 3, 1, 4],
    'product_id': [1001, 1002, 1003, 1004, 1001],
    'order_date': [datetime.now() - timedelta(days=i*30) for i in range(5)],
    'quantity': [2, 1, 5, 3, 2]
})

# Products DataFrame
products = pd.DataFrame({
    'product_id': [1001, 1002, 1003, 1004],
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'price': [1000, 800, 600, 300]
})

# Step 2: Transformations and Joins

# Join orders with products to get product price
orders_with_products = pd.merge(orders, products, on='product_id', how='left')

# Calculate total sales amount for each order
orders_with_products['total_amount'] = orders_with_products['quantity'] * orders_with_products['price']

# Join with customers to get customer details
orders_with_customers = pd.merge(orders_with_products, customers, on='customer_id', how='left')

# Final output
print(orders_with_customers)