import pandas as pd

df = pd.read_csv(r"S:\Elevatelabs_tasks\Dataset\Task1\sales_data_sample.csv", encoding="ISO-8859-1")

print(df.head())

# 1. Identify missing values
print(df.isnull().sum())   
# filter rows with missing values
missing_rows = df[df.isnull().any(axis=1)]

# Handle missing values 
df = df.fillna("Unknown")  

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Standardize text values: Convert to lowercase and strip spaces
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].map(lambda x: x.lower().strip() if isinstance(x, str) else x)

# 4. Convert date formats to consistent type
# Step 1: Convert column to datetime (replace 'orderdate' with your actual column)
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')
# Step 2: Format as dd-mm-yyyy
df['ORDERDATE'] = df['ORDERDATE'].dt.strftime('%d-%m-%Y')

# 5. Rename column headers
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 6. Check and fix data types
print(df.dtypes)

#7.Ensure 'age' is int and 'orderdate' is datetime
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')

# 8. clean phone numbers
import re
if 'phone' in df.columns:
    def clean_phone(x):
        if pd.isna(x):
            return None       
        digits = re.sub(r'\D', '', str(x))
        if len(digits) >= 10:
            return digits[-10:]
        return digits     
    df['phone'] = df['phone'].apply(clean_phone)

# Verify cleaned dataset
print(df.head())
# Save cleaned file
df.to_csv(r"S:\Elevatelabs_tasks\Dataset\sales_data_sample_cleaned.csv", index=False)
