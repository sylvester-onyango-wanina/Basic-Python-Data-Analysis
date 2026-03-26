import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("sales_data.csv")


# Calculate total revenue
total_revenue = df['Revenue ($)'].sum()
print('Total Revenue:$', total_revenue)

# Find best-selling product (by quantity sold)
best_selling_product = df.groupby('Product')['Quantity Sold'].sum().idxmax()
best_selling_quantity = df.groupby('Product')['Quantity Sold'].sum().max()

# Identify day with highest sales revenue
best_day = df.groupby('Date')['Revenue ($)'].sum().idxmax()
highest_day_revenue = df.groupby('Date')['Revenue ($)'].sum().max()

# Save summary to a text file
with open("sales_summary.txt", "w", encoding="utf-8") as file:
    file.write(f"Sales Summary\n")
    file.write(f"---------------------------\n")
    file.write(f"Total Revenue: ${total_revenue:,.2f}\n")
    file.write(f"Best-Selling Product: {best_selling_product} ({best_selling_quantity} units)\n")
    file.write(f"Highest Revenue Day: {best_day} (${highest_day_revenue:,.2f})\n")


# Print summary
print("Sales Analysis Summary")
print("---------------------------")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Best-Selling Product: {best_selling_product} ({best_selling_quantity} units)")
print(f"Highest Revenue Day: {best_day} (${highest_day_revenue:,.2f})")

# 🎯 Bonus: Sales trend visualization
daily_sales = df.groupby('Date')['Revenue ($)'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['Date'], daily_sales['Revenue ($)'], marker='o', color='teal')
plt.title('Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_trend.png")  # Save the figure
plt.show()
