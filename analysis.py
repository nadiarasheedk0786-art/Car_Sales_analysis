import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("car_sales.csv")

# Combine Manufacturer + Model for clear labels
df["Car_Model"] = df["Manufacturer"] + " " + df["Model"]

# Sort by sales and take top 10 models
top_models = df.sort_values(by="Sales_in_thousands", ascending=False).head(10)

# Bar chart
plt.figure(figsize=(10, 5))
plt.bar(top_models["Car_Model"], top_models["Sales_in_thousands"])
plt.title("Top 10 Selling Car Models")
plt.xlabel("Car Model")
plt.ylabel("Sales (in thousands)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_10_car_models.png", dpi=200)
plt.show()

# Pie chart (Top 5 models distribution)
top5 = top_models.head(5)

plt.figure(figsize=(6, 6))
plt.pie(
    top5["Sales_in_thousands"],
    labels=top5["Car_Model"],
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Sales Distribution Among Top 5 Car Models")
plt.axis("equal")  # Makes the pie a perfect circle
plt.savefig("sales_distribution_pie.png", dpi=200)
plt.show()

