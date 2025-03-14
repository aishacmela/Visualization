import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

#load the dataset
df = pd.read_csv("data/data.csv")

#display the first rows
print(df.head())

#create line plot
plt.plot(df["Year"], df["Sales"], marker = "o", linestyle = "-", color="orange", label="Sales")
plt.plot(df["Year"], df["Profit"], marker = "s", linestyle = "--", color="green", label="Profit")

#customize the plot 
plt.xlabel("Year")
plt.ylabel("Amount (R)")
plt.title("Sales & Profit Over Time")
plt.legend()

#compute correlation matrix 
correlation = df.corr()

#create a heatmap
sns.heatmap(correlation, annot=True, cmap="coolwarm", linewidths=0.5)

#Show plot 
plt.title("Correlation Heatmap")
plt.show()

#create bar chart
#plt.bar(df["Year"], df["Sales"], color="blue", label= "Sales")
#plt.bar(df["Year"], df["Profit"], color="red", label= "Profit", alpha=0.7)
#
#plt.xlabel("Sales (R)")
#plt.ylabel("Profit")
#plt.title("Sales vs Profit")


#create scatter plot 
#plt.scatter(df["Sales"], df["Profit"], color="purple")
#plt.xlabel("Sales (R)")
#plt.ylabel("Profit")
#plt.title("Sales vs Profit")


