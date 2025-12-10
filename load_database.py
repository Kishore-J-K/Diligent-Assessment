"""
PROMPT 2: Load CSVs into SQLite Database
- Database name: ecommerce.db
- Create tables with proper data types
- Enforce foreign key relationships
- Drop tables if they already exist
- Print the number of rows inserted for each table
"""

import pandas as pd
import sqlite3
import os

def load_data():
    """Load CSV files into SQLite database with proper schema"""
    
    print("=" * 70)
    print("LOADING CSVs INTO SQLITE DATABASE")
    print("=" * 70)
    
    # Remove existing database if it exists
    if os.path.exists("ecommerce.db"):
        os.remove("ecommerce.db")
        print("\n🗑️  Removed existing ecommerce.db\n")
    
    # Connect to SQLite
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    
    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON")
    
    try:
        # Load customers
        print("📥 Loading customers...")
        df_customers = pd.read_csv("customers.csv")
        cursor.execute("""
            DROP TABLE IF EXISTS customers
        """)
        cursor.execute("""
            CREATE TABLE customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                signup_date TEXT NOT NULL,
                region TEXT NOT NULL
            )
        """)
        cursor.executemany(
            "INSERT INTO customers VALUES (?, ?, ?, ?, ?)",
            df_customers.itertuples(index=False, name=None)
        )
        print(f"   ✓ Inserted {len(df_customers)} rows into customers")
        
        # Load products
        print("📥 Loading products...")
        df_products = pd.read_csv("products.csv")
        cursor.execute("""
            DROP TABLE IF EXISTS products
        """)
        cursor.execute("""
            CREATE TABLE products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                stock_quantity INTEGER NOT NULL
            )
        """)
        cursor.executemany(
            "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
            df_products.itertuples(index=False, name=None)
        )
        print(f"   ✓ Inserted {len(df_products)} rows into products")
        
        # Load orders
        print("📥 Loading orders...")
        df_orders = pd.read_csv("orders.csv")
        cursor.execute("""
            DROP TABLE IF EXISTS orders
        """)
        cursor.execute("""
            CREATE TABLE orders (
                order_id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                order_date TEXT NOT NULL,
                payment_method TEXT NOT NULL,
                order_status TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """)
        cursor.executemany(
            "INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
            df_orders.itertuples(index=False, name=None)
        )
        print(f"   ✓ Inserted {len(df_orders)} rows into orders")
        
        # Load order_items
        print("📥 Loading order_items...")
        df_order_items = pd.read_csv("order_items.csv")
        cursor.execute("""
            DROP TABLE IF EXISTS order_items
        """)
        cursor.execute("""
            CREATE TABLE order_items (
                item_id INTEGER PRIMARY KEY,
                order_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """)
        cursor.executemany(
            "INSERT INTO order_items VALUES (?, ?, ?, ?, ?)",
            df_order_items.itertuples(index=False, name=None)
        )
        print(f"   ✓ Inserted {len(df_order_items)} rows into order_items")
        
        # Load reviews
        print("📥 Loading reviews...")
        df_reviews = pd.read_csv("reviews.csv")
        cursor.execute("""
            DROP TABLE IF EXISTS reviews
        """)
        cursor.execute("""
            CREATE TABLE reviews (
                review_id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                rating INTEGER NOT NULL,
                review_text TEXT,
                review_date TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        """)
        cursor.executemany(
            "INSERT INTO reviews VALUES (?, ?, ?, ?, ?, ?)",
            df_reviews.itertuples(index=False, name=None)
        )
        print(f"   ✓ Inserted {len(df_reviews)} rows into reviews")
        
        conn.commit()
        print("\n✅ All data loaded into ecommerce.db successfully!\n")
        
    except sqlite3.IntegrityError as e:
        print(f"\n❌ Integrity error: {e}")
        conn.rollback()
    except Exception as e:
        print(f"\n❌ Error loading data: {e}")
        conn.rollback()
    finally:
        conn.close()


if __name__ == "__main__":
    load_data()
