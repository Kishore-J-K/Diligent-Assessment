"""
PROMPT 3: Write SQL Join Query
- Join customers, orders, order_items, and products
- Output columns: customer_id, customer_name, order_id, order_date, product_name, quantity, total_price
- Sort results by order_date descending
- Limit 50 rows
- Use proper INNER JOINs
"""

import sqlite3
import pandas as pd

def execute_join_query():
    """Execute SQL join query and display results"""
    
    print("=" * 70)
    print("SQL JOIN QUERY - CUSTOMERS, ORDERS, ITEMS & PRODUCTS")
    print("=" * 70)
    
    try:
        # Connect to database
        conn = sqlite3.connect("ecommerce.db")
        
        # SQL Join Query
        sql_query = """
        SELECT 
            c.customer_id,
            c.name AS customer_name,
            o.order_id,
            o.order_date,
            p.product_name,
            oi.quantity,
            (oi.quantity * oi.unit_price) AS total_price
        FROM customers c
        INNER JOIN orders o ON c.customer_id = o.customer_id
        INNER JOIN order_items oi ON o.order_id = oi.order_id
        INNER JOIN products p ON oi.product_id = p.product_id
        ORDER BY o.order_date DESC
        LIMIT 50
        """
        
        print("\n📋 SQL Query:\n")
        print(sql_query)
        print("\n" + "=" * 70)
        print("Query Results (50 rows):\n")
        
        # Execute query and load into DataFrame
        df_results = pd.read_sql_query(sql_query, conn)
        
        # Display results
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        
        print(df_results.to_string(index=False))
        
        print("\n" + "=" * 70)
        print(f"✅ Query executed successfully! Retrieved {len(df_results)} rows\n")
        
        conn.close()
        return df_results
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


if __name__ == "__main__":
    results_df = execute_join_query()
