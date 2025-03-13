import pandas as pd
import matplotlib.pyplot as plt 

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


#create bar chart
plt.bar(df["Year"], df["Sales"], color="blue", label= "Sales")
plt.bar(df["Year"], df["Profit"], color="red", label= "Profit", alpha=0.7)

plt.xlabel("Sales (R)")
plt.ylabel("Profit")
plt.title("Sales vs Profit")


#Show plot 
plt.show()