import matplotlib.pyplot as plt

def plot_stream(data, anomalies, ax):
    """Plot the data stream with anomalies on the given axes."""
    # Create a list of anomaly indices
    anomaly_indices = [i for i, point in enumerate(data) if point in anomalies]

    # Plot all data points first
    ax.plot(data, label="Data Stream", color='blue')

    # Highlight anomalies
    for idx in anomaly_indices:
        ax.plot(idx, data[idx], "ro", markersize=8, label="Anomaly")  # Mark anomalies with red dots

    ax.set_title("Data Stream Visualization")
    ax.set_xlabel("Data Point Index")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid()

def visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev, ax):
    """Visualize the report on the given axes."""
    # Data to plot
    labels = ['Total Points Processed', 'Number of Anomalies Detected', 'Percentage of Anomalies', 'Mean', 'Standard Deviation']
    values = [total_points, num_anomalies, anomaly_percentage, mean_value, std_dev]

    # Create a bar chart
    ax.bar(labels, values, color=['blue', 'red', 'orange', 'green', 'purple'])

    # Add labels and title
    ax.set_ylabel('Values')
    ax.set_title('Data Stream Report Visualization')
    ax.set_ylim(0, max(values) + 10)  # Set y-limit for better visibility

    # Display value on top of each bar
    for i, value in enumerate(values):
        ax.text(i, value + 0.5, str(value), ha='center')

    ax.grid()

    # Rotate x-axis labels for better readability
    ax.set_xticklabels(labels, rotation=15, ha='right', fontsize=10)  # Adjust rotation and font size

def plot_benchmark_results(results, ax):
    sizes, times = zip(*results)  # Unzip the results into sizes and times
    ax.plot(sizes, times, marker='o', linestyle='-', color='b')
    
    ax.set_title("Benchmarking Results")
    ax.set_xlabel("Data Size (Number of Points)")
    ax.set_ylabel("Time Taken (seconds)")
    ax.grid(True)

    # Set x-ticks to be the data sizes
    ax.set_xticks(sizes)  
    ax.set_xticklabels(sizes, rotation=45, ha='right', fontsize=10)  # Rotate labels for better readability

    # Optionally set a logarithmic scale if the size range is large
    # ax.set_xscale('log')  # Uncomment if you want a logarithmic scale for the x-axis
