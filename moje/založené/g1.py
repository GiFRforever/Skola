import matplotlib.pyplot as plt
import numpy as np
import random

# Czech names of months
months = [
    "leden",
    "únor",
    "březen",
    "duben",
    "květen",
    "červen",
    "červenec",
    "srpen",
    "září",
    "říjen",
    "listopad",
    "prosinec",
]

# Generate random sales and expenses data for two years
year_1_sales = [random.randint(10000, 30000) for _ in range(12)]
year_1_expenses = [random.randint(15000, 25000) for _ in range(6)]
year_1_expenses += [random.randint(5000, 10000) for _ in range(6)]
year_2_sales = [random.randint(30000, 60000) for _ in range(12)]
year_2_expenses = [random.randint(10000, 20000) for _ in range(12)]

# Combine sales and expenses data for two years
sales_data = year_1_sales + year_2_sales
expenses_data = year_1_expenses + year_2_expenses

# Generate x-axis ticks
x_ticks = range(1, len(sales_data) + 1)

# Create the figure and axis objects
fig, ax = plt.subplots()

# Plot the sales and expenses data
ax.plot(x_ticks, sales_data, marker="o", linestyle="-", color="b", label="Prodeje")
ax.plot(x_ticks, expenses_data, marker="o", linestyle="-", color="r", label="Výdaje")

# Calculate and plot the trend line
z = np.polyfit(x_ticks, sales_data, 1)
p = np.poly1d(z)
ax.plot(x_ticks, p(x_ticks), linestyle="--", color="g", label="Lineární trend")

# Set x-axis ticks and labels
ax.set_xticks(x_ticks)
ax.set_xticklabels(months * 2, rotation=45)

# Set axis labels and title
ax.set_xlabel("Měsíc")
ax.set_ylabel("Částka")
ax.set_title("Růst prodejů a výdajů kavárny za dva roky")

# Display the legend
ax.legend()

# Display the plot
plt.show()
