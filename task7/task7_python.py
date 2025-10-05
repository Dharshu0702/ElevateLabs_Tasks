import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("sales_data.db")

# SQL query to calculate total quantity + revenue
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# Run query and load results into pandas DataFrame
df = pd.read_sql_query(query, conn)
print("📊 Sales Summary:\n")
print(df)

# Plot bar chart for revenue
df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.savefig("sales_chart.png")   # Save chart as image
plt.show()

# Close DB connection
conn.close()
