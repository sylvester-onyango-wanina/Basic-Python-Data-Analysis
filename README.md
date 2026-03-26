# Sales Data Analysis

A Python script that analyses sales data from a CSV file, generates a summary report, and produces a daily revenue trend chart.

## Features

- Calculates total revenue across all records
- Identifies the best-selling product by quantity sold
- Finds the day with the highest sales revenue
- Saves a summary report to a text file (`sales_summary.txt`)
- Generates and saves a daily revenue trend chart (`sales_trend.png`)

## Requirements

- Python 3.7+
- pandas
- matplotlib

Install dependencies with:

```bash
pip install pandas matplotlib
```

## Input

The script expects a CSV file named `sales_data.csv` in the same directory, with at least the following columns:

| Column | Description |
|---|---|
| `Date` | Date of the sale |
| `Product` | Product name |
| `Quantity Sold` | Number of units sold |
| `Revenue ($)` | Revenue generated |

## Usage

```bash
python sales_analysis.py
```

## Output

| File | Description |
|---|---|
| `sales_summary.txt` | Text file with total revenue, best-selling product, and highest revenue day |
| `sales_trend.png` | Line chart of daily revenue over time |

Sample console output:

```
Total Revenue: $ 45230.00
Sales Analysis Summary
---------------------------
Total Revenue: $45,230.00
Best-Selling Product: Widget A (1,240 units)
Highest Revenue Day: 2024-03-15 ($3,850.00)
```

## Project Structure

```
.
├── sales_analysis.py
├── sales_data.csv
├── sales_summary.txt   # generated on run
└── sales_trend.png     # generated on run
```
