import matplotlib.pyplot as plt
import numpy as np
import random

# Generate random prices and sales data for six bakery products
products = ["Croissant", "Baguette", "Cupcake", "Danish", "Eclair", "Muffin"]

product_prices = []
product_sales = []

for _ in range(6):
    prices = np.random.normal(loc=3.5, scale=0.5, size=12)
    sales = np.random.normal(loc=100, scale=10, size=12)
    product_prices.append(prices)
    product_sales.append(sales)

# Create the figure and axis objects
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
axes = axes.flatten()

# Plot the changing price to sales relationship for each product
for i in range(6):
    axes[i].scatter(
        product_prices[i], product_sales[i], marker="o", color="b", alpha=0.7
    )
    axes[i].set_xlabel("Price")
    axes[i].set_ylabel("Sales")
    axes[i].set_title(products[i])

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plots
plt.show()
