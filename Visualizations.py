import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Scraping and Preparing the Dataset
url = "https://datahub.io/core/global-temp/r/annual.csv"
data = pd.read_csv(url)

# Data Preparation
data = data.dropna()
data['Decade'] = (data['Year'] // 10) * 10

# Scatter Plot with Regression Line
def scatter_plot_with_regression(data):
    years = data['Year']
    anomalies = data['Mean']
    
    # Linear regression
    m, b = np.polyfit(years, anomalies, 1)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(years, anomalies, color='blue', label='Temperature Anomalies')
    plt.plot(years, m * years + b, color='red', label=f'Regression Line (slope={m:.2e})')
    
    # Plot aesthetics
    plt.title("Global Temperature Anomalies Over Time (1880-2023)")
    plt.xlabel("Year")
    plt.ylabel("Temperature Anomaly (°C)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("scatter_plot_with_regression.png")  # Save the plot
    plt.show()

# Line Chart
def line_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['Mean'], color='green', marker='o', label='Mean Anomaly')
    
    # Plot aesthetics
    plt.title("Global Temperature Anomalies (1880-2023)")
    plt.xlabel("Year")
    plt.ylabel("Temperature Anomaly (°C)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("line_chart.png")  # Save the plot
    plt.show()

# Bar Chart
def bar_chart(data):
    # Group by decade and calculate mean anomaly
    decade_means = data.groupby('Decade')['Mean'].mean()
    
    plt.figure(figsize=(10, 6))
    plt.bar(decade_means.index, decade_means, color='purple', width=8, edgecolor='black')
    
    # Plot aesthetics
    plt.title("Average Temperature Anomalies by Decade (1880-2023)")
    plt.xlabel("Decade")
    plt.ylabel("Average Temperature Anomaly (°C)")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig("bar_chart.png")  # Save the plot
    plt.show()

# Main Code
if __name__ == "__main__":
    print("First 5 rows of the dataset:")
    print(data.head())
    
    scatter_plot_with_regression(data)
    line_chart(data)
    bar_chart(data)
