import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
from sklearn.linear_model import LinearRegression
import numpy as np

# Step 1: Download the dataset
url = "https://datahub.io/core/global-temp/r/annual.csv"
response = requests.get(url)
if response.status_code == 200:
    data = StringIO(response.text)
    df = pd.read_csv(data)
else:
    print("Failed to download dataset.")
    exit()

# Step 2: Data Preprocessing
df.rename(columns={"Source": "Source", "Year": "Year", "Mean": "Temperature"}, inplace=True)
df.dropna(subset=["Temperature"], inplace=True)

# Step 3: Create visualizations
# Scatter plot with regression line
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

X = df["Year"].values.reshape(-1, 1)
y = df["Temperature"].values

# Regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

sns.scatterplot(x="Year", y="Temperature", data=df, label="Data Points")
plt.plot(df["Year"], y_pred, color="red", label="Regression Line")
plt.title("Global Temperature Change Over Time (Scatterplot with Regression Line)")
plt.xlabel("Year")
plt.ylabel("Mean Temperature Anomaly (°C)")
plt.legend()
plt.show()

# Line chart for temperature trends
plt.figure(figsize=(10, 6))
sns.lineplot(x="Year", y="Temperature", data=df, label="Temperature Trend")
plt.title("Global Temperature Change Over Time (Line Chart)")
plt.xlabel("Year")
plt.ylabel("Mean Temperature Anomaly (°C)")
plt.legend()
plt.show()

# Bar chart for average temperature change per decade
df["Decade"] = (df["Year"] // 10) * 10
decade_avg = df.groupby("Decade")["Temperature"].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x="Decade", y="Temperature", data=decade_avg, palette="coolwarm")
plt.title("Average Temperature Change Per Decade (Bar Chart)")
plt.xlabel("Decade")
plt.ylabel("Mean Temperature Anomaly (°C)")
plt.show()
