"""
PROMPT 1: Generate 5 Synthetic E-Commerce CSV Files
- customers.csv: 500 records
- products.csv: 200 records
- orders.csv: 2000 records
- order_items.csv: ~3500 records
- reviews.csv: 500 records
"""

import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_csv_files():
    """Generate 5 synthetic e-commerce CSV files"""
    
    print("=" * 70)
    print("GENERATING 5 SYNTHETIC E-COMMERCE CSV FILES")
    print("=" * 70)
    
    # 1. Generate Customers
    print("\n📦 Generating customers.csv (500 records)...")
    customers = []
    regions = ["North America", "Europe", "Asia", "South America", "Africa", "Oceania"]
    
    for i in range(1, 501):
        customers.append({
            "customer_id": i,
            "name": fake.name(),
            "email": fake.email(),
            "signup_date": fake.date_between(start_date="-2y"),
            "region": random.choice(regions)
        })
    
    df_customers = pd.DataFrame(customers)
    df_customers.to_csv("customers.csv", index=False)
    print(f"✓ Saved customers.csv with {len(df_customers)} records")
    
    # 2. Generate Products
    print("\n📦 Generating products.csv (200 records)...")
    products = []
    categories = ["Electronics", "Clothing", "Home & Garden", "Sports", "Books", 
                  "Toys", "Beauty", "Food & Beverages", "Furniture", "Jewelry"]
    
    for i in range(1, 201):
        products.append({
            "product_id": i,
            "product_name": fake.word() + " " + fake.word(),
            "category": random.choice(categories),
            "price": round(random.uniform(10, 500), 2),
            "stock_quantity": random.randint(0, 500)
        })
    
    df_products = pd.DataFrame(products)
    df_products.to_csv("products.csv", index=False)
    print(f"✓ Saved products.csv with {len(df_products)} records")
    
    # 3. Generate Orders
    print("\n📦 Generating orders.csv (2000 records)...")
    orders = []
    payment_methods = ["Credit Card", "Debit Card", "PayPal", "Apple Pay", "Google Pay", "Bank Transfer"]
    order_statuses = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled", "Refunded"]
    
    for i in range(1, 2001):
        orders.append({
            "order_id": i,
            "customer_id": random.randint(1, 500),
            "order_date": fake.date_between(start_date="-1y"),
            "payment_method": random.choice(payment_methods),
            "order_status": random.choice(order_statuses)
        })
    
    df_orders = pd.DataFrame(orders)
    df_orders.to_csv("orders.csv", index=False)
    print(f"✓ Saved orders.csv with {len(df_orders)} records")
    
    # 4. Generate Order Items
    print("\n📦 Generating order_items.csv (~3500 records)...")
    order_items = []
    item_id = 1
    
    for order_id in range(1, 2001):
        num_items = random.randint(1, 3)
        for _ in range(num_items):
            product_id = random.randint(1, 200)
            unit_price = df_products[df_products["product_id"] == product_id]["price"].values[0]
            
            order_items.append({
                "item_id": item_id,
                "order_id": order_id,
                "product_id": product_id,
                "quantity": random.randint(1, 10),
                "unit_price": unit_price
            })
            item_id += 1
    
    df_order_items = pd.DataFrame(order_items)
    df_order_items.to_csv("order_items.csv", index=False)
    print(f"✓ Saved order_items.csv with {len(df_order_items)} records")
    
    # 5. Generate Reviews
    print("\n📦 Generating reviews.csv (500 records)...")
    reviews = []
    review_texts = [
        "Great product, highly recommended!",
        "Good quality but expensive.",
        "Not as described, disappointed.",
        "Excellent service and fast delivery!",
        "Average product, nothing special.",
        "Best purchase ever!",
        "Poor quality, would not buy again.",
        "Fantastic! Exceeded my expectations.",
        "Just okay, nothing impressive.",
        "Love it! Perfect for my needs."
    ]
    
    for i in range(1, 501):
        reviews.append({
            "review_id": i,
            "customer_id": random.randint(1, 500),
            "product_id": random.randint(1, 200),
            "rating": random.randint(1, 5),
            "review_text": random.choice(review_texts),
            "review_date": fake.date_between(start_date="-1y")
        })
    
    df_reviews = pd.DataFrame(reviews)
    df_reviews.to_csv("reviews.csv", index=False)
    print(f"✓ Saved reviews.csv with {len(df_reviews)} records")
    
    print("\n✅ All CSV files generated successfully!\n")
    return df_customers, df_products, df_orders, df_order_items, df_reviews


if __name__ == "__main__":
    generate_csv_files()
