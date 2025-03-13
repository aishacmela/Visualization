import pandas as pd
import matplotlib.pyplot as plt 

#load the dataset
df = pd.read_csv("data/data.csv")

#display the first rows
print(df.head())

#create line plot
plt.plot(df["Year"], df["Sales"], marker = "o", linestyle = "-", color="b", label="Sales")
plt.plot(df["Year"], df["Profit"], marker = "s", linestyle = "--", color="r", label="Profit")

#customize the plot 
plt.xlabel("Year")
plt.ylabel("Amount (R)")
plt.title("Sales & Profit Over Time")
plt.legend()
plt.grid()


#Show plot 
plt.show()