# 🐼 Pandas for Data Analysis — Complete Notes
### From Scratch to Professional | Beginner to Advanced

---

## Table of Contents

| # | Topic |
|---|-------|
| 01 | [Introduction to Pandas](#1-introduction-to-pandas) |
| 02 | [Why Pandas?](#2-why-pandas) |
| 03 | [History & Creator](#3-history--creator-of-pandas) |
| 04 | [Data Manipulation vs Data Analysis](#4-data-manipulation-vs-data-analysis) |
| 05 | [Installation & Setup](#5-installation--setup) |
| 06 | [Importing Pandas](#6-importing-pandas) |
| 07 | [Series](#7-series) |
| 08 | [DataFrame](#8-dataframe) |
| 09 | [Reading Files](#9-reading-files) |
| 10 | [Saving Files](#10-saving-files) |
| 11 | [Data Exploration](#11-data-exploration) |
| 12 | [Data Inspection Methods](#12-data-inspection-methods) |
| 13 | [Statistical Analysis](#13-statistical-analysis) |
| 14 | [Data Selection](#14-data-selection) |
| 15 | [Filtering Data](#15-filtering-data) |
| 16 | [Sorting Data](#16-sorting-data) |
| 17 | [Data Cleaning](#17-data-cleaning) |
| 18 | [Missing Values](#18-missing-values) |
| 19 | [Duplicate Values](#19-duplicate-values) |
| 20 | [Data Transformation](#20-data-transformation) |
| 21 | [GroupBy Operations](#21-groupby-operations) |
| 22 | [Aggregations](#22-aggregations) |
| 23 | [Merging Data](#23-merging-data) |
| 24 | [Joining Data](#24-joining-data) |
| 25 | [Concatenation](#25-concatenation) |
| 26 | [Working with Dates](#26-working-with-dates) |
| 27 | [String Operations](#27-string-operations) |
| 28 | [Apply Functions](#28-apply-functions) |
| 29 | [Lambda Functions](#29-lambda-functions) |
| 30 | [Pivot Tables](#30-pivot-tables) |
| 31 | [Crosstabs](#31-crosstabs) |
| 32 | [Performance Optimization](#32-performance-optimization) |
| 33 | [Common Errors](#33-common-errors) |
| 34 | [Interview Questions](#34-interview-questions) |
| 35 | [Practice Exercises](#35-practice-exercises) |
| 36 | [Cheatsheet](#36-pandas-cheatsheet) |
| 37 | [Final Summary](#37-final-summary) |

---

## 1. Introduction to Pandas

### Definition
Pandas is an open-source Python library used for **data manipulation, cleaning, and analysis**. The name "Pandas" comes from **Panel Data**, a term used in economics and statistics to describe multi-dimensional data.

Think of Pandas like **Microsoft Excel inside Python** — but 100× faster, more powerful, and fully programmable.

### Why It Is Used
Pandas is the backbone of data science in Python. It allows you to:
- Load large datasets (CSV, Excel, JSON, SQL, etc.)
- Clean messy data (handle missing values, duplicates)
- Transform and reshape data
- Perform powerful statistical analysis
- Prepare data for Machine Learning models

### Real-World Example
Imagine you work at Walmart and have sales data of 1 million rows. You need to:
- Find which store earned the most revenue
- Identify months with lowest sales
- Clean all empty rows

Doing this manually in Excel would take hours. With Pandas, it takes **3-4 lines of code**.

---

## 2. Why Pandas?

### Before Pandas (The Problem)
Before Pandas, Python developers used:
- Plain Python lists and dictionaries (very slow and hard to manage)
- NumPy arrays (no column labels, limited to numbers)
- CSV module (basic reading only, no analysis)

### After Pandas (The Solution)
Pandas gives you:

| Feature | Without Pandas | With Pandas |
|---------|----------------|-------------|
| Load CSV | 15+ lines of code | 1 line |
| Filter data | Complex loops | `df[df['col'] > 5]` |
| Missing values | Manual loops | `df.fillna()` |
| Group & aggregate | Very complex | `df.groupby()` |
| Merge tables | Nested loops | `pd.merge()` |

### Pandas vs Excel

| Factor | Excel | Pandas |
|--------|-------|--------|
| Max rows | ~1 million | Unlimited |
| Speed | Slow on large data | Very fast |
| Automation | Limited (macros) | Full automation |
| ML Integration | None | Direct |
| Free | Paid (mostly) | Free & Open Source |

---

## 3. History & Creator of Pandas

### Creator
Pandas was created by **Wes McKinney** in **2008** while he was working at AQR Capital Management (a hedge fund). He needed a powerful, flexible data analysis tool in Python and built Pandas to solve his own problems.

### Timeline

| Year | Milestone |
|------|-----------|
| 2008 | Wes McKinney starts developing Pandas at AQR Capital |
| 2009 | Open-sourced on GitHub |
| 2012 | Wes publishes "Python for Data Analysis" book |
| 2015 | Pandas becomes standard in data science |
| 2020 | Pandas 1.0 released (major stable release) |
| 2023 | Pandas 2.0 released (major performance improvements) |

### Key Book
"Python for Data Analysis" by Wes McKinney is the bible of Pandas. It covers everything from basics to advanced topics.

---

## 4. Data Manipulation vs Data Analysis

### Definitions

**Data Manipulation** = Changing the structure or content of data
Examples: Adding columns, removing duplicates, merging tables, handling missing values

**Data Analysis** = Understanding patterns and insights from data
Examples: Finding average salary, identifying best-selling products, checking trends

### Real-World Comparison

| Task | Type |
|------|------|
| Removing empty rows | Manipulation |
| Finding max salary | Analysis |
| Merging employee + salary tables | Manipulation |
| Calculating monthly revenue | Analysis |
| Renaming columns | Manipulation |
| Finding correlation between age and salary | Analysis |

**In Practice:** You always do manipulation first, then analysis.

---

## 5. Installation & Setup

### Definition
Before using Pandas, you need to install it in your Python environment.

### Method 1 — Using pip (Recommended for Beginners)

```bash
pip install pandas
```

### Method 2 — Using conda (If using Anaconda)

```bash
conda install pandas
```

### Method 3 — Install with Excel support

```bash
pip install pandas openpyxl xlrd
```

You need `openpyxl` for reading/writing `.xlsx` files and `xlrd` for older `.xls` files.

### Verify Installation

```python
import pandas as pd
print(pd.__version__)
```

**Output:**
```
2.1.0
```

### Common Installation Errors

**Error 1: `ModuleNotFoundError: No module named 'pandas'`**
Solution: Run `pip install pandas` in your terminal or Jupyter notebook cell using `!pip install pandas`.

**Error 2: `No module named 'openpyxl'` when reading Excel**
Solution: Run `pip install openpyxl`.

**Error 3: Permission denied during install**
Solution: Use `pip install pandas --user` to install for current user only.

### Best Practices
- Always use virtual environments (`venv` or `conda env`) to manage packages
- Keep Pandas updated: `pip install --upgrade pandas`
- Use Jupyter Notebook or VS Code for the best Pandas experience

---

## 6. Importing Pandas

### Definition
Importing means making the Pandas library available in your Python script so you can use its functions.

### Standard Import (Used Everywhere)

```python
import pandas as pd
```

**Why `pd`?** It's a universal shorthand convention. Every data scientist in the world uses `pd`. Never change it.

### Additional Imports for Data Work

```python
import pandas as pd
import numpy as np          # Numerical operations
import matplotlib.pyplot as plt  # Plotting
import xlrd                 # For .xls files
import openpyxl             # For .xlsx files
```

### Checking Available Functions

```python
# See all pandas functions
print(dir(pd))

# Get help on a specific function
help(pd.read_csv)
```

### Best Practices
- Always import Pandas at the top of your file
- Never use `from pandas import *` — it pollutes the namespace and causes confusion
- Stick to `import pandas as pd` always

---

## 7. Series

### Definition
A **Series** is a one-dimensional labeled array. Think of it as a **single column** from an Excel spreadsheet. It can hold any data type — integers, floats, strings, Python objects.

```
Index | Value
------|-------
  0   |  10
  1   |  20
  2   |  30
  3   |  40
```

### Syntax

```python
pd.Series(data, index=None, dtype=None, name=None)
```

### Example 1 — Creating a Series from a List

```python
import pandas as pd

marks = pd.Series([85, 90, 78, 95, 88])
print(marks)
```

**Output:**
```
0    85
1    90
2    78
3    95
4    88
dtype: int64
```

**Explanation:**
- Left column = index (auto-assigned 0, 1, 2...)
- Right column = values
- `dtype: int64` = data type of values

### Example 2 — Series with Custom Index

```python
marks = pd.Series(
    [85, 90, 78, 95, 88],
    index=['Math', 'Science', 'English', 'Hindi', 'CS']
)
print(marks)
```

**Output:**
```
Math       85
Science    90
English    78
Hindi      95
CS         88
dtype: int64
```

### Example 3 — Creating a Series from a Dictionary

```python
salary_data = {'Alice': 50000, 'Bob': 60000, 'Charlie': 55000}
salary = pd.Series(salary_data)
print(salary)
```

**Output:**
```
Alice      50000
Bob        60000
Charlie    55000
dtype: int64
```

### Accessing Series Elements

```python
marks = pd.Series([85, 90, 78], index=['Math', 'Science', 'English'])

# By label
print(marks['Math'])       # 85

# By position
print(marks[0])            # 85

# Multiple elements
print(marks[['Math', 'English']])

# Slicing
print(marks[0:2])
```

### Series Operations

```python
s = pd.Series([10, 20, 30, 40])

print(s + 5)      # Adds 5 to every element
print(s * 2)      # Multiplies every element by 2
print(s.sum())    # Sum of all values
print(s.mean())   # Average
print(s.max())    # Maximum value
print(s.min())    # Minimum value
print(s.count())  # Count of non-null values
```

**Output:**
```
0    15
1    25
2    35
3    45
dtype: int64

200
25.0
40
10
4
```

### Checking Series Properties

```python
s = pd.Series([10, 20, 30, 40], name='Scores')

print(s.dtype)    # int64
print(s.shape)    # (4,)
print(s.size)     # 4
print(s.name)     # Scores
print(s.index)    # RangeIndex(start=0, stop=4, step=1)
print(s.values)   # array([10, 20, 30, 40])
```

### Common Errors

**Error 1: `KeyError: 'Math'`**
```python
s = pd.Series([1, 2, 3])
print(s['Math'])  # Error! No label 'Math'
```
Solution: Use integer index `s[0]` or create series with correct labels.

**Error 2: Index mismatch when combining Series**
```python
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6], index=[3, 4, 5])
print(s1 + s2)  # All NaN! Indexes don't match
```
Solution: Align indexes before operations.

### Best Practices
- Always give meaningful names to Series: `pd.Series(data, name='Salary')`
- Use custom indexes when data has meaningful labels (names, dates)
- Check `dtype` before operations to avoid type errors

### Interview Questions
**Q1. What is a Pandas Series?**
A one-dimensional labeled array that can hold any data type. Like a single column in Excel.

**Q2. What is the default index in a Series?**
Integers starting from 0 (RangeIndex).

**Q3. What is the difference between a Python list and a Pandas Series?**
A Series has labels (index), supports vectorized operations, handles missing values (NaN), and is built on NumPy.

### Quick Revision
A Pandas Series = 1D array + index labels + data type awareness. It's the building block of DataFrames.

---

## 8. DataFrame

### Definition
A **DataFrame** is a two-dimensional, tabular data structure — like a spreadsheet or SQL table. It has rows and columns, where each column is a Series.

```
   Name    Age  Salary
0  Alice   25   50000
1  Bob     30   60000
2  Charlie 28   55000
```

### Syntax

```python
pd.DataFrame(data, index=None, columns=None, dtype=None)
```

### Example 1 — Creating from a Dictionary

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Emma", "David"],
    "Age": [25, 30, 28, 35, 32],
    "City": ["Delhi", "Mumbai", "Bangalore", "Pune", "Chennai"],
    "Salary": [50000, 60000, 55000, 70000, 45000]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
      Name  Age       City  Salary
0    Alice   25      Delhi   50000
1      Bob   30     Mumbai   60000
2  Charlie   28  Bangalore   55000
3     Emma   35       Pune   70000
4    David   32    Chennai   45000
```

**Explanation:**
- Row index is auto-assigned (0, 1, 2...)
- Each key in the dictionary becomes a column
- All lists must have the same length

### Example 2 — Creating from a List of Dictionaries

```python
data = [
    {"Name": "Alice", "Score": 85},
    {"Name": "Bob", "Score": 90},
    {"Name": "Charlie", "Score": 78}
]

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
      Name  Score
0    Alice     85
1      Bob     90
2  Charlie     78
```

### Example 3 — Creating from a NumPy Array

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df)
```

**Output:**
```
   A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
```

### Accessing DataFrame Properties

```python
data = {"Name": ["Alice", "Bob"], "Age": [25, 30], "Salary": [50000, 60000]}
df = pd.DataFrame(data)

print(df.shape)     # (2, 3) — 2 rows, 3 columns
print(df.columns)   # Index(['Name', 'Age', 'Salary'])
print(df.index)     # RangeIndex(start=0, stop=2, step=1)
print(df.dtypes)    # Data type of each column
print(df.size)      # 6 (total elements = rows × columns)
print(df.ndim)      # 2 (two-dimensional)
```

### Accessing Rows and Columns

```python
# Access a single column (returns Series)
print(df['Name'])

# Access multiple columns (returns DataFrame)
print(df[['Name', 'Age']])

# Access a row by index
print(df.loc[0])      # First row by label
print(df.iloc[0])     # First row by position
```

### Modifying a DataFrame

```python
# Add a new column
df['Department'] = ['IT', 'HR']

# Modify existing column
df['Salary'] = df['Salary'] * 1.10  # 10% hike

# Rename columns
df.rename(columns={'Name': 'Employee_Name'}, inplace=True)

# Delete a column
df.drop(columns=['Department'], inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)
```

### Common Errors

**Error 1: `ValueError: arrays must all be same length`**
```python
data = {"Name": ["Alice", "Bob"], "Age": [25]}  # Different lengths!
pd.DataFrame(data)  # Error!
```
Solution: Make sure all columns have the same number of elements.

**Error 2: `KeyError: 'column_name'`**
```python
print(df['Salry'])  # Typo!
```
Solution: Check column names with `df.columns` first.

**Error 3: Adding column with wrong size**
```python
df['New'] = [1, 2, 3, 4, 5, 6]  # More elements than rows
```
Solution: Match the number of rows exactly.

### Best Practices
- Use descriptive column names (no spaces — use underscores: `Employee_Name`)
- Always check `df.shape` and `df.dtypes` after loading data
- Use `inplace=True` carefully — it permanently modifies the DataFrame
- Make a copy before transformation: `df_clean = df.copy()`

### Interview Questions
**Q1. What is a DataFrame?**
A 2D labeled data structure with rows and columns. Like an Excel table. Each column is a Series.

**Q2. What is the difference between a Series and a DataFrame?**
Series is 1D (one column). DataFrame is 2D (multiple columns). A DataFrame is a collection of Series.

**Q3. How do you create an empty DataFrame?**
```python
df = pd.DataFrame()
# or with column names
df = pd.DataFrame(columns=['Name', 'Age', 'Salary'])
```

**Q4. What is `inplace=True`?**
It modifies the DataFrame in memory without creating a new copy. Without it, you must assign: `df = df.drop(...)`.

### Quick Revision
DataFrame = 2D table = collection of Series sharing the same index. The most important data structure in Pandas.

---

## 9. Reading Files

### Definition
Pandas can read data from many file formats. This is how you bring external data into Python for analysis.

---

### 9.1 `pd.read_csv()` — Read CSV Files

#### Definition
Reads a comma-separated values (CSV) file into a DataFrame. CSV is the most common data format in data science.

#### Syntax
```python
pd.read_csv(filepath, sep=',', header=0, index_col=None,
            usecols=None, dtype=None, nrows=None,
            skiprows=None, na_values=None, encoding='utf-8')
```

#### Parameters Explained
| Parameter | Purpose | Example |
|-----------|---------|---------|
| `filepath` | Path to the file | `"data.csv"` |
| `sep` | Separator (default: comma) | `sep='\t'` for TSV |
| `header` | Row number for column names | `header=0` (first row) |
| `index_col` | Column to use as index | `index_col='ID'` |
| `usecols` | Only load specific columns | `usecols=['Name', 'Age']` |
| `nrows` | Load only N rows | `nrows=100` |
| `na_values` | Values to treat as NaN | `na_values=['N/A', 'null']` |
| `encoding` | File encoding | `encoding='utf-8'` |

#### Example — Basic Usage

```python
import pandas as pd

# Read entire CSV
df = pd.read_csv("Walmart_Sales.csv")
print(df.head())
```

#### Example — With Parameters

```python
# Read only first 100 rows, specific columns
df = pd.read_csv(
    "Walmart_Sales.csv",
    usecols=['Store', 'Date', 'Weekly_Sales'],
    nrows=100
)

# Read TSV file (tab-separated)
df = pd.read_csv("data.tsv", sep='\t')

# Handle custom missing values
df = pd.read_csv("data.csv", na_values=['NA', 'N/A', '-', 'null', ''])

# Use first column as index
df = pd.read_csv("data.csv", index_col=0)
```

#### Common Errors

**Error 1: `FileNotFoundError: [Errno 2] No such file or directory`**
```
Cause: Wrong file path
Solution: Use raw strings for Windows: r"C:\Users\data.csv"
         Or use forward slashes: "C:/Users/data.csv"
```

**Error 2: `UnicodeDecodeError`**
```
Cause: File has special characters not compatible with UTF-8
Solution: Try encoding='latin-1' or encoding='cp1252'
```

**Error 3: `ParserError: Error tokenizing data`**
```
Cause: Inconsistent number of columns in rows
Solution: Add error_bad_lines=False (older pandas) or
          on_bad_lines='skip' (pandas 1.3+)
```

#### Best Practices
- Always check `df.head()` and `df.shape` right after loading
- Use `usecols` for large files (loads only what you need)
- Specify `dtype` for columns you know the type of (faster loading)
- Use `nrows` to quickly preview large datasets

---

### 9.2 `pd.read_excel()` — Read Excel Files

#### Definition
Reads Excel files (`.xlsx`, `.xls`) into a DataFrame.

#### Syntax
```python
pd.read_excel(filepath, sheet_name=0, header=0,
              usecols=None, nrows=None, dtype=None, engine=None)
```

#### Parameters Explained
| Parameter | Purpose | Example |
|-----------|---------|---------|
| `sheet_name` | Which sheet to read | `sheet_name='Sales'` or `sheet_name=0` |
| `engine` | File reader engine | `engine='openpyxl'` for `.xlsx` |

#### Example

```python
import pandas as pd

# Read first sheet
df = pd.read_excel("SampleSuperstore.xlsx")

# Read specific sheet by name
df = pd.read_excel("SampleSuperstore.xlsx", sheet_name="Orders")

# Read all sheets at once (returns dict)
all_sheets = pd.read_excel("data.xlsx", sheet_name=None)
print(all_sheets.keys())  # Shows all sheet names

# Read specific sheet
orders = all_sheets['Orders']

# Read old .xls format
df = pd.read_excel("old_data.xls", engine='xlrd')
```

#### Common Errors

**Error 1: `ModuleNotFoundError: Missing optional dependency 'openpyxl'`**
```
Solution: pip install openpyxl
```

**Error 2: `XLRDError: Excel xlsx file; not supported`**
```
Cause: xlrd no longer supports .xlsx (only .xls)
Solution: Use engine='openpyxl' for .xlsx files
```

---

### 9.3 `pd.read_json()` — Read JSON Files

#### Definition
Reads JSON (JavaScript Object Notation) files into a DataFrame. Common in web APIs and NoSQL databases.

#### Syntax
```python
pd.read_json(filepath, orient=None, dtype=True, encoding='utf-8')
```

#### Example

```python
import pandas as pd

# Read JSON file
df = pd.read_json("sample_Data.json")
print(df.head())

# Read JSON from a URL (API)
url = "https://jsonplaceholder.typicode.com/users"
df = pd.read_json(url)
print(df.head())

# Different JSON orientations
# orient='records' -> [{'col': val, ...}, ...]
# orient='columns' -> {'col': {index: val, ...}}
# orient='index'   -> {index: {'col': val, ...}}
df = pd.read_json("data.json", orient='records')
```

---

### 9.4 `pd.read_sql()` — Read from SQL Database

#### Definition
Reads data from a SQL database using a connection.

#### Example

```python
import pandas as pd
import sqlite3

# Create connection
conn = sqlite3.connect("company.db")

# Read entire table
df = pd.read_sql("SELECT * FROM employees", conn)

# Read with WHERE clause
df = pd.read_sql(
    "SELECT name, salary FROM employees WHERE department='IT'",
    conn
)

# Close connection
conn.close()
```

---

### 9.5 Other Reading Functions

```python
# Read HTML tables from a webpage
dfs = pd.read_html("https://en.wikipedia.org/wiki/India")
df = dfs[0]  # First table on the page

# Read from clipboard (Ctrl+C then run this)
df = pd.read_clipboard()

# Read Parquet files (fast columnar format)
df = pd.read_parquet("data.parquet")

# Read fixed-width text file
df = pd.read_fwf("data.txt", widths=[10, 5, 8])
```

### Comparison Table

| Function | Format | When to Use |
|----------|--------|-------------|
| `read_csv()` | .csv, .tsv | Most common data sharing format |
| `read_excel()` | .xlsx, .xls | Business reports, financial data |
| `read_json()` | .json | APIs, web data, NoSQL |
| `read_sql()` | SQL DB | Company databases |
| `read_html()` | HTML | Wikipedia, web tables |
| `read_parquet()` | .parquet | Big Data, fast storage |

---

## 10. Saving Files

### Definition
After cleaning/transforming data, you save it back to a file.

### 10.1 Save to CSV — `df.to_csv()`

```python
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam'],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}
df = pd.DataFrame(data)

# Basic save
df.to_csv("Output.csv", index=False)
# index=False → don't save the row numbers (0, 1, 2...)

# Save with custom separator
df.to_csv("Output.tsv", sep='\t', index=False)

# Save specific columns
df.to_csv("Output.csv", columns=['Name', 'City'], index=False)

# Append to existing CSV
df.to_csv("Output.csv", mode='a', header=False, index=False)
```

### 10.2 Save to Excel — `df.to_excel()`

```python
# Basic save
df.to_excel("Output.xlsx", index=False)

# Specify sheet name
df.to_excel("Output.xlsx", sheet_name="Employees", index=False)

# Save multiple DataFrames to different sheets
with pd.ExcelWriter("multi_sheet.xlsx") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    df2.to_excel(writer, sheet_name="Sheet2", index=False)
```

### 10.3 Save to JSON — `df.to_json()`

```python
# Basic save
df.to_json("Output.json")

# Save as list of records (most readable)
df.to_json("Output.json", orient='records', indent=2)
```

### Common Errors

**Error: `PermissionError: [Errno 13] Permission denied`**
```
Cause: File is already open in Excel
Solution: Close the file in Excel, then run again
```

**Error: `ModuleNotFoundError: openpyxl`**
```
Solution: pip install openpyxl
```

### Best Practices
- Always use `index=False` in `to_csv()` unless you specifically want to save the index
- Use `ExcelWriter` context manager for multiple sheets
- Use `orient='records'` in `to_json()` for human-readable output

---

## 11. Data Exploration

### Definition
Data Exploration is the first step after loading data. You examine the data to understand its structure, size, and content before doing any analysis.

**Golden Rule:** Always explore data BEFORE touching it!

---

### 11.1 `head(n)` — First N Rows

```python
import pandas as pd
df = pd.read_csv("Walmart_Sales.csv")

# Show first 5 rows (default)
print(df.head())

# Show first 10 rows
print(df.head(10))
```

**Output:**
```
   Store        Date  Weekly_Sales  Holiday_Flag  Temperature  Fuel_Price
0      1  05-02-2010    1643690.90             0        42.31       2.572
1      1  12-02-2010    1641957.44             1        38.51       2.548
2      1  19-02-2010    1611968.17             0        39.93       2.514
...
```

**When to use:** Quick preview of data structure after loading.

---

### 11.2 `tail(n)` — Last N Rows

```python
# Show last 5 rows
print(df.tail())

# Show last 3 rows
print(df.tail(3))
```

**When to use:** Check if data ends correctly (no corrupted rows at the bottom).

---

### 11.3 `info()` — Dataset Information

```python
print(df.info())
```

**Output:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6435 entries, 0 to 6434
Data columns (total 8 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   Store         6435 non-null   int64
 1   Date          6435 non-null   object
 2   Weekly_Sales  6435 non-null   float64
 3   Holiday_Flag  6435 non-null   int64
 4   Temperature   6435 non-null   float64
 5   Fuel_Price    6435 non-null   float64
 6   CPI           6435 non-null   float64
 7   Unemployment  6435 non-null   float64
dtypes: float64(5), int64(2), object(1)
memory usage: 402.3+ KB
```

**What to look for:**
- Total rows and columns
- Missing values (where Non-Null Count < total rows)
- Data types (object = string, float64, int64)
- Memory usage

---

### 11.4 `describe()` — Statistical Summary

```python
print(df.describe())
```

**Output:**
```
            Store   Weekly_Sales  Temperature   Fuel_Price
count  6435.000000    6435.000000  6435.000000  6435.000000
mean     23.000000  1046964.877   60.663782       3.358607
std      12.988182   564366.636   18.444933       0.459020
min       1.000000   209986.250   -2.060000       2.472000
25%      12.000000   553350.422   47.460000       2.933000
50%      23.000000   960746.045   62.670000       3.445000
75%      34.000000  1420159.685   74.940000       3.736000
max      45.000000  3818686.450  100.140000       4.468000
```

**What each row means:**
| Statistic | Meaning |
|-----------|---------|
| count | Number of non-null values |
| mean | Average value |
| std | Standard deviation (spread) |
| min | Minimum value |
| 25% | 25th percentile (Q1) |
| 50% | Median (Q2) |
| 75% | 75th percentile (Q3) |
| max | Maximum value |

**Include non-numeric columns:**
```python
df.describe(include='all')     # All columns
df.describe(include='object')  # String columns only
```

---

### 11.5 `shape` — Dimensions

```python
print(df.shape)  # (rows, columns)
```

**Output:** `(6435, 8)` — 6435 rows, 8 columns

```python
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")
```

---

### 11.6 `columns` — Column Names

```python
print(df.columns)
# Output: Index(['Store', 'Date', 'Weekly_Sales', 'Holiday_Flag',
#                'Temperature', 'Fuel_Price', 'CPI', 'Unemployment'],
#               dtype='object')

# Convert to list
print(df.columns.tolist())
# Output: ['Store', 'Date', 'Weekly_Sales', ...]

# Number of columns
print(len(df.columns))
# Output: 8
```

---

### 11.7 `index` — Row Index

```python
print(df.index)
# Output: RangeIndex(start=0, stop=6435, step=1)

# Set a column as index
df.set_index('Store', inplace=True)
print(df.index)
# Output: Int64Index([1, 1, 1, ...], name='Store')

# Reset to default numeric index
df.reset_index(inplace=True)
```

---

### 11.8 `dtypes` — Data Types

```python
print(df.dtypes)
```

**Output:**
```
Store             int64
Date             object
Weekly_Sales    float64
Holiday_Flag      int64
Temperature     float64
Fuel_Price      float64
dtype: object
```

**Why it matters:** Wrong data types cause errors in calculations. `Date` should be `datetime64`, not `object`.

```python
# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)
# Date → datetime64[ns]
```

---

### 11.9 `sample()` — Random Rows

```python
# Get 5 random rows
print(df.sample(5))

# Get 10% of data randomly
print(df.sample(frac=0.1))

# Reproducible random sample
print(df.sample(5, random_state=42))
```

**When to use:** Quick random check of data quality. Test code on small sample.

---

### 11.10 `value_counts()` — Frequency Count

```python
# Count occurrences of each unique value
print(df['Holiday_Flag'].value_counts())
```

**Output:**
```
0    5985
1     450
Name: Holiday_Flag, dtype: int64
```

```python
# Normalized (percentage)
print(df['Holiday_Flag'].value_counts(normalize=True))

# Include NaN in count
print(df['Department'].value_counts(dropna=False))
```

---

### 11.11 `nunique()` — Count Unique Values

```python
# Unique values per column
print(df.nunique())
```

**Output:**
```
Store           45
Date           143
Weekly_Sales  6435
Holiday_Flag     2
```

```python
# Unique values in one column
print(df['Store'].nunique())  # 45
```

---

### 11.12 `unique()` — Get Unique Values

```python
# Get all unique values in a column
print(df['Holiday_Flag'].unique())
# Output: array([0, 1])

print(df['Department'].unique())
# Output: array(['IT', 'HR', 'Finance', 'Marketing'], dtype=object)
```

---

## 12. Data Inspection Methods

### Quick Reference Table

| Method | Returns | Use Case |
|--------|---------|----------|
| `head(n)` | First n rows | Preview data after loading |
| `tail(n)` | Last n rows | Check data end |
| `info()` | Data types + nulls | Diagnose problems |
| `describe()` | Statistics | Understand numeric distribution |
| `shape` | (rows, cols) | Know dataset size |
| `columns` | Column names | See available fields |
| `index` | Row labels | Understand row structure |
| `dtypes` | Type per column | Type validation |
| `sample(n)` | Random n rows | Random quality check |
| `value_counts()` | Frequency table | Category distribution |
| `nunique()` | Unique count | Cardinality check |
| `unique()` | Unique values | See all categories |

### Complete Exploration Workflow

```python
import pandas as pd

df = pd.read_csv("Walmart_Sales.csv")

# Step 1: Quick look
print("=== HEAD ===")
print(df.head())

# Step 2: Size
print("\n=== SHAPE ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Step 3: Data types and missing values
print("\n=== INFO ===")
df.info()

# Step 4: Statistical summary
print("\n=== DESCRIBE ===")
print(df.describe())

# Step 5: Missing values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Step 6: Duplicates
print("\n=== DUPLICATES ===")
print(df.duplicated().sum())
```

---

## 13. Statistical Analysis

### Definition
Using Pandas built-in statistical functions to understand data distribution, central tendency, and spread.

### Core Statistical Functions

```python
import pandas as pd

data = {"Salary": [50000, 60000, 55000, 70000, 45000, 65000, 58000]}
df = pd.DataFrame(data)

# Central Tendency
print(df['Salary'].mean())     # Average: 57571.43
print(df['Salary'].median())   # Middle value: 58000
print(df['Salary'].mode()[0])  # Most frequent: (multiple modes possible)

# Spread
print(df['Salary'].std())      # Standard deviation: 8376.51
print(df['Salary'].var())      # Variance: 70164285.71
print(df['Salary'].min())      # Minimum: 45000
print(df['Salary'].max())      # Maximum: 70000
print(df['Salary'].range())    # Not built-in, use max-min
print(df['Salary'].max() - df['Salary'].min())  # Range: 25000

# Count
print(df['Salary'].count())    # Non-null values: 7
print(df['Salary'].sum())      # Sum: 403000

# Percentiles
print(df['Salary'].quantile(0.25))   # Q1: 52500
print(df['Salary'].quantile(0.50))   # Q2/Median: 58000
print(df['Salary'].quantile(0.75))   # Q3: 63750
```

### Correlation Analysis

```python
data = {
    "Age": [25, 30, 28, 35, 32, 45, 27],
    "Salary": [50000, 60000, 55000, 70000, 65000, 80000, 45000],
    "Experience": [2, 5, 3, 8, 6, 15, 1]
}
df = pd.DataFrame(data)

# Correlation matrix (-1 to +1)
print(df.corr())
```

**Output:**
```
                 Age  Salary  Experience
Age         1.000000   0.976       0.987
Salary       0.976   1.000000     0.981
Experience   0.987    0.981    1.000000
```

**Interpretation:**
- Close to 1.0 → Strong positive correlation (as Age increases, Salary increases)
- Close to -1.0 → Strong negative correlation
- Close to 0 → No correlation

### `cumsum()` and `cumprod()` — Cumulative Statistics

```python
sales = pd.Series([100, 200, 300, 150, 250])

# Cumulative sum (running total)
print(sales.cumsum())
# 0    100
# 1    300
# 2    600
# 3    750
# 4   1000

# Cumulative max/min
print(sales.cummax())
print(sales.cummin())
```

### `pct_change()` — Percentage Change

```python
monthly_sales = pd.Series([1000, 1200, 1100, 1400, 1300])
print(monthly_sales.pct_change())
# Month-over-month % change
# 0         NaN
# 1    0.200000  (20% increase)
# 2   -0.083333  (8.3% decrease)
# 3    0.272727  (27.3% increase)
# 4   -0.071429  (7.1% decrease)
```

### Interview Questions

**Q1. What is the difference between mean and median?**
Mean is the average (sum/count). Median is the middle value when sorted. Median is better for skewed data with outliers.

**Q2. What does `df.corr()` return?**
A correlation matrix showing the relationship (-1 to +1) between all numeric column pairs.

**Q3. What does `std()` tell you?**
Standard deviation measures how spread out values are from the mean. Low std = data is clustered around the mean. High std = data is spread out.

### Quick Revision
Pandas provides powerful statistical functions: `mean()`, `median()`, `std()`, `corr()`, `describe()`. These help understand data distribution in seconds.

---

## 14. Data Selection

### Definition
Data Selection means picking specific rows, columns, or cells from a DataFrame. Pandas offers multiple ways to select data.

---

### 14.1 Selecting Columns

```python
import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["John", "Anaya", "Bob", "Emma", "David"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 45000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)

# Single column → returns Series
print(df['Name'])

# Multiple columns → returns DataFrame
subset = df[['Name', 'Age']]
print(subset)

# All columns EXCEPT some
df_no_id = df.drop(columns=['Employee_ID'])
```

---

### 14.2 `loc[]` — Label-Based Selection

#### Definition
`loc[]` selects rows and columns by their **labels (names)**. It uses row labels (index values) and column names.

#### Syntax
```python
df.loc[row_label, column_label]
df.loc[row_start:row_end, col_start:col_end]
```

**IMPORTANT:** `loc[]` is **inclusive** on both ends of slicing.

#### Examples

```python
# Select single row by index label
print(df.loc[0])         # Row with index 0

# Select a specific cell
print(df.loc[0, 'Name'])  # John

# Select multiple rows
print(df.loc[1:3])        # Rows 1, 2, 3 (all inclusive!)

# Select specific rows AND columns
print(df.loc[0:2, ['Name', 'Salary']])

# Select all rows, specific columns
print(df.loc[:, ['Name', 'Age']])

# Conditional selection with loc
print(df.loc[df['Salary'] > 50000])

# Modify a value using loc
df.loc[0, 'Salary'] = 60000
print(df.loc[0])
```

**Output of `df.loc[0:2, ['Name', 'Salary']]`:**
```
    Name  Salary
0   John   50000
1  Anaya   45000
2    Bob   60000
```

---

### 14.3 `iloc[]` — Position-Based Selection

#### Definition
`iloc[]` selects rows and columns by their **integer positions** (like Python list indexing). Starts from 0.

#### Syntax
```python
df.iloc[row_position, col_position]
df.iloc[row_start:row_end, col_start:col_end]
```

**IMPORTANT:** `iloc[]` is **exclusive** on the end (like Python slicing).

#### Examples

```python
# First row
print(df.iloc[0])

# Last row
print(df.iloc[-1])

# First 3 rows
print(df.iloc[0:3])   # Rows 0, 1, 2 (NOT 3!)

# Specific cell: 3rd row, 2nd column
print(df.iloc[2, 1])  # Bob

# First 3 rows, first 2 columns
print(df.iloc[0:3, 0:2])

# Select rows 0, 2, 4 using list
print(df.iloc[[0, 2, 4]])

# Last 2 rows, last 2 columns
print(df.iloc[-2:, -2:])
```

---

### 14.4 `loc[]` vs `iloc[]` Comparison

| Feature | `loc[]` | `iloc[]` |
|---------|---------|---------|
| Based on | Labels/names | Integer positions |
| End inclusive? | YES | NO |
| Works after set_index? | Uses new labels | Uses positions |
| Better for | Custom indexes, names | Positional slicing |
| Safer? | Less error-prone | More Pythonic |

```python
# When these differ — set a custom index
df.set_index('Name', inplace=True)

# loc uses the label 'John'
print(df.loc['John'])

# iloc uses position 0
print(df.iloc[0])

# Both give same result (first row), but using different identifiers
```

---

### 14.5 `at[]` and `iat[]` — Single Cell Selection

#### Definition
`at[]` and `iat[]` are faster versions for selecting a **single cell**. Same as `loc` and `iloc` but for one value.

```python
# at[] — by label
print(df.at[0, 'Name'])    # John (fast!)

# iat[] — by position
print(df.iat[0, 1])        # John (fast!)

# Modify single cell
df.at[0, 'Salary'] = 75000
```

**When to use:** When you need to access/modify a single cell repeatedly in a loop, `at[]` and `iat[]` are much faster than `loc[]` and `iloc[]`.

### Quick Comparison Table

| Method | Rows | Columns | Speed |
|--------|------|---------|-------|
| `loc[]` | Labels | Labels | Normal |
| `iloc[]` | Positions | Positions | Normal |
| `at[]` | Label | Label | Fastest |
| `iat[]` | Position | Position | Fastest |
| `df['col']` | All | Single col | Fast |
| `df[['col1','col2']]` | All | Multi col | Fast |

---

## 15. Filtering Data

### Definition
Filtering means selecting only the rows that satisfy certain conditions.

### 15.1 Basic Filtering — Comparison Operators

```python
import pandas as pd

data = {
    "Name": ["John", "Anaya", "Bob", "Emma", "David"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 45000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)

# Salary greater than 50000
high_salary = df[df['Salary'] > 50000]
print(high_salary)

# Salary equal to 60000
exact = df[df['Salary'] == 60000]

# NOT equal
not_it = df[df['Department'] != 'IT']

# Greater than or equal
senior = df[df['Age'] >= 30]
```

---

### 15.2 Multiple Conditions with `&` (AND) and `|` (OR)

#### `&` — AND (Both conditions must be True)

```python
# Age > 30 AND Salary > 50000
filtered = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print(filtered)
```

**Output:**
```
   Name  Age Department  Salary
3  Emma   35         IT   70000
4 David   32  Marketing   55000
```

**IMPORTANT:** Always wrap each condition in parentheses `()` when using `&` or `|`.

```python
# WRONG (will cause error)
df[df['Age'] > 30 & df['Salary'] > 50000]

# CORRECT
df[(df['Age'] > 30) & (df['Salary'] > 50000)]
```

#### `|` — OR (At least one condition must be True)

```python
# Age > 30 OR Salary > 50000
filtered = df[(df['Age'] > 25) | (df['Salary'] > 50000)]
print(filtered)
```

---

### 15.3 `~` — NOT (Negation)

```python
# NOT IT department
not_it = df[~(df['Department'] == 'IT')]
print(not_it)

# Same as
not_it = df[df['Department'] != 'IT']
```

---

### 15.4 `isin()` — Filter by Multiple Values

```python
# Select IT or HR department
it_hr = df[df['Department'].isin(['IT', 'HR'])]
print(it_hr)

# Exclude specific values
not_it_finance = df[~df['Department'].isin(['IT', 'Finance'])]
```

---

### 15.5 `between()` — Filter by Range

```python
# Age between 25 and 30 (inclusive)
age_range = df[df['Age'].between(25, 30)]
print(age_range)

# Salary between 50000 and 65000
salary_range = df[df['Salary'].between(50000, 65000)]
```

---

### 15.6 `query()` — Filter with String Query

```python
# Clean, readable syntax
result = df.query("Age > 30 and Salary > 50000")
print(result)

# Using variables in query
min_age = 28
result = df.query("Age > @min_age")

# Multiple conditions
result = df.query("Department == 'IT' or Salary > 60000")
```

**When to use `query()`:** When you have complex conditions and want cleaner, more readable code.

---

### 15.7 String Filtering with `.str`

```python
# Contains
it_emp = df[df['Department'].str.contains('IT')]

# Starts with
j_names = df[df['Name'].str.startswith('J')]

# Ends with
a_names = df[df['Name'].str.endswith('a')]

# Case-insensitive
it_emp = df[df['Department'].str.contains('it', case=False)]

# Not contains
non_it = df[~df['Department'].str.contains('IT')]
```

---

### Common Filtering Errors

**Error 1: `ValueError: The truth value of a Series is ambiguous`**
```python
# WRONG
df[df['Age'] > 30 and df['Salary'] > 50000]

# CORRECT — use & instead of 'and'
df[(df['Age'] > 30) & (df['Salary'] > 50000)]
```

**Error 2: Forgot parentheses around conditions**
```python
# WRONG — crashes!
df[df['Age'] > 30 & df['Salary'] > 50000]

# CORRECT
df[(df['Age'] > 30) & (df['Salary'] > 50000)]
```

### Interview Questions

**Q1. What is the difference between `isin()` and `==`?**
`==` checks equality to ONE value. `isin()` checks membership in a LIST of values.

**Q2. When should you use `query()` vs boolean indexing?**
Use `query()` when conditions are complex and readability matters. Use boolean indexing when you need to work with intermediate masks programmatically.

**Q3. How do you combine more than 2 conditions?**
```python
df[(df['A'] > 0) & (df['B'] < 100) & (df['C'].isin(['X', 'Y']))]
```

---

## 16. Sorting Data

### Definition
Arranging DataFrame rows in a specific order based on column values.

### `sort_values()` — Sort by Column Values

```python
import pandas as pd

data = {
    "Name": ["John", "Anaya", "Bob", "Emma", "David"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 45000, 60000, 70000, 55000],
    "Experience": [2, 5, 3, 8, 6]
}
df = pd.DataFrame(data)

# Sort by single column (ascending — default)
print(df.sort_values(by='Salary'))

# Sort descending
print(df.sort_values(by='Salary', ascending=False))

# Sort by multiple columns
# First sort by Department (A-Z), then by Salary (high to low)
print(df.sort_values(by=['Department', 'Salary'], ascending=[True, False]))

# Sort in place
df.sort_values(by='Age', ascending=True, inplace=True)
df
```

**Output of sort by Age ascending:**
```
    Name  Age Department  Salary  Experience
0   John   25         IT   50000           2
2    Bob   28    Finance   60000           3
1  Anaya   30         HR   45000           5
4  David   32  Marketing   55000           6
3   Emma   35         IT   70000           8
```

### `sort_index()` — Sort by Index

```python
# Sort by row index
df.sort_index(ascending=True, inplace=True)

# Sort by column names
df.sort_index(axis=1, inplace=True)  # axis=1 means columns
```

### `nlargest()` and `nsmallest()` — Top N Values

```python
# Top 3 highest salary employees
print(df.nlargest(3, 'Salary'))

# Bottom 3 salary employees
print(df.nsmallest(3, 'Salary'))

# Top 5 by multiple columns
print(df.nlargest(5, ['Salary', 'Experience']))
```

### Common Errors

**Error: `TypeError: '<' not supported between instances of 'str' and 'float'`**
```
Cause: Column has mixed data types (strings and numbers)
Solution: df['col'] = pd.to_numeric(df['col'], errors='coerce')
```

### Interview Questions

**Q1. What is the difference between `sort_values()` and `sort_index()`?**
`sort_values()` sorts by column data values. `sort_index()` sorts by row/column labels.

**Q2. How to get top 5 salaries?**
```python
df.nlargest(5, 'Salary')
```

### Quick Revision
`sort_values(by='col', ascending=True/False)` — most used. For multiple columns: `sort_values(by=['col1', 'col2'], ascending=[True, False])`.

---

## 17. Data Cleaning

### Definition
Data Cleaning means fixing problems in your dataset so it can be accurately analyzed. Real-world data is ALWAYS messy.

**The 80/20 Rule:** Data scientists spend 80% of their time cleaning data.

### Types of Data Problems

| Problem | Description | Solution |
|---------|-------------|---------|
| Missing values | NaN, None, empty | `fillna()`, `dropna()` |
| Duplicates | Repeated rows | `drop_duplicates()` |
| Wrong data types | Date as string | `astype()`, `to_datetime()` |
| Inconsistent values | "IT", "it", "I.T." | `str.lower()`, `replace()` |
| Outliers | Extreme values | Filter, clip |
| Extra whitespace | " John " | `str.strip()` |

---

## 18. Missing Values

### Definition
Missing values are represented as `NaN` (Not a Number) in Pandas. They occur when data is not recorded, not available, or accidentally deleted.

### 18.1 `isnull()` — Detect Missing Values

```python
import pandas as pd

data = {
    "Employee_ID": [101, None, 103, 104, 105],
    "Name": ["John", None, "Bob", "Emma", "David"],
    "Age": [25, None, 28, 35, 32],
    "Department": ["IT", None, "Finance", "IT", "Marketing"],
    "Salary": [50000, None, 60000, 70000, 55000],
    "Experience": [2, None, 3, 8, 6]
}
df = pd.DataFrame(data)

# Boolean mask — True where value is missing
print(df.isnull())
```

**Output:**
```
   Employee_ID   Name    Age  Department  Salary  Experience
0        False  False  False       False   False       False
1         True   True   True        True    True        True
2        False  False  False       False   False       False
...
```

### 18.2 `isnull().sum()` — Count Missing Values Per Column

```python
print(df.isnull().sum())
```

**Output:**
```
Employee_ID    1
Name           1
Age            1
Department     1
Salary         1
Experience     1
dtype: int64
```

```python
# Total missing in entire DataFrame
print(df.isnull().sum().sum())  # 6

# Percentage missing
print((df.isnull().sum() / len(df)) * 100)

# Columns with any missing values
print(df.columns[df.isnull().any()])
```

### 18.3 `notnull()` — Detect Non-Missing Values

```python
# Returns True where value is NOT missing
print(df.notnull())

# Filter rows where Name is not null
df_clean = df[df['Name'].notnull()]
```

### 18.4 `dropna()` — Remove Missing Values

```python
# Drop ALL rows that have ANY missing value
df_dropped = df.dropna()
print(df_dropped)

# Drop rows where ALL values are missing
df.dropna(how='all', inplace=True)

# Drop rows with missing values in specific columns only
df.dropna(subset=['Name', 'Salary'], inplace=True)

# Drop columns with missing values
df.dropna(axis=1, inplace=True)

# Keep rows with at least N non-null values
df.dropna(thresh=4)  # Keep rows with at least 4 non-null values
```

### 18.5 `fillna()` — Fill Missing Values

```python
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["John", "Anaya", "Bob", "Emma", "David"],
    "Age": [25, None, 28, 35, 32],
    "Department": ["IT", "IT", "Finance", "IT", "Marketing"],
    "Salary": [50000, None, 60000, 70000, 55000],
    "Experience": [2, None, 3, 8, 6]
}
df = pd.DataFrame(data)

# Fill with a constant value
df['Department'].fillna('Unknown', inplace=True)

# Fill with mean (best for numeric data)
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Fill with median (better for skewed data)
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# Fill with mode (most common value)
df['Department'].fillna(df['Department'].mode()[0], inplace=True)

# Forward fill — use previous row's value
df.ffill(inplace=True)

# Backward fill — use next row's value
df.bfill(inplace=True)

# Fill different columns differently
df.fillna({'Age': df['Age'].mean(), 'Salary': 0, 'Department': 'Unknown'}, inplace=True)
```

### 18.6 `interpolate()` — Fill with Estimated Values

```python
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["John", "Alice", None, "Emma", "David", "Sophia"],
    "Age": [25, None, 28, 35, None, 29],
    "Salary": [50000, 45000, None, 70000, 55000, 60000]
}
df = pd.DataFrame(data)

# Linear interpolation — estimates based on surrounding values
df[['Age', 'Salary']] = df[['Age', 'Salary']].interpolate(method='linear')
print(df)
```

**Output:**
```
   Employee_ID   Name        Age  Salary
0          101   John  25.000000   50000
1          102  Alice  26.500000   45000  ← interpolated
2          103   None  28.000000   57500  ← interpolated
3          104   Emma  35.000000   70000
4          105  David  32.000000   55000  ← interpolated
5          106  Sophia  29.000000   60000
```

**When to use:**
- `fillna(mean)` → Random missing data
- `fillna(median)` → Data with outliers
- `ffill/bfill` → Time series data (previous/next reading)
- `interpolate()` → Sequential data (sensor readings, trends)

### Missing Value Strategy Guide

| Column Type | Best Strategy |
|-------------|---------------|
| Numeric (no outliers) | Fill with `mean()` |
| Numeric (with outliers) | Fill with `median()` |
| Category/String | Fill with `mode()[0]` or 'Unknown' |
| Time series | `ffill()` or `interpolate()` |
| Many missing (>50%) | Consider dropping the column |
| Random few missing | `dropna()` if dataset is large |

### Common Errors

**Error 1: `inplace=True` has no effect with `fillna()`**
```python
# WRONG — This creates a NEW DataFrame, doesn't modify df
df['Age'] = df['Age'].fillna(df['Age'].mean(), inplace=True)
# The inplace=True makes it return None, so df['Age'] becomes None!

# CORRECT — Option 1
df['Age'] = df['Age'].fillna(df['Age'].mean())

# CORRECT — Option 2
df['Age'].fillna(df['Age'].mean(), inplace=True)
```

**This is one of the most common Pandas mistakes!**

---

## 19. Duplicate Values

### Definition
Duplicate rows are rows that have identical values in some or all columns.

### 19.1 `duplicated()` — Detect Duplicates

```python
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "John", "Alice"],
    "Department": ["IT", "HR", "Finance", "IT", "HR"],
    "Salary": [50000, 45000, 60000, 50000, 45000]
}
df = pd.DataFrame(data)

# Boolean mask — True for duplicate rows (keeps FIRST occurrence)
print(df.duplicated())
# 0    False
# 1    False
# 2    False
# 3     True   ← duplicate!
# 4     True   ← duplicate!

# Count duplicates
print(df.duplicated().sum())  # 2

# Mark the FIRST occurrence as duplicate (keep last)
print(df.duplicated(keep='last'))

# Mark ALL occurrences as duplicate
print(df.duplicated(keep=False))

# Check duplicates on specific columns
print(df.duplicated(subset=['Name', 'Department']))
```

### 19.2 `drop_duplicates()` — Remove Duplicates

```python
# Remove all duplicate rows (keep first occurrence)
df_clean = df.drop_duplicates()
print(df_clean)

# Keep last occurrence
df_clean = df.drop_duplicates(keep='last')

# Remove if specific columns are duplicated
df_clean = df.drop_duplicates(subset=['Name', 'Department'])

# In-place removal
df.drop_duplicates(inplace=True)
```

### 19.3 `replace()` — Replace Specific Values

```python
# Replace incorrect/inconsistent values
df['Department'].replace('I.T.', 'IT', inplace=True)
df['Department'].replace('Human Resources', 'HR', inplace=True)

# Replace multiple values at once
df['Department'].replace({
    'I.T.': 'IT',
    'Human Resources': 'HR',
    'Fin.': 'Finance'
}, inplace=True)

# Replace across entire DataFrame
df.replace(-999, None, inplace=True)  # Replace sentinel value with NaN
df.replace(np.nan, 0, inplace=True)   # Replace NaN with 0
```

### Interview Questions

**Q1. How do you find duplicate rows?**
```python
df.duplicated().sum()          # Count
df[df.duplicated()]            # Show them
df[df.duplicated(keep=False)]  # Show all copies
```

**Q2. What does `keep` parameter do in `drop_duplicates()`?**
- `keep='first'` (default) → Remove later duplicates, keep first
- `keep='last'` → Remove earlier duplicates, keep last
- `keep=False` → Remove ALL occurrences

### Quick Revision
Duplicates waste memory and skew analysis. `duplicated()` detects, `drop_duplicates()` removes. Always check duplicates during data cleaning.

---

## 20. Data Transformation

### Definition
Data Transformation means changing the structure, shape, or values of a DataFrame to make it suitable for analysis.

### 20.1 Adding Columns

```python
import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["John", "Anaya", "Bob", "Emma", "David"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 45000, 60000, 70000, 55000],
    "Experience": [2, 5, 3, 8, 6]
}
df = pd.DataFrame(data)

# Method 1 — Direct assignment (adds to END)
df["Bonus"] = df["Salary"] * 0.2
print(df.head())

# Method 2 — insert() — add at SPECIFIC position
df.insert(2, "Gender", ["Male", "Female", "Male", "Female", "Male"])
# Parameters: (position, column_name, values)

# Method 3 — Derived column from multiple columns
df["Total_Compensation"] = df["Salary"] + df["Bonus"]

# Method 4 — Conditional column
df["Seniority"] = "Junior"
df.loc[df["Experience"] >= 5, "Seniority"] = "Senior"
```

### 20.2 Dropping Columns

```python
# Drop a single column
df.drop(columns=["Gender"], inplace=True)

# Drop multiple columns
df.drop(columns=["Bonus", "Total_Compensation"], inplace=True)

# Drop by position (axis=1 means columns)
df.drop(df.columns[0], axis=1, inplace=True)  # Drops first column
```

### 20.3 Renaming Columns

```python
# Rename specific columns
df.rename(columns={
    'Name': 'Employee_Name',
    'Dept': 'Department'
}, inplace=True)

# Rename all columns at once
df.columns = ['ID', 'EmpName', 'EmpAge', 'Dept', 'Pay', 'Exp']

# Clean column names (lowercase, remove spaces)
df.columns = df.columns.str.lower().str.replace(' ', '_')
```

### 20.4 Changing Data Types — `astype()`

```python
# Convert column to different data type
df['Employee_ID'] = df['Employee_ID'].astype(str)  # int → string
df['Salary'] = df['Salary'].astype(float)          # int → float
df['Age'] = df['Age'].astype(int)                  # float → int

# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Handle errors during conversion
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
# errors='coerce' → sets invalid values to NaN instead of crashing
```

### 20.5 `map()` — Apply a Mapping to a Column

```python
# Replace values using a dictionary
department_map = {'IT': 'Technology', 'HR': 'Human Resources', 'Finance': 'Accounting'}
df['Department_Full'] = df['Department'].map(department_map)

# Encode categories as numbers
df['Dept_Code'] = df['Department'].map({'IT': 1, 'HR': 2, 'Finance': 3, 'Marketing': 4})
```

### 20.6 Updating Values

```python
# Apply 10% salary increase using loc
df['Salary'] = df['Salary'] * 1.10

# Update specific rows
df.loc[df['Department'] == 'IT', 'Salary'] = df.loc[df['Department'] == 'IT', 'Salary'] * 1.15

# Update a specific cell
df.loc[0, 'Salary'] = 60000
```

---

## 21. GroupBy Operations

### Definition
`groupby()` splits data into groups based on one or more columns and applies a function to each group separately. Think of it like "Group Sales data by Store, then calculate Total Revenue for each Store."

It's one of the most powerful and frequently used Pandas operations.

### How GroupBy Works (Split-Apply-Combine)

```
Original Data          Split              Apply           Combine
--------------         -----              -----           -------
IT  50000              IT   [50000,70000] → sum → 120000  IT     120000
HR  45000              HR   [45000]       → sum → 45000   HR     45000
Finance 60000      →   Finance [60000]   → sum → 60000  Finance  60000
IT  70000
```

### 21.1 Basic GroupBy

```python
import pandas as pd

data = {
    "Name": ["John", "Anaya", "Bob", "Emma", "David"],
    "Age": [25, 30, 28, 35, 32],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 45000, 60000, 70000, 55000],
    "Experience": [2, 5, 3, 8, 6]
}
df = pd.DataFrame(data)

# Total salary per department
grouped = df.groupby("Department")["Salary"].sum()
print(grouped)
```

**Output:**
```
Department
Finance      60000
HR           45000
IT          120000
Marketing    55000
Name: Salary, dtype: int64
```

```python
# Average salary per department
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

# Count employees per department
emp_count = df.groupby("Department")["Name"].count()
print(emp_count)

# Max and min salary per department
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())
```

### 21.2 GroupBy Multiple Columns

```python
# Group by Department AND Seniority
df["Seniority"] = ["Junior", "Senior", "Junior", "Senior", "Mid"]
result = df.groupby(["Department", "Seniority"])["Salary"].mean()
print(result)
```

### 21.3 GroupBy with Multiple Aggregations

```python
# Apply multiple functions at once
result = df.groupby("Department")["Salary"].agg(['sum', 'mean', 'count', 'max', 'min'])
print(result)
```

**Output:**
```
              sum      mean  count    max    min
Department
Finance     60000  60000.0      1  60000  60000
HR          45000  45000.0      1  45000  45000
IT         120000  60000.0      2  70000  50000
Marketing   55000  55000.0      1  55000  55000
```

### 21.4 `transform()` — GroupBy Without Reducing

#### Definition
Unlike `agg()` which reduces groups to single values, `transform()` returns a Series/DataFrame of the **same size as the original** — each row gets the group-level statistic.

```python
# Add a column showing the department average salary
df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
print(df[['Name', 'Department', 'Salary', 'Dept_Avg_Salary']])
```

**Output:**
```
    Name Department  Salary  Dept_Avg_Salary
0   John         IT   50000          60000.0
1  Anaya         HR   45000          45000.0
2    Bob    Finance   60000          60000.0
3   Emma         IT   70000          60000.0
4  David  Marketing   55000          55000.0
```

**Real-world use:** Compare each employee's salary to their department average.
```python
df['Above_Avg'] = df['Salary'] > df['Dept_Avg_Salary']
```

### 21.5 `filter()` — GroupBy with Conditions on Groups

```python
# Keep only departments where average salary > 55000
high_pay_depts = df.groupby('Department').filter(lambda x: x['Salary'].mean() > 55000)
print(high_pay_depts)
```

### 21.6 Iterating Over Groups

```python
# See each group's data
for dept_name, group_df in df.groupby('Department'):
    print(f"\n=== {dept_name} ===")
    print(group_df)
```

### Interview Questions

**Q1. What is `groupby()` and how does it work?**
`groupby()` uses a Split-Apply-Combine strategy. It splits data into groups, applies a function to each group, then combines the results.

**Q2. What is the difference between `agg()` and `transform()`?**
`agg()` reduces each group to a single value (fewer rows). `transform()` returns a value for every original row (same size).

**Q3. How do you group by multiple columns?**
```python
df.groupby(['col1', 'col2'])['col3'].sum()
```

**Q4. How do you reset the group index?**
```python
df.groupby('Department')['Salary'].sum().reset_index()
```

### Quick Revision
`groupby()` is SQL GROUP BY in Python. Pattern: `df.groupby('column')['measure'].agg_function()`. Use `reset_index()` to convert result back to a flat DataFrame.

---

## 22. Aggregations

### Definition
Aggregation means computing a summary statistic (like sum, average, count) for a group or the entire dataset.

### 22.1 Built-in Aggregation Functions

```python
import pandas as pd

data = {
    "Department": ["IT", "HR", "Finance", "IT", "Marketing"],
    "Salary": [50000, 45000, 60000, 70000, 55000],
    "Experience": [2, 5, 3, 8, 6]
}
df = pd.DataFrame(data)

# All built-in aggregation functions
print(df.groupby("Department")["Salary"].sum())       # Total
print(df.groupby("Department")["Salary"].mean())      # Average
print(df.groupby("Department")["Salary"].median())    # Median
print(df.groupby("Department")["Salary"].count())     # Count (non-null)
print(df.groupby("Department")["Salary"].size())      # Size (includes null)
print(df.groupby("Department")["Salary"].max())       # Maximum
print(df.groupby("Department")["Salary"].min())       # Minimum
print(df.groupby("Department")["Salary"].std())       # Standard deviation
print(df.groupby("Department")["Salary"].var())       # Variance
print(df.groupby("Department")["Salary"].first())     # First value in group
print(df.groupby("Department")["Salary"].last())      # Last value in group
```

### 22.2 `agg()` — Multiple Aggregations

```python
# Multiple functions on one column
result = df.groupby("Department")["Salary"].agg(['mean', 'sum', 'count'])

# Different functions on different columns
result = df.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Experience": ["mean", "sum"]
})
print(result)

# Custom function in agg
result = df.groupby("Department")["Salary"].agg(
    Total_Salary=('sum'),
    Avg_Salary=('mean'),
    Max_Salary=('max')
)
```

### 22.3 Named Aggregations (Pandas 0.25+)

```python
# Cleaner syntax with custom column names
result = df.groupby("Department").agg(
    Total_Salary=pd.NamedAgg(column="Salary", aggfunc="sum"),
    Avg_Experience=pd.NamedAgg(column="Experience", aggfunc="mean"),
    Headcount=pd.NamedAgg(column="Salary", aggfunc="count")
)
print(result)
```

---

## 23. Merging Data

### Definition
Merging combines two DataFrames based on one or more **common columns** (keys). Like SQL JOIN operations.

### Setup DataFrames

```python
import pandas as pd

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["John", "Alice", "Bob", "Emma", "David"],
    "Department_ID": [1, 2, 1, 3, 2],
    "Salary": [50000, 45000, 60000, 70000, 55000]
})

departments = pd.DataFrame({
    "Department_ID": [1, 2, 3, 4],
    "Department_Name": ["IT", "HR", "Finance", "Marketing"],
    "Location": ["Delhi", "Mumbai", "Bangalore", "Chennai"]
})
```

### 23.1 `merge()` — Join Two DataFrames

```python
# INNER JOIN — Only matching rows from both tables
df_inner = pd.merge(employees, departments, on="Department_ID", how="inner")
print(df_inner)
```

**Output:**
```
   Employee_ID   Name  Department_ID  Salary Department_Name   Location
0          101   John              1   50000              IT      Delhi
1          103    Bob              1   60000              IT      Delhi
2          102  Alice              2   45000              HR     Mumbai
3          105  David              2   55000              HR     Mumbai
4          104   Emma              3   70000         Finance  Bangalore
```
*Note: Employee 4 (Marketing = ID 4) is not in employees, so dropped in INNER.*

```python
# LEFT JOIN — All rows from LEFT table, match from RIGHT (NaN if no match)
df_left = pd.merge(employees, departments, on="Department_ID", how="left")
print(df_left)

# RIGHT JOIN — All rows from RIGHT table, match from LEFT
df_right = pd.merge(employees, departments, on="Department_ID", how="right")
print(df_right)

# OUTER JOIN — All rows from BOTH tables (NaN where no match)
df_outer = pd.merge(employees, departments, on="Department_ID", how="outer")
print(df_outer)
```

### Visual Guide — Join Types

```
INNER JOIN:         LEFT JOIN:          RIGHT JOIN:         OUTER JOIN:
   A    B              A    B              A    B              A    B
 [===]                [===]              [===]             [=======]
   ↑                    ↑                    ↑                  ↑
Only matching      All of left +       All of right +     Everything
                   matching right      matching left
```

### 23.2 Merge with Different Column Names

```python
# When key columns have different names in each table
df_merged = pd.merge(
    employees,
    departments,
    left_on="Department_ID",    # Column in employees
    right_on="Dept_ID",         # Column in departments
    how="inner"
)
```

### 23.3 Merge on Multiple Columns

```python
df_merged = pd.merge(df1, df2, on=["Year", "Month", "Store_ID"], how="inner")
```

### 23.4 Merge with Suffixes (When Column Names Clash)

```python
# Both tables have 'Name' column
df_merged = pd.merge(df1, df2, on="ID", how="inner",
                     suffixes=('_employee', '_department'))
# Result: 'Name_employee', 'Name_department'
```

### SQL vs Pandas Merge Comparison

| SQL | Pandas |
|-----|--------|
| `INNER JOIN` | `how='inner'` |
| `LEFT JOIN` | `how='left'` |
| `RIGHT JOIN` | `how='right'` |
| `FULL OUTER JOIN` | `how='outer'` |
| `ON table1.col = table2.col` | `on='col'` |
| `ON t1.col1 = t2.col2` | `left_on='col1', right_on='col2'` |

### Common Errors

**Error: `MergeError: No common columns to perform merge on`**
```
Cause: Column names don't match between DataFrames
Solution: Use left_on and right_on parameters
```

**Error: Unexpected duplicate rows after merge**
```
Cause: Many-to-many relationship — both tables have duplicates on the key
Solution: Drop duplicates before merging or use aggregation first
```

### Interview Questions

**Q1. What are the four types of merge/join in Pandas?**
Inner, Left, Right, Outer. Inner keeps only matching rows. Left keeps all left rows. Right keeps all right rows. Outer keeps all rows.

**Q2. What is the difference between `merge()` and `join()`?**
`merge()` joins on column values (like SQL). `join()` joins on index values by default. `merge()` is more flexible and commonly used.

---

## 24. Joining Data

### Definition
`join()` is similar to `merge()` but works primarily with the **index** rather than column values.

### `join()` Method

```python
import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Salary": [50000, 60000, 55000]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    "Department": ["IT", "HR", "Finance"],
    "Location": ["Delhi", "Mumbai", "Pune"]
}, index=[1, 2, 4])

# Join on index
result = df1.join(df2, how='inner')
print(result)
```

**Output:**
```
     Name  Salary Department Location
1   Alice   50000         IT    Delhi
2     Bob   60000         HR   Mumbai
```
*Row 3 (Charlie, index=3) and Row 4 (index=4) dropped in INNER join.*

```python
# Left join (keep all of df1)
result = df1.join(df2, how='left')
# Row 3 (Charlie) will have NaN for Department and Location
```

### When to use `merge()` vs `join()`

| Situation | Use |
|-----------|-----|
| Join on column values | `merge()` |
| Join on index | `join()` |
| Joining with SQL-like thinking | `merge()` |
| Quick join of DataFrames with same index | `join()` |

---

## 25. Concatenation

### Definition
`concat()` stacks DataFrames either **vertically** (row-wise, adding more rows) or **horizontally** (column-wise, adding more columns).

### 25.1 Vertical Concatenation (Default — axis=0)

```python
import pandas as pd

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["John", "Alice", "Bob", "Emma", "David"],
    "Department_ID": [1, 2, 1, 3, 2],
    "Salary": [50000, 45000, 60000, 70000, 55000]
})

departments = pd.DataFrame({
    "Department_ID": [1, 2, 3, 4],
    "Department_Name": ["IT", "HR", "Finance", "Marketing"],
    "Location": ["Delhi", "Mumbai", "Bangalore", "Chennai"]
})

# Stack rows on top of each other (add more rows)
result = pd.concat([employees, departments], axis=0, ignore_index=True)
print(result)
```

**Output:**
```
   Department_ID Department_Name  Employee_ID  Location   Name  Salary
0            1.0             NaN        101.0       NaN   John   50000
1            2.0             NaN        102.0       NaN  Alice   45000
...
5            1.0              IT          NaN     Delhi    NaN     NaN
```
*Columns that don't exist in one DataFrame become NaN.*

### 25.2 Horizontal Concatenation (axis=1)

```python
# Stack columns side by side (add more columns)
result = pd.concat([employees, departments], axis=1, ignore_index=True)
print(result)
```

### 25.3 Practical Use Case — Combining Monthly Data

```python
jan = pd.read_csv("sales_jan.csv")
feb = pd.read_csv("sales_feb.csv")
mar = pd.read_csv("sales_mar.csv")

# Stack all months together
all_months = pd.concat([jan, feb, mar], axis=0, ignore_index=True)
print(f"Total rows: {all_months.shape[0]}")
```

### `merge()` vs `join()` vs `concat()` Comparison

| Method | Purpose | Based On | SQL Equivalent |
|--------|---------|----------|----------------|
| `merge()` | Combine based on column values | Column keys | JOIN |
| `join()` | Combine based on index | Index | JOIN on index |
| `concat()` | Stack DataFrames together | Row/Column order | UNION ALL |

### Common Errors

**Error: Index gets duplicated after concat**
```python
# Problem
pd.concat([df1, df2])  # Index 0,1,2,0,1,2 — duplicated!

# Solution
pd.concat([df1, df2], ignore_index=True)  # New 0,1,2,3,4,5
```

### Interview Questions

**Q1. What is the difference between `concat()` and `merge()`?**
`concat()` simply stacks DataFrames (no key matching). `merge()` joins based on common column values (like SQL JOIN).

**Q2. What does `ignore_index=True` do in `concat()`?**
Resets the row index from 0 after concatenation, preventing duplicate index values.

### Quick Revision
`concat(axis=0)` = UNION (add rows). `concat(axis=1)` = add columns. `merge()` = JOIN on column values. `join()` = JOIN on index values.

---

## 26. Working with Dates

### Definition
Date/time handling is critical in time-series analysis. Pandas has powerful datetime support through `pd.Timestamp` and `datetime64` data type.

### 26.1 Converting to Datetime

```python
import pandas as pd

# Convert string column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Specific format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
# %d=day, %m=month, %Y=4-digit year, %y=2-digit year
# %H=hour, %M=minute, %S=second

# Format reference
# %d  → 05 (day with zero padding)
# %-d → 5  (day without zero padding, Linux/Mac)
# %m  → 02 (month with zero padding)
# %B  → February (full month name)
# %b  → Feb (abbreviated month name)
# %Y  → 2024 (4-digit year)
# %y  → 24  (2-digit year)

# Handle errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# errors='coerce' → invalid dates become NaT (Not a Time)
```

### 26.2 Extracting Date Components

```python
df['Date'] = pd.to_datetime(df['Date'])

# Extract components using .dt accessor
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day_of_Week'] = df['Date'].dt.dayofweek   # 0=Monday, 6=Sunday
df['Day_Name'] = df['Date'].dt.day_name()      # 'Monday', 'Tuesday'...
df['Month_Name'] = df['Date'].dt.month_name()  # 'January', 'February'...
df['Week'] = df['Date'].dt.isocalendar().week  # Week number
df['Quarter'] = df['Date'].dt.quarter          # 1, 2, 3, or 4
df['Hour'] = df['Date'].dt.hour
df['Minute'] = df['Date'].dt.minute
df['Is_Weekend'] = df['Date'].dt.dayofweek >= 5  # True for Saturday/Sunday
```

### 26.3 Date Filtering

```python
# Filter dates
df_2023 = df[df['Date'].dt.year == 2023]
df_q1 = df[df['Date'].dt.quarter == 1]
df_jan = df[df['Date'].dt.month == 1]
df_weekend = df[df['Date'].dt.dayofweek >= 5]

# Filter by date range
start = pd.Timestamp('2023-01-01')
end = pd.Timestamp('2023-12-31')
df_year = df[(df['Date'] >= start) & (df['Date'] <= end)]

# Using between
df_range = df[df['Date'].between('2023-01-01', '2023-06-30')]
```

### 26.4 Date Arithmetic

```python
from datetime import timedelta

# Add days
df['Due_Date'] = df['Date'] + pd.Timedelta(days=30)

# Difference between dates
df['Days_Employed'] = (pd.Timestamp.today() - df['Join_Date']).dt.days
df['Months_Employed'] = (pd.Timestamp.today() - df['Join_Date']).dt.days // 30

# Age calculation
df['Age'] = (pd.Timestamp.today() - df['Birth_Date']).dt.days // 365
```

### 26.5 `resample()` — Time Series Grouping

```python
# If index is a datetime
df.set_index('Date', inplace=True)

# Monthly sum
monthly = df['Sales'].resample('M').sum()   # 'M' = Month end
weekly = df['Sales'].resample('W').sum()    # 'W' = Week
daily = df['Sales'].resample('D').sum()     # 'D' = Day
quarterly = df['Sales'].resample('Q').sum() # 'Q' = Quarter

# Multiple functions
monthly_stats = df['Sales'].resample('M').agg(['sum', 'mean', 'max'])
```

### Date Format Reference

| Format Code | Meaning | Example |
|-------------|---------|---------|
| `%d` | Day (01-31) | 05 |
| `%m` | Month (01-12) | 02 |
| `%Y` | Year (4 digit) | 2024 |
| `%y` | Year (2 digit) | 24 |
| `%B` | Full month name | February |
| `%b` | Short month | Feb |
| `%A` | Full day name | Monday |
| `%a` | Short day | Mon |
| `%H` | Hour (00-23) | 14 |
| `%M` | Minute | 30 |
| `%S` | Second | 45 |

### Common Errors

**Error: `AttributeError: Can only use .dt accessor with datetimelike values`**
```python
# Problem: Column is still object/string type
# Solution: Convert first
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year  # Now works!
```

---

## 27. String Operations

### Definition
The `.str` accessor lets you apply string methods to every element in a Series without loops. Pandas string operations are vectorized and very fast.

### 27.1 Basic String Operations

```python
import pandas as pd

data = {
    "Name": ["  John Smith  ", "alice JONES", "BOB johnson"],
    "Department": ["Information Technology", "HR dept", "Finance & Accounts"]
}
df = pd.DataFrame(data)

# Case conversion
df['Name_lower'] = df['Name'].str.lower()     # "john smith"
df['Name_upper'] = df['Name'].str.upper()     # "JOHN SMITH"
df['Name_title'] = df['Name'].str.title()     # "John Smith"

# Whitespace removal
df['Name_clean'] = df['Name'].str.strip()     # Remove leading/trailing spaces
df['Name_lstrip'] = df['Name'].str.lstrip()   # Remove leading spaces only
df['Name_rstrip'] = df['Name'].str.rstrip()   # Remove trailing spaces only

# Length
df['Name_length'] = df['Name'].str.len()

# Replace
df['Dept_clean'] = df['Department'].str.replace(' dept', '', regex=False)
df['Dept_clean'] = df['Department'].str.replace(r'\s+', '_', regex=True)  # spaces → underscore
```

### 27.2 Searching in Strings

```python
# Contains
df['is_IT'] = df['Department'].str.contains('Technology')
df['is_IT_ci'] = df['Department'].str.contains('technology', case=False)  # Case-insensitive

# Starts/Ends with
df['starts_J'] = df['Name'].str.startswith('J')
df['ends_son'] = df['Name'].str.endswith('son')

# Find position
df['at_pos'] = df['Name'].str.find('o')       # First position of 'o' (-1 if not found)

# Count occurrences
df['vowel_count'] = df['Name'].str.lower().str.count('[aeiou]')  # Regex
```

### 27.3 Extracting from Strings

```python
# Split string into multiple columns
df[['First_Name', 'Last_Name']] = df['Name'].str.strip().str.split(' ', expand=True)

# Get specific part
df['First_Word'] = df['Department'].str.split(' ').str[0]

# Slice string
df['First_3'] = df['Name'].str[:3]    # First 3 characters
df['Last_3'] = df['Name'].str[-3:]    # Last 3 characters

# Extract with regex
df['Numbers'] = df['Code'].str.extract(r'(\d+)')  # Extract numbers from code
```

### 27.4 Replacing with Regex

```python
import re

# Remove all special characters
df['Clean'] = df['Name'].str.replace(r'[^a-zA-Z\s]', '', regex=True)

# Multiple replacements
df['Dept'] = df['Department'].str.replace(r'(IT|I\.T\.)', 'Information Technology', regex=True)
```

### String Method Quick Reference

| Method | What it does | Example |
|--------|-------------|---------|
| `.str.lower()` | Lowercase | `"JOHN" → "john"` |
| `.str.upper()` | Uppercase | `"john" → "JOHN"` |
| `.str.title()` | Title Case | `"john doe" → "John Doe"` |
| `.str.strip()` | Remove spaces | `" hi " → "hi"` |
| `.str.replace(a, b)` | Replace text | `"Hi" → "Hello"` |
| `.str.contains('x')` | Check substring | `True/False` |
| `.str.startswith('x')` | Check prefix | `True/False` |
| `.str.split('x')` | Split by delimiter | `["a", "b"]` |
| `.str.len()` | String length | `5` |
| `.str.extract(pattern)` | Extract with regex | `"A123" → "123"` |
| `.str.count('x')` | Count occurrences | `2` |

---

## 28. Apply Functions

### Definition
`apply()` lets you apply any custom function to a DataFrame column (Series) or each row. Use it when built-in Pandas methods aren't enough.

### 28.1 `apply()` on a Series (Column)

```python
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Emma"],
    "Salary": [50000, 45000, 60000, 70000],
    "Experience": [2, 5, 3, 8]
}
df = pd.DataFrame(data)

# Apply a function to each value in a column
def salary_grade(salary):
    if salary >= 65000:
        return "A"
    elif salary >= 55000:
        return "B"
    elif salary >= 45000:
        return "C"
    else:
        return "D"

df['Grade'] = df['Salary'].apply(salary_grade)
print(df)
```

**Output:**
```
   Name  Salary  Experience Grade
0  John   50000           2     C
1 Alice   45000           5     C
2   Bob   60000           3     B
3  Emma   70000           8     A
```

### 28.2 `apply()` on a DataFrame (Row-wise)

```python
# Apply function across columns (axis=0) or rows (axis=1)

# Example: Calculate total compensation per employee (row-wise)
def total_comp(row):
    return row['Salary'] + (row['Salary'] * row['Experience'] * 0.01)

df['Total_Comp'] = df.apply(total_comp, axis=1)
# axis=1 = apply function to each ROW
# axis=0 = apply function to each COLUMN (default)
```

### 28.3 `apply()` with Multiple Return Values

```python
def salary_info(salary):
    return pd.Series({
        'Grade': 'A' if salary >= 65000 else ('B' if salary >= 55000 else 'C'),
        'Tax': salary * 0.3,
        'Net': salary * 0.7
    })

result = df['Salary'].apply(salary_info)
df = pd.concat([df, result], axis=1)
```

---

## 29. Lambda Functions

### Definition
Lambda is a small, anonymous (nameless) function defined in a single line. Perfect for quick, one-time operations inside `apply()`.

### Syntax
```python
lambda arguments: expression
```

### 29.1 Lambda with `apply()`

```python
import pandas as pd

data = {"Salary": [50000, 45000, 60000, 70000], "Experience": [2, 5, 3, 8]}
df = pd.DataFrame(data)

# Classify salary in one line
df['Grade'] = df['Salary'].apply(lambda x: 'High' if x > 60000 else 'Low')

# Calculate tax
df['Tax'] = df['Salary'].apply(lambda x: x * 0.30)

# Multiple conditions
df['Level'] = df['Experience'].apply(lambda x: 'Senior' if x >= 7 else ('Mid' if x >= 4 else 'Junior'))
```

### 29.2 Lambda in `map()`

```python
# map() applies function to each element
df['Salary_K'] = df['Salary'].map(lambda x: f"₹{x//1000}K")
```

### 29.3 Lambda in `sort_values()`

```python
# Sort by string length
df.sort_values(by='Name', key=lambda x: x.str.len())
```

### 29.4 Lambda vs Named Function

```python
# Named function — use when logic is complex or reused
def classify_salary(x):
    if x >= 70000:
        return 'Platinum'
    elif x >= 60000:
        return 'Gold'
    elif x >= 50000:
        return 'Silver'
    else:
        return 'Bronze'

df['Tier'] = df['Salary'].apply(classify_salary)

# Lambda — use when logic is simple and used once
df['Tier'] = df['Salary'].apply(lambda x:
    'Platinum' if x >= 70000 else
    'Gold' if x >= 60000 else
    'Silver' if x >= 50000 else 'Bronze'
)
```

### 29.5 `applymap()` / `map()` — Apply to Every Cell

```python
# Apply to EVERY cell in the DataFrame (Pandas < 2.0: applymap, >= 2.0: map)
df_numeric = df.select_dtypes(include='number')

# Round all numbers to 2 decimal places
df_rounded = df_numeric.map(lambda x: round(x, 2))

# Check with applymap (older Pandas)
df_numeric = df_numeric.applymap(lambda x: round(x, 2))
```

### Interview Questions

**Q1. What is the difference between `apply()` and `map()`?**
`map()` works on a single Series, element by element. `apply()` works on Series or DataFrame with more control (axis parameter).

**Q2. When should you avoid `apply()`?**
When Pandas built-in functions exist. `apply()` is slower than vectorized operations. Example: Use `df['Salary'] * 0.3` instead of `df['Salary'].apply(lambda x: x * 0.3)`.

**Q3. What is a lambda function?**
An anonymous, single-expression function: `lambda x: x * 2`.

---

## 30. Pivot Tables

### Definition
A Pivot Table reorganizes and summarizes data. It's the Pandas version of Excel's PivotTable. It reshapes data by grouping rows and columns to create a summary table.

### 30.1 `pivot_table()` — Create Pivot Table

```python
import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Finance", "IT"],
    "Location": ["Delhi", "Mumbai", "Delhi", "Delhi", "Bangalore", "Mumbai"],
    "Salary": [50000, 45000, 60000, 42000, 55000, 58000],
    "Experience": [2, 3, 5, 2, 4, 3]
}
df = pd.DataFrame(data)

# Basic pivot table
pivot = pd.pivot_table(
    df,
    values="Salary",       # Values to aggregate
    index="Department",    # Rows
    aggfunc="mean"         # Aggregation function
)
print(pivot)
```

**Output:**
```
                   Salary
Department
Finance          55000.0
HR               43500.0
IT               56000.0
```

```python
# Add columns dimension
pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Location",
    aggfunc="mean"
)
print(pivot)
```

**Output:**
```
Location       Bangalore   Delhi       Mumbai
Department
Finance         55000.0     NaN          NaN
HR                  NaN   42000.0    45000.0
IT                  NaN   55000.0    58000.0
```

```python
# Multiple values and aggregations
pivot = pd.pivot_table(
    df,
    values=["Salary", "Experience"],
    index="Department",
    aggfunc={"Salary": "mean", "Experience": "sum"},
    fill_value=0    # Fill NaN with 0
)

# Add row and column totals
pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Location",
    aggfunc="sum",
    margins=True,    # Add "All" row and column
    margins_name="Total"
)
```

---

## 31. Crosstabs

### Definition
`pd.crosstab()` computes a cross-tabulation (frequency table) of two or more columns. It's like a simplified pivot table for counting.

### 31.1 Basic Crosstab

```python
import pandas as pd

data = {
    "Gender": ["M", "F", "M", "F", "M", "F"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Senior": [True, False, True, True, False, True]
}
df = pd.DataFrame(data)

# How many M/F are in each Department?
ct = pd.crosstab(df['Gender'], df['Department'])
print(ct)
```

**Output:**
```
Department  Finance  HR  IT
Gender
F                 1   1   1
M                 0   1   2
```

```python
# Normalize to percentages
ct_pct = pd.crosstab(df['Gender'], df['Department'], normalize=True) * 100

# Add row/column totals
ct_margins = pd.crosstab(df['Gender'], df['Department'], margins=True)

# Three-way crosstab
ct_3 = pd.crosstab(df['Gender'], [df['Department'], df['Senior']])

# With custom aggregation (values + aggfunc)
ct_salary = pd.crosstab(
    df['Gender'],
    df['Department'],
    values=df['Senior'],
    aggfunc='mean'
)
```

### Pivot Table vs Crosstab

| Feature | `pivot_table()` | `crosstab()` |
|---------|-----------------|--------------|
| Input | DataFrame | Series/arrays |
| Default aggregation | Mean | Count |
| Custom aggregation | Yes | Yes (with values) |
| Best for | Summary statistics | Frequency tables |

---

## 32. Performance Optimization

### Definition
Making Pandas code faster, especially important for large datasets (millions of rows).

### 32.1 Vectorization — Replace Loops with Built-ins

```python
# SLOW — Python loop
for i in range(len(df)):
    df.at[i, 'Tax'] = df.at[i, 'Salary'] * 0.3

# FAST — Vectorized (10-100x faster!)
df['Tax'] = df['Salary'] * 0.3
```

**Rule:** Never loop over rows if a built-in Pandas function exists.

### 32.2 Use Efficient Data Types

```python
import pandas as pd

# Check memory usage
df.info(memory_usage='deep')

# Before optimization
print(df.dtypes)
# Department    object    ← strings take lots of memory

# Convert string columns with few unique values to 'category'
df['Department'] = df['Department'].astype('category')
df['Gender'] = df['Gender'].astype('category')

# Downcast numeric types
df['Age'] = pd.to_numeric(df['Age'], downcast='integer')  # int64 → int8
df['Salary'] = pd.to_numeric(df['Salary'], downcast='float')

# After optimization — memory significantly reduced!
df.info(memory_usage='deep')
```

### 32.3 Load Only What You Need

```python
# Only load needed columns
df = pd.read_csv("large_file.csv", usecols=['Name', 'Salary'])

# Only load N rows
df = pd.read_csv("large_file.csv", nrows=10000)

# Chunked loading for huge files
chunk_size = 10000
all_data = []
for chunk in pd.read_csv("huge_file.csv", chunksize=chunk_size):
    # Process each chunk
    filtered = chunk[chunk['Sales'] > 1000]
    all_data.append(filtered)

df = pd.concat(all_data, ignore_index=True)
```

### 32.4 Use `query()` for Fast Filtering

```python
# Slightly faster on large DataFrames than boolean indexing
df.query("Salary > 50000 and Department == 'IT'")
```

### 32.5 Method Chaining

```python
# Instead of multiple assignments:
df = pd.read_csv("data.csv")
df = df.dropna()
df = df[df['Salary'] > 30000]
df = df.sort_values('Salary', ascending=False)
df = df.reset_index(drop=True)

# Use method chaining (cleaner, more Pythonic):
df = (pd.read_csv("data.csv")
      .dropna()
      .query("Salary > 30000")
      .sort_values('Salary', ascending=False)
      .reset_index(drop=True))
```

### 32.6 `eval()` — Fast Expression Evaluation

```python
# eval() is faster than column arithmetic for large datasets
df['Net'] = df.eval("Salary - Tax")
df['Total'] = df.eval("Salary + Bonus + Allowance")
```

### Performance Tips Summary

| Tip | Speedup |
|-----|---------|
| Use vectorized operations | 10-100x |
| Use `category` dtype for string columns | Memory 5-10x |
| Downcast numeric types | Memory 2-4x |
| Use `query()` | Slightly faster |
| Load only needed columns | IO 2-10x |
| Use `eval()` for arithmetic | Slightly faster |
| Avoid `apply()` when alternatives exist | 10x |

---

## 33. Common Errors

### 33.1 `KeyError`

```python
# Error
df['Salry']  # Typo!
# KeyError: 'Salry'

# Why it happens: Column doesn't exist with that name
# Solution 1: Check columns
print(df.columns)

# Solution 2: Safe access
df.get('Salary')  # Returns None if not found

# Solution 3: Check and handle
if 'Salary' in df.columns:
    print(df['Salary'])
```

### 33.2 `ValueError`

```python
# Error 1: Arrays different length
pd.DataFrame({"A": [1, 2, 3], "B": [4, 5]})
# ValueError: arrays must all be same length

# Error 2: Ambiguous truth value
df[df['A'] > 0 and df['B'] < 5]
# ValueError: The truth value of a Series is ambiguous

# Solution: Use & (AND) or | (OR) with parentheses
df[(df['A'] > 0) & (df['B'] < 5)]
```

### 33.3 `TypeError`

```python
# Error
df['Salary'] + df['Name']  # Adding number to string!
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Solution: Convert types first
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
```

### 33.4 `AttributeError`

```python
# Error
df['Date'].dt.year  # If Date is NOT datetime type!
# AttributeError: Can only use .dt accessor with datetimelike values

# Solution: Convert to datetime first
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year  # Now works!
```

### 33.5 `UnicodeDecodeError`

```python
# Error
pd.read_csv("data.csv")
# UnicodeDecodeError: 'utf-8' codec can't decode byte...

# Solution: Try different encodings
pd.read_csv("data.csv", encoding='latin-1')
pd.read_csv("data.csv", encoding='cp1252')   # Windows
pd.read_csv("data.csv", encoding='utf-8-sig')  # UTF-8 with BOM
```

### 33.6 `SettingWithCopyWarning`

```python
# Warning appears when modifying a copy of a slice
subset = df[df['Department'] == 'IT']
subset['Salary'] = 100000  # SettingWithCopyWarning!

# Solution 1: Use .copy()
subset = df[df['Department'] == 'IT'].copy()
subset['Salary'] = 100000  # No warning

# Solution 2: Use loc on original
df.loc[df['Department'] == 'IT', 'Salary'] = 100000  # Best practice
```

**Why this warning matters:** You might be modifying a view (not the original), and your changes might not stick.

### 33.7 `IndexError`

```python
# Error
df.iloc[1000]  # DataFrame has only 10 rows!
# IndexError: single positional indexer is out-of-bounds

# Solution: Check shape first
print(df.shape)
if len(df) > 1000:
    print(df.iloc[1000])
```

### Quick Error Reference

| Error | Common Cause | Solution |
|-------|-------------|---------|
| `KeyError` | Wrong column name | Check `df.columns` |
| `ValueError` | Wrong data/shape | Check types, use `&` not `and` |
| `TypeError` | Wrong type operation | Convert with `astype()` |
| `AttributeError` | Method on wrong type | Convert column first |
| `UnicodeDecodeError` | Wrong file encoding | Try `encoding='latin-1'` |
| `SettingWithCopyWarning` | Modifying a copy | Use `.copy()` or `loc` |
| `IndexError` | Out of range | Check `len(df)` |

---

## 34. Interview Questions

---

### 🟢 BEGINNER QUESTIONS (Q1–Q20)

---

**Q1. What is Pandas?**

Pandas is an open-source Python library for data manipulation and analysis. It provides two main data structures — Series (1D) and DataFrame (2D) — that make it easy to work with structured tabular data. It was created by Wes McKinney in 2008.

---

**Q2. What are the two main data structures in Pandas?**

1. **Series** — A one-dimensional labeled array (like a single column in Excel).
2. **DataFrame** — A two-dimensional table with rows and columns (like an Excel spreadsheet or SQL table).

---

**Q3. How do you import Pandas?**

```python
import pandas as pd  # 'pd' is the universal shorthand
```

---

**Q4. How do you create a DataFrame?**

```python
# From dictionary
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

# From list of dicts
data = [{"Name": "Alice", "Age": 25}, {"Name": "Bob", "Age": 30}]
df = pd.DataFrame(data)

# From CSV
df = pd.read_csv("file.csv")
```

---

**Q5. What is the difference between a Series and a DataFrame?**

| Feature | Series | DataFrame |
|---------|--------|-----------|
| Dimensions | 1D | 2D |
| Structure | Single column | Multiple columns |
| Type | One data type | Multiple data types |

A DataFrame is a collection of Series (each column is a Series).

---

**Q6. What is `NaN` in Pandas?**

NaN (Not a Number) represents missing or undefined values. It's from NumPy (`np.nan`). Pandas uses it to mark missing data. Functions like `isnull()`, `fillna()`, and `dropna()` deal with NaN values.

---

**Q7. How do you check for missing values?**

```python
df.isnull()             # Boolean mask
df.isnull().sum()       # Count per column
df.isnull().sum().sum() # Total missing values
```

---

**Q8. What is the difference between `loc[]` and `iloc[]`?**

| Feature | `loc[]` | `iloc[]` |
|---------|---------|---------|
| Based on | Labels (column names, index labels) | Integer positions |
| Inclusive end? | YES | NO |
| Example | `df.loc[0, 'Name']` | `df.iloc[0, 1]` |

---

**Q9. How do you read a CSV file in Pandas?**

```python
df = pd.read_csv("filename.csv")
```

Key parameters: `sep`, `header`, `index_col`, `usecols`, `nrows`, `encoding`, `na_values`.

---

**Q10. How do you drop missing values?**

```python
df.dropna()                    # Drop rows with any NaN
df.dropna(how='all')           # Drop only if ALL values are NaN
df.dropna(subset=['Name'])     # Drop where 'Name' is NaN
df.dropna(axis=1)              # Drop columns with NaN
```

---

**Q11. How do you fill missing values?**

```python
df['Col'].fillna(0)                          # Fill with constant
df['Col'].fillna(df['Col'].mean())           # Fill with mean
df['Col'].fillna(df['Col'].median())         # Fill with median
df['Col'].fillna(df['Col'].mode()[0])        # Fill with mode
df.ffill()                                   # Forward fill
df.bfill()                                   # Backward fill
```

---

**Q12. What does `df.info()` return?**

Column names, non-null counts, data types, and memory usage. It's the first method to call after loading data to diagnose problems.

---

**Q13. What does `df.describe()` return?**

Statistical summary of numeric columns: count, mean, std, min, 25th percentile (Q1), 50th percentile (median), 75th percentile (Q3), and max.

---

**Q14. How do you select multiple columns?**

```python
df[['Name', 'Age', 'Salary']]  # Use double brackets → returns DataFrame
```

Single bracket `df['Name']` returns a Series.

---

**Q15. How do you filter rows based on a condition?**

```python
df[df['Salary'] > 50000]

# Multiple conditions
df[(df['Age'] > 25) & (df['Department'] == 'IT')]
```

---

**Q16. How do you add a new column?**

```python
df['Bonus'] = df['Salary'] * 0.10
df.insert(2, 'Gender', ['M', 'F', 'M'])  # At specific position
```

---

**Q17. How do you sort a DataFrame?**

```python
df.sort_values(by='Salary', ascending=False)
df.sort_values(by=['Department', 'Salary'], ascending=[True, False])
```

---

**Q18. How do you remove duplicate rows?**

```python
df.drop_duplicates()                              # All columns
df.drop_duplicates(subset=['Name', 'Department']) # Specific columns
df.duplicated().sum()                             # Count duplicates first
```

---

**Q19. What is `inplace=True`?**

It modifies the DataFrame in memory directly without returning a new object. Without it, you must reassign: `df = df.dropna()`. With it: `df.dropna(inplace=True)`.

---

**Q20. What are the different ways to save a DataFrame?**

```python
df.to_csv("file.csv", index=False)          # CSV
df.to_excel("file.xlsx", index=False)       # Excel
df.to_json("file.json", orient='records')   # JSON
df.to_sql("table_name", connection)         # SQL
df.to_parquet("file.parquet")              # Parquet
```

---

### 🟡 INTERMEDIATE QUESTIONS (Q21–Q40)

---

**Q21. What is the difference between `merge()`, `join()`, and `concat()`?**

- `merge()` — Joins two DataFrames on column values (like SQL JOIN)
- `join()` — Joins on index values (faster for index-based joins)
- `concat()` — Stacks DataFrames vertically (rows) or horizontally (columns)

---

**Q22. Explain the four types of merge (join types).**

- **Inner** — Only matching rows from both DataFrames
- **Left** — All rows from left, matches from right (NaN where no match)
- **Right** — All rows from right, matches from left
- **Outer** — All rows from both (NaN where no match)

---

**Q23. What is `groupby()` and how does it work?**

`groupby()` uses a **Split-Apply-Combine** strategy:
1. **Split** — Divide DataFrame into groups based on column
2. **Apply** — Apply a function to each group
3. **Combine** — Combine results into a new DataFrame

```python
df.groupby("Department")["Salary"].mean()
```

---

**Q24. What is the difference between `agg()` and `transform()`?**

- `agg()` — Reduces each group to a **single value** (fewer rows)
- `transform()` — Returns a value for **every original row** (same size as input)

```python
# agg → one row per department
df.groupby("Dept")["Salary"].agg("mean")

# transform → one value per employee (department mean for their dept)
df["Dept_Avg"] = df.groupby("Dept")["Salary"].transform("mean")
```

---

**Q25. What is the SettingWithCopyWarning and how to fix it?**

It occurs when modifying a copy of a slice. The change may not affect the original.

```python
# Triggers warning
subset = df[df['Dept'] == 'IT']
subset['Salary'] = 100000  # Warning!

# Fix 1: copy()
subset = df[df['Dept'] == 'IT'].copy()

# Fix 2: Direct loc
df.loc[df['Dept'] == 'IT', 'Salary'] = 100000
```

---

**Q26. How do you convert a column to datetime?**

```python
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Invalid → NaT
```

---

**Q27. How do you extract year, month, day from a date column?**

```python
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Day_Name'] = df['Date'].dt.day_name()
df['Quarter'] = df['Date'].dt.quarter
```

---

**Q28. What is `apply()` and when should you use it?**

`apply()` applies a custom function to each row or column. Use it when no built-in Pandas method solves the problem.

```python
df['Grade'] = df['Salary'].apply(lambda x: 'High' if x > 60000 else 'Low')
```

**Avoid apply() when:** Built-in vectorized functions exist (much faster).

---

**Q29. What is `pivot_table()` and how is it different from `groupby()`?**

Both summarize data, but:
- `groupby()` → Returns long-format data
- `pivot_table()` → Returns wide-format table with rows × columns layout

```python
# pivot_table: Departments as rows, Locations as columns
pd.pivot_table(df, values="Salary", index="Department",
               columns="Location", aggfunc="mean")
```

---

**Q30. How do you handle categorical data in Pandas?**

```python
# Convert to category (saves memory)
df['Department'] = df['Department'].astype('category')

# Encode as numbers
df['Dept_Code'] = df['Department'].cat.codes

# Map categories to numbers
df['Dept_Num'] = df['Department'].map({'IT': 1, 'HR': 2})
```

---

**Q31. How do you rename columns?**

```python
df.rename(columns={'Name': 'Employee_Name', 'Dept': 'Department'}, inplace=True)

# Rename all columns
df.columns = ['Col1', 'Col2', 'Col3']

# Clean all column names
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
```

---

**Q32. How do you perform string operations in Pandas?**

Using the `.str` accessor:
```python
df['Name'].str.lower()
df['Name'].str.strip()
df['Name'].str.contains('John')
df['Name'].str.startswith('J')
df['Name'].str.replace('old', 'new')
df['Name'].str.split(' ').str[0]
```

---

**Q33. How do you concatenate DataFrames?**

```python
pd.concat([df1, df2], axis=0, ignore_index=True)  # Vertical (add rows)
pd.concat([df1, df2], axis=1, ignore_index=True)  # Horizontal (add columns)
```

---

**Q34. What is `value_counts()` and when do you use it?**

Returns the frequency of each unique value in a column. Used to understand distribution of categorical data.

```python
df['Department'].value_counts()
df['Department'].value_counts(normalize=True)  # As percentages
```

---

**Q35. How do you reset the index?**

```python
df.reset_index(drop=True, inplace=True)
# drop=True → removes the old index entirely
# drop=False → old index becomes a column
```

---

**Q36. What is `nunique()` vs `unique()`?**

- `nunique()` → Returns the **count** of unique values (integer)
- `unique()` → Returns an **array** of all unique values

```python
df['Department'].nunique()  # 4
df['Department'].unique()   # array(['IT', 'HR', 'Finance', 'Marketing'])
```

---

**Q37. What is method chaining in Pandas?**

Applying multiple operations in sequence using `.` dot notation for cleaner code.

```python
df = (pd.read_csv("data.csv")
      .dropna()
      .query("Salary > 30000")
      .sort_values('Salary', ascending=False)
      .reset_index(drop=True))
```

---

**Q38. How do you use `isin()` for filtering?**

```python
# Select rows where Department is IT or HR
df[df['Department'].isin(['IT', 'HR'])]

# Exclude
df[~df['Department'].isin(['IT', 'Finance'])]
```

---

**Q39. How do you change the data type of a column?**

```python
df['ID'] = df['ID'].astype(str)           # to string
df['Age'] = df['Age'].astype(int)         # to integer
df['Salary'] = df['Salary'].astype(float) # to float
df['Date'] = pd.to_datetime(df['Date'])   # to datetime
df['Dept'] = df['Dept'].astype('category') # to category
```

---

**Q40. What is the difference between `count()` and `size()` in groupby?**

- `count()` → Counts **non-null values** in each group
- `size()` → Counts **all rows** including NaN

```python
df.groupby("Dept")["Name"].count()  # Excludes NaN rows
df.groupby("Dept").size()           # Includes NaN rows
```

---

### 🔴 ADVANCED QUESTIONS (Q41–Q60)

---

**Q41. What is vectorization in Pandas and why is it important?**

Vectorization means applying operations to entire arrays at once (without Python for loops), using NumPy under the hood. It's 10-100× faster than row-by-row iteration.

```python
# Vectorized (FAST)
df['Tax'] = df['Salary'] * 0.30

# Loop (SLOW - avoid this)
for i in range(len(df)):
    df.at[i, 'Tax'] = df.at[i, 'Salary'] * 0.30
```

---

**Q42. What is `pd.crosstab()` and how does it differ from `pivot_table()`?**

`crosstab()` computes a cross-tabulation (frequency table) between two or more columns. It defaults to counting. `pivot_table()` is more general and can aggregate any numeric values.

```python
pd.crosstab(df['Gender'], df['Department'])
# vs
pd.pivot_table(df, values="Salary", index="Gender", columns="Department", aggfunc="mean")
```

---

**Q43. How do you handle MultiIndex DataFrames?**

MultiIndex is multiple levels of indexing. Common in grouped data or time series.

```python
# Create MultiIndex
df = df.set_index(['Department', 'Name'])

# Access with MultiIndex
df.loc['IT']             # All IT rows
df.loc[('IT', 'John')]   # Specific row

# Reset to flat index
df.reset_index(inplace=True)

# After groupby agg
result = df.groupby(['Department', 'Location'])['Salary'].mean()
print(result.index)  # MultiIndex
result = result.reset_index()  # Flatten
```

---

**Q44. What is `pd.eval()` and when should you use it?**

`eval()` evaluates Python expressions efficiently for large DataFrames.

```python
# Faster than regular syntax on large datasets
df['Net'] = df.eval("Salary - Tax - Deductions")
df.query("Salary > @min_salary")  # @ for local variables
```

---

**Q45. What is the difference between `copy()` and view in Pandas?**

A **view** shares memory with the original — changes to one affect the other. A **copy** is an independent DataFrame — changes don't propagate.

```python
view = df[['Name', 'Salary']]   # May be a view
copy = df[['Name', 'Salary']].copy()  # Always a copy

# Modifying copy — safe
copy['Salary'] = 0  # Original df unchanged

# Modifying view — risky, may cause SettingWithCopyWarning
```

---

**Q46. How would you find and handle outliers in Pandas?**

```python
# IQR method
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[(df['Salary'] < lower) | (df['Salary'] > upper)]
print(f"Outliers: {len(outliers)}")

# Remove outliers
df_clean = df[(df['Salary'] >= lower) & (df['Salary'] <= upper)]

# Cap outliers (Winsorizing)
df['Salary'] = df['Salary'].clip(lower=lower, upper=upper)

# Z-score method
from scipy import stats
z_scores = stats.zscore(df['Salary'])
df_clean = df[abs(z_scores) < 3]
```

---

**Q47. How do you efficiently load very large CSV files?**

```python
# Technique 1: Read specific columns only
df = pd.read_csv("big.csv", usecols=['Name', 'Salary'])

# Technique 2: Specify dtypes upfront (avoids type inference)
dtypes = {'Name': str, 'Age': 'int8', 'Salary': 'float32'}
df = pd.read_csv("big.csv", dtype=dtypes)

# Technique 3: Chunked reading
chunks = []
for chunk in pd.read_csv("big.csv", chunksize=100000):
    filtered = chunk[chunk['Sales'] > 1000]
    chunks.append(filtered)
df = pd.concat(chunks, ignore_index=True)
```

---

**Q48. What is `pd.to_numeric()` and when do you use it?**

Converts a column to numeric type. Use when numeric columns are stored as strings.

```python
df['Salary'] = pd.to_numeric(df['Salary'])
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')  # Invalid → NaN
df['Salary'] = pd.to_numeric(df['Salary'], downcast='integer')  # Smallest type
```

---

**Q49. What is `resample()` and when would you use it?**

`resample()` is used with time series data (DatetimeIndex) to change frequency — like converting daily data to monthly.

```python
df.set_index('Date', inplace=True)
df.resample('M').sum()   # Monthly totals
df.resample('Q').mean()  # Quarterly averages
df.resample('W').max()   # Weekly maximums
```

---

**Q50. How do you flatten a MultiIndex in Pandas?**

```python
# After groupby with multiple aggregations
result = df.groupby("Dept").agg({"Salary": ["mean", "sum"]})

# Flatten column MultiIndex
result.columns = ['_'.join(col) for col in result.columns]
# Becomes: 'Salary_mean', 'Salary_sum'

# Flatten row MultiIndex
result.reset_index(inplace=True)
```

---

**Q51. What is `interpolate()` and when should you use it over `fillna()`?**

`interpolate()` estimates missing values based on surrounding data points. Best for sequential/time-series data where trend matters. `fillna()` uses a fixed value.

```python
df['Price'].interpolate(method='linear')  # Fill with interpolated estimate
df['Price'].fillna(df['Price'].mean())    # Fill with overall average
```

---

**Q52. How do you create dummy variables (one-hot encoding) in Pandas?**

```python
# Convert categorical column to binary columns
dummies = pd.get_dummies(df['Department'], prefix='Dept', drop_first=True)
# drop_first=True avoids multicollinearity

# Join back to original DataFrame
df = pd.concat([df, dummies], axis=1)

# OR use directly on full DataFrame
df = pd.get_dummies(df, columns=['Department', 'Gender'])
```

---

**Q53. What is `pd.melt()` and when is it used?**

`melt()` transforms a wide-format DataFrame into long-format. Useful when column names contain data values.

```python
# Wide format:
#    Name  Jan  Feb  Mar
#    John  100  200  150

df_long = pd.melt(df, id_vars=['Name'], var_name='Month', value_name='Sales')
# Long format:
#    Name  Month  Sales
#    John    Jan    100
#    John    Feb    200
#    John    Mar    150
```

---

**Q54. What is `pd.wide_to_long()` vs `melt()`?**

Both reshape wide to long format. `wide_to_long()` is better for data with structured column name patterns (like `Sales_2022`, `Sales_2023`).

```python
df_long = pd.wide_to_long(df, stubnames=['Sales', 'Profit'],
                           i='Name', j='Year', sep='_')
```

---

**Q55. How do you check the memory usage of a DataFrame?**

```python
# Basic
df.info(memory_usage=True)

# Detailed (includes object dtype actual memory)
df.info(memory_usage='deep')

# Per column in bytes
df.memory_usage(deep=True)

# Total in MB
total_mb = df.memory_usage(deep=True).sum() / 1024**2
print(f"Memory: {total_mb:.2f} MB")
```

---

**Q56. What is `nlargest()` and how is it different from `sort_values().head()`?**

Both get top N values, but `nlargest()` is more efficient because it only partially sorts.

```python
# nlargest — faster
df.nlargest(5, 'Salary')

# sort_values + head — slower (full sort)
df.sort_values('Salary', ascending=False).head(5)
```

---

**Q57. How do you use `assign()` for creating new columns?**

`assign()` returns a new DataFrame with added columns — great for method chaining.

```python
# Without assign (breaks chaining)
df['Tax'] = df['Salary'] * 0.3
df['Net'] = df['Salary'] - df['Tax']

# With assign (chainable)
df = (df.assign(Tax=lambda x: x['Salary'] * 0.3)
        .assign(Net=lambda x: x['Salary'] - x['Tax']))
```

---

**Q58. What is the difference between `where()` and `mask()` in Pandas?**

- `where(condition)` — Keeps values where condition is True, replaces with NaN where False
- `mask(condition)` — Opposite: replaces with NaN where condition is True

```python
# Replace low salaries with NaN
df['Salary'].where(df['Salary'] > 50000)     # Keep >50000, rest = NaN
df['Salary'].mask(df['Salary'] < 50000)      # Make <50000 = NaN (same result)

# Replace with specific value
df['Salary'].where(df['Salary'] > 50000, other=0)  # Replace low with 0
```

---

**Q59. How do you merge DataFrames that have columns with the same name but different meanings?**

```python
# Use suffixes to distinguish
merged = pd.merge(df1, df2, on='ID',
                  suffixes=('_employee', '_manager'))
# Result: 'Name_employee', 'Name_manager'
```

---

**Q60. How would you aggregate a custom function that is not available in Pandas?**

```python
# Define custom aggregation function
def salary_range(x):
    return x.max() - x.min()

def coefficient_of_variation(x):
    return x.std() / x.mean() * 100

# Use in agg
result = df.groupby("Department")["Salary"].agg([
    "mean",
    "std",
    salary_range,
    coefficient_of_variation
])
```

---

## 35. Practice Exercises

> **Instructions:** Try these without looking at solutions. Use the datasets you've learned to create or download sample data.

### 🟢 EASY EXERCISES (E1–E20)

**E1.** Create a DataFrame with 5 employees: Name, Age, Department, Salary.

**E2.** Load a CSV file and display its first 10 rows, last 5 rows, and shape.

**E3.** Find the number of missing values in each column of any DataFrame.

**E4.** Select only the 'Name' and 'Salary' columns from the employee DataFrame.

**E5.** Filter employees with Salary > 50,000.

**E6.** Sort employees by Salary in descending order.

**E7.** Add a 'Bonus' column that is 15% of Salary.

**E8.** Fill all missing values in the 'Department' column with 'Unknown'.

**E9.** Drop all rows where 'Age' is missing.

**E10.** Count the number of employees in each department using `value_counts()`.

**E11.** Rename the column 'Dept' to 'Department'.

**E12.** Find the maximum and minimum salary in the DataFrame.

**E13.** Count the number of duplicate rows.

**E14.** Convert the 'Join_Date' column from string to datetime format.

**E15.** Create a Series of monthly sales figures for 12 months with month names as index.

**E16.** Filter employees who are either in IT or Finance department.

**E17.** Save the cleaned DataFrame to a new CSV file without the index column.

**E18.** Use `describe()` to see statistical summary of the DataFrame.

**E19.** Find the unique departments in the DataFrame.

**E20.** Change the 'Salary' column data type to float.

---

### 🟡 MEDIUM EXERCISES (M1–M20)

**M1.** Calculate the average salary per department using `groupby()`.

**M2.** Find the department with the highest total salary bill.

**M3.** Add a 'Salary_Grade' column: 'A' if Salary >= 70000, 'B' if >= 50000, else 'C'.

**M4.** Create a pivot table showing average Salary by Department and Location.

**M5.** Merge an employees table with a departments table on Department_ID (inner join).

**M6.** Concatenate three months of sales data (Jan, Feb, Mar) into one DataFrame.

**M7.** Find the top 5 highest-paid employees using `nlargest()`.

**M8.** Use `groupby()` + `transform()` to add a column showing each employee's salary compared to their department average.

**M9.** Handle outliers in the Salary column using the IQR method.

**M10.** Extract the year, month, and day from a 'Date' column.

**M11.** Filter only weekend data from a time-series DataFrame.

**M12.** Use `apply()` with a custom function to categorize experience levels.

**M13.** Replace inconsistent department names ('I.T.', 'it', 'I T') all with 'IT'.

**M14.** Find employees whose Name starts with 'A' using string methods.

**M15.** Create a crosstab showing the count of employees by Gender and Department.

**M16.** Use `interpolate()` to fill missing values in a time-series price column.

**M17.** Left join employees with departments and identify which employees have no department.

**M18.** Use `groupby().agg()` to compute the sum, mean, and count of Salary per Department simultaneously.

**M19.** Use `isin()` to filter data for specific store IDs from a list.

**M20.** Downcast numeric columns to reduce memory usage.

---

### 🔴 ADVANCED EXERCISES (A1–A20)

**A1.** Load a large CSV in chunks and compute the total sales per store without loading the entire file at once.

**A2.** Read multiple Excel sheets into separate DataFrames, process them, and combine into one.

**A3.** Create a function that automatically detects and handles missing values differently based on column type (numeric vs categorical).

**A4.** Build a full data cleaning pipeline: load → rename columns → fix dtypes → handle missing → remove duplicates → save.

**A5.** Use `pd.wide_to_long()` or `melt()` to reshape a wide-format dataset into long format.

**A6.** Perform a self-join (merge a DataFrame with itself) to find employees in the same department.

**A7.** Implement one-hot encoding using `pd.get_dummies()` for a machine learning-ready dataset.

**A8.** Use MultiIndex to create a DataFrame indexed by (Department, Year) and compute year-over-year salary growth per department.

**A9.** Create a rolling 7-day average on a daily sales time series.

**A10.** Build a summary report using method chaining: load → clean → group → aggregate → sort → save.

**A11.** Detect outliers using Z-score and replace them with the column median (not drop).

**A12.** Parse a messy date column that has mixed formats ('2023-01-15', '15/01/2023', 'Jan 15, 2023') into a consistent datetime.

**A13.** Use `pd.eval()` to create 5 new columns in a large DataFrame without temporary variables.

**A14.** Write a function that creates a formatted summary table (department | avg salary | headcount | % above avg).

**A15.** Load Walmart sales data, compute monthly revenue per store, find the best and worst performing store in each month.

**A16.** Use `groupby().apply()` with a custom function to compute a percentile rank within each department.

**A17.** Create a correlation heatmap data (correlation matrix) between all numeric features.

**A18.** Use category dtype to reduce memory of a 1M+ row DataFrame and measure the memory before/after.

**A19.** Merge three DataFrames in sequence (employees → departments → salaries) and create a complete employee profile table.

**A20.** Perform a fuzzy string match to identify and merge duplicate entries with slightly different names ('John Smith', 'Jon Smith', 'JOHN SMITH').

---

## 36. Pandas Cheatsheet

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        🐼 PANDAS CHEATSHEET                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

📦 IMPORT & CREATE
  import pandas as pd
  pd.Series([1,2,3])
  pd.DataFrame({'A': [1,2], 'B': [3,4]})
  pd.DataFrame(list_of_dicts)

📂 FILE OPERATIONS
  pd.read_csv("file.csv")                    Read CSV
  pd.read_excel("file.xlsx")                 Read Excel
  pd.read_json("file.json")                  Read JSON
  pd.read_sql("SELECT *...", conn)           Read SQL
  df.to_csv("file.csv", index=False)         Save CSV
  df.to_excel("file.xlsx", index=False)      Save Excel
  df.to_json("file.json", orient='records')  Save JSON

🔍 EXPLORATION
  df.head(n)          First n rows (default 5)
  df.tail(n)          Last n rows
  df.info()           Data types + nulls + memory
  df.describe()       Statistical summary
  df.shape            (rows, columns)
  df.columns          Column names
  df.dtypes           Data types per column
  df.sample(n)        n random rows
  df.nunique()        Unique count per column
  df.value_counts()   Frequency count

🎯 SELECTION
  df['col']                   Single column → Series
  df[['col1','col2']]         Multiple columns → DataFrame
  df.loc[row, col]            By label
  df.iloc[row, col]           By position
  df.at[row, 'col']           Single cell by label (fast)
  df.iat[row, col]            Single cell by position (fast)

🔎 FILTERING
  df[df['col'] > value]               Compare
  df[(cond1) & (cond2)]               AND
  df[(cond1) | (cond2)]               OR
  df[~(cond)]                         NOT
  df[df['col'].isin([a, b, c])]      Is in list
  df[df['col'].between(low, high)]   In range
  df.query("col > value")             String query

🧹 CLEANING
  df.isnull()                    Boolean mask of nulls
  df.isnull().sum()              Count nulls per column
  df.dropna()                    Drop rows with any null
  df.dropna(subset=['col'])      Drop where specific col is null
  df.fillna(value)               Fill nulls with value
  df.fillna(df['col'].mean())    Fill with mean
  df.ffill()                     Forward fill
  df.bfill()                     Backward fill
  df.interpolate()               Linear interpolation
  df.duplicated().sum()          Count duplicates
  df.drop_duplicates()           Remove duplicates
  df.replace('old', 'new')       Replace values

🔧 TRANSFORMATION
  df['new'] = df['col'] * 2          Add column
  df.insert(pos, 'col', values)      Add at position
  df.drop(columns=['col'])           Remove column
  df.rename(columns={'old':'new'})   Rename column
  df['col'].astype('int')            Change dtype
  df['col'].astype('category')       To category (memory)
  pd.to_datetime(df['col'])          To datetime
  pd.to_numeric(df['col'])           To numeric

📊 SORTING
  df.sort_values('col')              Ascending
  df.sort_values('col', ascending=False)  Descending
  df.sort_values(['col1','col2'])    Multi-column sort
  df.nlargest(n, 'col')             Top n rows
  df.nsmallest(n, 'col')            Bottom n rows

📈 STATISTICS
  df['col'].mean()          Average
  df['col'].median()        Median
  df['col'].mode()          Most frequent
  df['col'].std()           Standard deviation
  df['col'].sum()           Sum
  df['col'].min()           Minimum
  df['col'].max()           Maximum
  df['col'].count()         Non-null count
  df['col'].quantile(0.75)  75th percentile
  df.corr()                 Correlation matrix

🔗 GROUPBY
  df.groupby('col')['measure'].sum()    Group + sum
  df.groupby('col')['m'].agg(['mean','sum','count'])
  df.groupby('col')['m'].transform('mean')  Group without reducing
  df.groupby('col').filter(lambda x: x['val'].mean() > 100)

🔀 COMBINING
  pd.merge(df1, df2, on='col', how='inner')   INNER JOIN
  pd.merge(df1, df2, on='col', how='left')    LEFT JOIN
  pd.merge(df1, df2, on='col', how='right')   RIGHT JOIN
  pd.merge(df1, df2, on='col', how='outer')   OUTER JOIN
  df1.join(df2, how='left')                   JOIN on index
  pd.concat([df1, df2], axis=0, ignore_index=True)  Add rows
  pd.concat([df1, df2], axis=1)               Add columns

📅 DATES
  pd.to_datetime(df['col'])        Convert to datetime
  df['Date'].dt.year               Extract year
  df['Date'].dt.month              Extract month
  df['Date'].dt.day                Extract day
  df['Date'].dt.day_name()         Day name ('Monday')
  df['Date'].dt.quarter            Quarter (1-4)
  df.set_index('Date').resample('M').sum()  Monthly totals

📝 STRINGS (.str accessor)
  df['col'].str.lower()             Lowercase
  df['col'].str.upper()             Uppercase
  df['col'].str.strip()             Remove whitespace
  df['col'].str.replace('a','b')   Replace
  df['col'].str.contains('x')      Contains?
  df['col'].str.startswith('A')    Starts with?
  df['col'].str.split(' ')         Split
  df['col'].str.len()              Length

⚡ APPLY / LAMBDA
  df['col'].apply(func)               Apply function
  df['col'].apply(lambda x: x * 2)   Lambda
  df.apply(func, axis=1)             Row-wise
  df['col'].map({'A': 1, 'B': 2})   Map values

🔲 PIVOT & CROSSTAB
  pd.pivot_table(df, values='v', index='r', columns='c', aggfunc='mean')
  pd.crosstab(df['A'], df['B'])       Frequency table
  pd.crosstab(df['A'], df['B'], normalize=True)  Percentages

🚀 PERFORMANCE
  df['col'].astype('category')        Less memory for strings
  pd.to_numeric(df['col'], downcast='integer')  Smaller int type
  df = pd.read_csv("f.csv", usecols=['A','B'])  Load less
  df.eval("A + B")                    Fast expression
  df.query("A > 100")                 Fast filter
```

---

## 37. Final Summary

### One-Day-Before-Interview Revision Sheet

---

#### 🔑 The 5 Most Important Concepts

1. **DataFrame** — The core data structure. 2D table. Each column is a Series.
2. **loc vs iloc** — Labels vs positions. `loc` inclusive, `iloc` exclusive end.
3. **GroupBy** — Split-Apply-Combine. SQL GROUP BY equivalent.
4. **merge() join types** — Inner (matching only), Left (all left), Right (all right), Outer (everything).
5. **Missing Values** — `isnull()` detects, `dropna()` removes, `fillna()` fills, `interpolate()` estimates.

---

#### 🚨 Top 10 Common Mistakes

1. Using `and` instead of `&` for multiple conditions → Use `& | ~`
2. Forgetting parentheses: `df[df['A']>0 & df['B']<5]` → Must be: `df[(df['A']>0) & (df['B']<5)]`
3. `fillna(value, inplace=True)` with assignment → Use EITHER inplace OR assignment, not both
4. Reading `.xlsx` with `xlrd` → Use `engine='openpyxl'` for `.xlsx`
5. `apply()` instead of vectorized operations → Much slower, use built-ins
6. Not using `index=False` in `to_csv()` → Saves ugly extra row number column
7. Modifying a slice without `.copy()` → Causes SettingWithCopyWarning
8. Not checking `df.dtypes` after loading → Date as object, number as string
9. Duplicate index after `concat()` → Always use `ignore_index=True`
10. `df['col'].str.method()` without first checking dtype is string → Will fail on numeric

---

#### 📌 Essential One-Liners

```python
# Load and preview
df = pd.read_csv("data.csv"); df.head()

# Find missing values
df.isnull().sum()

# Clean missing: fill numeric with mean, categorical with mode
df = df.fillna({c: df[c].mean() if df[c].dtype != 'O' else df[c].mode()[0] for c in df.columns})

# Find and remove duplicates
df[df.duplicated()]; df.drop_duplicates(inplace=True)

# Group and aggregate
df.groupby("Dept")["Salary"].agg(["mean","sum","count"])

# Filter multiple values
df[df["Dept"].isin(["IT","Finance"])]

# Sort and get top 5
df.nlargest(5, "Salary")

# Convert to datetime and extract year
df["Date"] = pd.to_datetime(df["Date"]); df["Year"] = df["Date"].dt.year

# Full inner join
merged = pd.merge(df1, df2, on="ID", how="inner")

# Save cleaned data
df.to_csv("cleaned.csv", index=False)
```

---

#### 📊 Data Workflow Map

```
RAW DATA
   │
   ▼
LOAD          → pd.read_csv / read_excel / read_json / read_sql
   │
   ▼
EXPLORE       → head(), info(), describe(), shape, dtypes, value_counts()
   │
   ▼
CLEAN         → dropna(), fillna(), drop_duplicates(), replace(), astype()
   │
   ▼
TRANSFORM     → new columns, rename, sort, groupby, merge, concat
   │
   ▼
ANALYZE       → groupby, pivot_table, corr(), statistical functions
   │
   ▼
VISUALIZE     → matplotlib / seaborn / plotly (outside Pandas scope)
   │
   ▼
SAVE          → to_csv(), to_excel(), to_json(), to_sql()
```

---

#### 🎯 Key Method Families

| Goal | Methods |
|------|---------|
| **Load data** | `read_csv`, `read_excel`, `read_json`, `read_sql` |
| **Explore** | `head`, `tail`, `info`, `describe`, `shape`, `dtypes` |
| **Select** | `loc`, `iloc`, `at`, `iat`, `df['col']`, `df[['c1','c2']]` |
| **Filter** | `df[cond]`, `isin`, `between`, `query`, `.str.contains` |
| **Clean** | `dropna`, `fillna`, `drop_duplicates`, `replace`, `interpolate` |
| **Transform** | `assign`, `apply`, `map`, `rename`, `drop`, `insert`, `astype` |
| **Sort** | `sort_values`, `sort_index`, `nlargest`, `nsmallest` |
| **Group** | `groupby`, `agg`, `transform`, `filter` |
| **Combine** | `merge`, `join`, `concat` |
| **Date** | `to_datetime`, `.dt.year`, `.dt.month`, `resample` |
| **String** | `.str.lower`, `.str.strip`, `.str.contains`, `.str.split` |
| **Save** | `to_csv`, `to_excel`, `to_json`, `to_sql` |

---

*Created with ❤️ for complete Pandas mastery — from scratch to professional level.*

*These notes cover everything needed to confidently perform data analysis, pass interviews, and work on real-world data science projects.*
