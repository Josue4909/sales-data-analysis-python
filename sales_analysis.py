import pandas as pd
import matplotlib.pyplot as plt

# Example dataset
data = {
    "Product": ["Cooler", "Water Bottle", "Lunch Box", "Cooler", "Water Bottle"],
    "Sales": [120, 90, 60, 150, 110],
    "Month": ["Jan", "Jan", "Jan", "Feb", "Feb"]
}

df = pd.DataFrame(data)

# Total sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()

print("Sales by Product:")
print(sales_by_product)

# Plot sales
sales_by_product.plot(kind="bar", title="Sales by Product")
plt.show()
