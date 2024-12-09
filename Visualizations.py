import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Scraping and Preparing the Dataset
url = "https://datahub.io/core/global-temp/r/annual.csv"
data = pd.read_csv(url)

# Drop missing values if any
data = data.dropna()

# Add a 'Decade' column for analysis
data['Decade'] = (data['Year'] // 10) * 10

# Function 1: Scatter Plot with Regression Line
def scatter_plot_with_regression(data):
    plt.figure(figsize=(10, 6))
    sns.regplot(x=data['Year'], y=data['Mean'], scatter_kws={'s': 10}, line_kws={"color": "red"})
    plt.title('Global Temperature Anomalies Over Time', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Mean Temperature Anomaly (°C)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('scatter_plot_regression.png')  # Save the plot
    plt.show()

# Function 2: Line Chart
def line_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Year'], data['Mean'], marker='o', linestyle='-', color='blue')
    plt.title('Yearly Global Temperature Anomalies', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Mean Temperature Anomaly (°C)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('line_chart.png')  # Save the plot
    plt.show()

# Function 3: Bar Chart
def bar_chart(data):
    decadal_avg = data.groupby('Decade')['Mean'].mean()
    plt.figure(figsize=(10, 6))
    decadal_avg.plot(kind='bar', color='orange')
    plt.title('Average Temperature Anomaly Per Decade', fontsize=14)
    plt.xlabel('Decade', fontsize=12)
    plt.ylabel('Average Temperature Anomaly (°C)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('bar_chart.png')  # Save the plot
    plt.show()

# Main Execution
if __name__ == "__main__":
    print("First 5 rows of the dataset:")
    print(data.head())  # Display the first 5 rows of the dataset

    # Create visualizations
    scatter_plot_with_regression(data)
    line_chart(data)
    bar_chart(data)
