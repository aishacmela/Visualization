import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Manually entering the data (from the image)
data = {
    "X": [0, 3, 6, 9, 12, 18, 24],
    "A:Y1": [10000, 35000, 340000, 3500000, 3e+007, 1.87e+008, 1.9e+008],
    "A:Y2": [16000, 43000, 370000, 4100000, 3e+007, 2.75e+008, 2.8e+008 ],
    "A:Y3": [5000, 87000, 400000, 3700000, 3e+007, 3.08e+008, 1.9e+008],
    "B:Y1": [32000, 79000, 370000, 6500000, 3.3e+007, 3.3e+008, 8e+008],
    "B:Y2": [16000, 71000, 410000, 4300000, 3.2e+007, 6.16e+008, 7.4e+008],
    "B:Y3": [48000, 45000, 310000, 2.8e+007, 3.2e+007, 5.61e+008, 2.2e+008],
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute mean & standard deviation for sc (A) and hg (B)
df["A_Mean"] = df[["A:Y1", "A:Y2", "A:Y3"]].mean(axis=1)
df["A_Std"] = df[["A:Y1", "A:Y2", "A:Y3"]].std(axis=1)

df["B_Mean"] = df[["B:Y1", "B:Y2", "B:Y3"]].mean(axis=1)
df["B_Std"] = df[["B:Y1", "B:Y2", "B:Y3"]].std(axis=1)

# Plot mean with error bars
plt.figure(figsize=(8, 5))
plt.errorbar(df["X"], df["A_Mean"], yerr=df["A_Std"], fmt='o-', label="sc (A)", capsize=6, color='b')
plt.errorbar(df["X"], df["B_Mean"], yerr=df["B_Std"], fmt='o-', label="hg (B)", capsize=3, color='r')

# Customize the plot
plt.xlabel("Time (Hours)")  
plt.ylabel("CFU/ml")
plt.title("Growth curve of sc & hg")
plt.legend()

# Show the plot
plt.show()
