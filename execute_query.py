"""
PROMPT 4: Execute SQL Query in Python
- Connect to ecommerce.db
- Execute the SQL join query
- Print the results as a pandas DataFrame
- Include exception handling
- Fully runnable Python code
"""

import sqlite3
import pandas as pd

def execute_sql_query():
    """Execute SQL join query and display results as DataFrame"""
    
    try:
        # Connect to ecommerce database
        print("=" * 80)
        print("EXECUTING SQL JOIN QUERY - RESULTS AS DATAFRAME")
        print("=" * 80)
        
        conn = sqlite3.connect("ecommerce.db")
        print("\n✓ Connected to ecommerce.db")
        
        # Define the SQL join query
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
        
        # Display the query
        print("\n📋 SQL QUERY:")
        print("-" * 80)
        print(sql_query)
        print("-" * 80)
        
        # Execute query and load into DataFrame
        df_results = pd.read_sql_query(sql_query, conn)
        
        # Configure pandas display options for better readability
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 25)
        
        # Display results
        print("\n📊 QUERY RESULTS:")
        print("-" * 80)
        print(df_results.to_string(index=False))
        print("-" * 80)
        
        # Summary statistics
        print(f"\n📈 SUMMARY:")
        print(f"   Total rows retrieved: {len(df_results)}")
        print(f"   Total revenue (all items): ${df_results['total_price'].sum():.2f}")
        print(f"   Average item value: ${df_results['total_price'].mean():.2f}")
        print(f"   Min item value: ${df_results['total_price'].min():.2f}")
        print(f"   Max item value: ${df_results['total_price'].max():.2f}")
        print(f"   Unique customers: {df_results['customer_id'].nunique()}")
        print(f"   Unique orders: {df_results['order_id'].nunique()}")
        print(f"   Unique products: {df_results['product_name'].nunique()}")
        
        # Return the DataFrame
        conn.close()
        print("\n✅ Query executed successfully!\n")
        return df_results
        
    except sqlite3.DatabaseError as e:
        print(f"\n❌ Database error: {e}")
        return None
    except sqlite3.OperationalError as e:
        print(f"\n❌ Operational error (database may not exist): {e}")
        return None
    except FileNotFoundError:
        print("\n❌ Error: ecommerce.db file not found in current directory")
        return None
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return None


if __name__ == "__main__":
    # Execute the query
    results = execute_sql_query()
    
    # Optionally, you can work with the results further
    if results is not None:
        print("\n" + "=" * 80)
        print("DATAFRAME INFORMATION")
        print("=" * 80)
        print(f"\nDataFrame shape: {results.shape}")
        print(f"\nColumn names and types:")
        print(results.dtypes)
        print("\n" + "=" * 80)
