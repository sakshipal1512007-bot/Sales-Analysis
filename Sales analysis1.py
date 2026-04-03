# sales_analysis_final.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 0. Create Sample Dataset
# -----------------------------
data = {
    "OrderID": list(range(1, 11)),
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Laptop",
                "Phone", "Tablet", "Laptop", "Headphones", "Phone"],
    "Region": ["North", "South", "East", "West", "North",
               "South", "East", "West", "North", "South"],
    "Date": pd.date_range("2024-01-01", periods=10, freq="MS"),  # Month Start
    "Quantity": [2, 5, 3, 4, 1, 6, 2, 3, 4, 5],
    "Price": [800, 500, 300, 100, 850, 520, 310, 830, 120, 510]
}

df_sample = pd.DataFrame(data)
df_sample.to_csv("sales_data.csv", index=False)
print("✅ Sample dataset created: sales_data.csv")

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]

# KPIs
total_revenue = df["Revenue"].sum()
average_order_value = df.groupby("OrderID")["Revenue"].sum().mean()
top_regions = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

# Print KPIs
print("\n📊 KPI Summary")
print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Average Order Value: {average_order_value:,.2f}")
print("\nTop Regions:\n", top_regions)
print("\nTop Products:\n", top_products)

# Seasonality
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Revenue"].sum()

# -----------------------------
# 2. Attractive Visualizations
# -----------------------------
sns.set_theme(style="darkgrid", palette="muted")

# Monthly Trend
plt.figure(figsize=(10,6))
monthly_sales.plot(kind="line", marker="o", linewidth=2, color="dodgerblue")
plt.title("Monthly Revenue Trend", fontsize=16, fontweight="bold")
plt.ylabel("Revenue", fontsize=12)
plt.xlabel("Month", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("monthly_trend.png", dpi=300)
plt.close