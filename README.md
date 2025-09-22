
#  Sales Dataset Cleaning - Task 1

This project demonstrates **data cleaning techniques** using Python and Pandas on a **sales dataset**. It is part of my learning journey to improve my **data analysis and data preprocessing** skills for analytics and machine learning.

---

## 📌 Project Overview

In this task, I took a **raw sales dataset** and cleaned it step by step. The main goals were to:

* Handle **missing values**
* Remove **duplicate records**
* Standardize **column names, phone numbers, and date formats**
* Fix **data types** for consistency
* Make the dataset ready for **analysis or visualization**

---

## 🛠️ Tools & Libraries Used

* **Python 3**
* **Pandas** – data manipulation
* **NumPy** – numerical operations
* **re (Regex)** – phone number cleaning

Install dependencies:

```bash
pip install pandas numpy
```

---

## 🧾 Steps Performed

### 1️⃣ Importing Libraries and Dataset

```python
import pandas as pd
import numpy as np

# Load dataset (with encoding fix)
df = pd.read_csv("sales_data_sample.csv", encoding="ISO-8859-1")
print(df.head())
```

---

### 2️⃣ Handling Missing Values

```python
print(df.isnull().sum())       # Check missing values
df = df.fillna("Unknown")      # Fill with placeholder
```

---

### 3️⃣ Removing Duplicate Records

```python
df = df.drop_duplicates()
```

---

### 4️⃣ Standardizing Data

```python
# Standardize text (lowercase + strip spaces)
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].map(lambda x: x.lower().strip() if isinstance(x, str) else x)

# Rename column headers
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert date formats
df['orderdate'] = pd.to_datetime(df['orderdate'], errors='coerce')
df['orderdate'] = df['orderdate'].dt.strftime('%d-%m-%Y')
```

---

### 5️⃣ Fixing Data Types

```python
# Example: convert numeric columns
df['quantityordered'] = pd.to_numeric(df['quantityordered'], errors='coerce').astype('Int64')
```

---

### 6️⃣ Cleaning Phone Numbers

```python
import re

def clean_phone(x):
    if pd.isna(x):
        return None
    digits = re.sub(r'\D', '', str(x))  # keep only digits
    if len(digits) >= 10:
        return digits[-10:]             # keep last 10 digits
    return digits

df['phone'] = df['phone'].apply(clean_phone)
```

---

### 7️⃣ Save the Cleaned Dataset

```python
df.to_csv("sales_data_sample_cleaned.csv", index=False)
```

---

## 📂 Project Structure

```
Sales-Data-Cleaning/
├── sales_data_sample.csv           # Original raw dataset
├── Task1.py                        # Python data cleaning script
└── sales_data_sample_cleaned.csv   # Final cleaned dataset
```

---
📊 Summary of Changes

✔ Missing values handled

✔ Duplicates removed

✔ Standardized text values

✔ Dates converted to proper format

✔ Columns renamed for consistency

✔ Data types corrected
