import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

studies={
    "hours" : [11,12,13,14,15,16,17,18,19,20],
    "marks" : [80,81,82,83,84,85,86,87,88,89]
}

df  = pd.DataFrame(studies)

correlation = df.corr()
print("the correlation:")
print(correlation)

sns.regplot(x="hours", y="marks", data=df, marker = "v")
plt.title("Regression Plot: Hours vs Marks")
plt.show()

