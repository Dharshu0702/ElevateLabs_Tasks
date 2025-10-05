import sqlite3

# Connect to database (creates sales_data.db file if not exists)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert some rows
cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", [
    ("Laptop", 2, 50000),
    ("Phone", 5, 20000),
    ("Tablet", 3, 15000),
    ("Laptop", 1, 50000),
    ("Phone", 2, 20000)
])

# Save and close
conn.commit()
conn.close()

print("Database created with sample data")
