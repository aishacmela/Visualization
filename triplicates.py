import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Manually entering the data (from the table)
data = {
    "X": [0, 3, 6, 9, 12, 18, 24],
    "A:Y1": [0.447, 0.697, 0.955, 1.102, 1.415, 1.914, 1.924],
    "A:Y2": [0.506, 0.448, 0.966, 1.029, 1.572, 1.903, 1.935],
    "A:Y3": [0.478, 0.452, 0.970, 1.343, 1.674, 1.866, 1.909],
    "B:Y1": [0.303, 0.524, 0.550, 1.002, 1.474, 1.931, 1.916],
    "B:Y2": [0.327, 0.541, 0.560, 0.994, 1.332, 1.962, 1.897],
    "B:Y3": [0.492, 0.540, 0.610, 0.920, 1.333, 1.912, 1.914],
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute mean & standard deviation for sc (A) and hg (B)
df["A_Mean"] = df[["A:Y1", "A:Y2", "A:Y3"]].mean(axis=1)
df["A_Std"] = df[["A:Y1", "A:Y2", "A:Y3"]].std(axis=1)

df["B_Mean"] = df[["B:Y1", "B:Y2", "B:Y3"]].mean(axis=1)
df["B_Std"] = df[["B:Y1", "B:Y2", "B:Y3"]].std(axis=1)

# Plot with error bars
plt.figure(figsize=(8, 5))
plt.errorbar(df["X"], df["A_Mean"], yerr=df["A_Std"], fmt='o-', label="sc (A)", capsize=4, color='b')
plt.errorbar(df["X"], df["B_Mean"], yerr=df["B_Std"], fmt='o-', label="hg (B)", capsize=3, color='r')

# Customize the plot
plt.xlabel("Time (Hours)")  
plt.ylabel("OD600")
plt.title("Growth curve of sc & hg")
plt.legend()


# Show the plot
plt.show()
