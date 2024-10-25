import matplotlib.pyplot as plt

def visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev):
    # Data to plot
    labels = ['Total Points Processed', 'Number of Anomalies Detected', 'Percentage of Anomalies', 'Mean', 'Standard Deviation']
    values = [total_points, num_anomalies, anomaly_percentage, mean_value, std_dev]

    # Create a bar chart
    fig, ax = plt.subplots()

    ax.bar(labels, values, color=['blue', 'red', 'orange', 'green', 'purple'])

    # Add labels and title
    ax.set_ylabel('Values')
    ax.set_title('Data Stream Report Visualization')
    ax.set_ylim(0, max(values) + 10)  # Set y-limit for better visibility

    # Display value on top of each bar
    for i, value in enumerate(values):
        ax.text(i, value + 0.5, str(value), ha='center')

    # Show the plot
    plt.xticks(rotation=10)  # Rotate x labels for better readability
    plt.tight_layout()
    plt.show()

# Sample data for testing
if __name__ == "__main__":
    total_points = 120
    num_anomalies = 3
    anomaly_percentage = 2.50
    mean_value = 50.94
    std_dev = 12.42

    visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev)
