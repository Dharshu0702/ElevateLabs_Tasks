
#  Sales Dataset Cleaning - Task 1

This task demonstrates **data cleaning techniques** using Python and Pandas on a **sales dataset**. It is part of my learning journey to improve my **data analysis and data preprocessing** skills for analytics and machine learning.

---

##  Overview

In this task, I took a **raw sales dataset** and cleaned it step by step. The main goals were to:

* Handle **missing values**
* Remove **duplicate records**
* Standardize **column names, phone numbers, and date formats**
* Fix **data types** for consistency
* Make the dataset ready for **analysis or visualization**

---

##  Tools & Libraries Used

* **Python 3**
* **Pandas** – data manipulation
* **NumPy** – numerical operations
* **re (Regex)** – phone number cleaning

Install dependencies:

```bash
pip install pandas numpy
```

---

## Steps Performed

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

---
---

## Superstore Sales Performance (Tableau) - Task 2

In this task, I analyzed the **Superstore dataset** using Tableau Public to uncover insights into sales and profitability.

### Steps Performed
- Created multiple **worksheets**:
  - Sales & Profit over Time  
  - Profitability by Region  
  - Categories with High Sales  
  - Impact of Discounts on Profit  
  - Top 5 Profitable States  

- Built a **dashboard** for interactive analysis.  
- Created a **story** combining all the sheets to narrate insights step by step.  
- Exported the final story as a PDF for submission.  

### Key Insights
- California contributes the highest profit, while Texas and Pennsylvania show consistent losses.  
- Technology category drives maximum profits.  
- High discounts often negatively impact profitability.  
- The West region is the most profitable overall.  

### Files in Task2
- `Supersales_performance.twbx` → Tableau Packaged Workbook  
- `Supersales_performance_visualization.pdf` → Exported Story in PDF  

---

---
### Coffee Sales Dashboard – Task 3

This task demonstrates creating an interactive Tableau dashboard from a coffee sales dataset. It is part of my learning journey to improve data visualization, storytelling, and business analytics skills.

 ### Overview

In this task, I took a cleaned coffee sales dataset and built a dashboard in Tableau.
The main goals were to:

Track key KPIs (Total Sales, Profit, Orders, Growth %)

Add filters & slicers for interactivity

Perform time-series analysis on sales and growth

Create summary KPI cards for stakeholders

Apply a consistent coffee-themed design

Export a PPT summary for business review

### Tools Used

Tableau Desktop – Dashboard creation

Excel / CSV – Data preparation

PowerPoint – Summary report for stakeholders

 ### Steps Performed

1️⃣ Importing Data

Loaded Coffe_sales.csv into Tableau.

Verified column types (Date, Money, Coffee Name, Payment Type).

2️⃣ Data Cleaning (minor fixes in Tableau)

Converted Date field to proper Date type.

Ensured Weekday and Month sorted correctly using helper columns.

3️⃣ KPI Cards

Created calculated fields:

Total Sales = SUM([money])

Profit = SUM([money]) * 0.7 (assumed margin)

Avg Daily Sales = SUM([money]) / COUNTD([Date])

MoM Growth % = (SUM([money]) - LOOKUP(SUM([money]), -1)) / LOOKUP(SUM([money]), -1)

4️⃣ Visualizations

Sales over Time (Line Chart)

MoM Growth % (Line Chart)

Sales by Coffee Type (Bar Chart)

Sales by Payment Method (Pie/Bar)

Peak Hours Heatmap (Weekday × Hour)

5️⃣ Dashboard Assembly

Added KPI Cards (top row).

Arranged charts into clean layout.

Applied filters (Coffee Name, Payment, Date).

Used coffee-themed color palette.

###  Project Structure

Coffee-Sales-Dashboard/

├── Coffe_sales.csv                 # Original dataset

├── Tableau_Coffee_Dashboard.twbx   # Tableau workbook

└── financial_sales_performance.pdf # Exported dashboard PDF



### Summary of Outcomes

✔ Dashboard with interactive filters

✔ KPI cards for Sales, Profit, Orders, Growth

✔ Time-series analysis for trends

✔ Product & customer insights

