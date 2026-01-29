# Generate a dataset of daily temperature and ice-cream sales.
# Find the covariance between temperature and sales.
# Plot the relationship using a scatter plot.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.random.seed(42)

temp = np.random.randint(20, 40, 10)
icecream = temp * 5 + np.random.randint(-10, 10, 10)

df = pd.DataFrame({
    "temperature":temp,
    "Icecream_sales":icecream
})

print("Covariance:", df.cov())

plt.scatter(temp,icecream)
plt.xlabel("Temperature")
plt.ylabel("Icecream Sales")
plt.title("Temperature and Icecream Sales")
plt.show()
