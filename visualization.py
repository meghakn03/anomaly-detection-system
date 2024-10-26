import matplotlib.pyplot as plt

def plot_stream(data, anomalies, ax):
    try:
        # Identify the indices of the data points that are considered anomalies
        anomaly_indices = [i for i, point in enumerate(data) if point in anomalies]

        # Plot the data stream
        ax.plot(data, label="Data Stream", color='blue')

        # Highlight anomalies with red circles on the plot
        for idx in anomaly_indices:
            ax.plot(idx, data[idx], "ro", markersize=8, label="Anomaly")
        
        # Set plot title and labels
        ax.set_title("Data Stream Visualization")
        ax.set_xlabel("Data Point Index")
        ax.set_ylabel("Value")
        
        # Add a legend to the plot
        ax.legend()
        ax.grid()  # Add a grid for better readability

    except Exception as e:
        # Handle any errors that occur during plotting
        print(f"Error in plot_stream: {e}")

def visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev, ax):
    try:
        # Define labels and values for the bar chart
        labels = ['Total Points Processed', 'Number of Anomalies Detected', 'Percentage of Anomalies', 'Mean', 'Standard Deviation']
        values = [total_points, num_anomalies, anomaly_percentage, mean_value, std_dev]

        # Create a bar chart to visualize the report metrics
        ax.bar(labels, values, color=['blue', 'red', 'orange', 'green', 'purple'])
        
        # Set the y-axis label and title for the plot
        ax.set_ylabel('Values')
        ax.set_title('Data Stream Report Visualization')
        ax.set_ylim(0, max(values) + 10)  # Set y-axis limits

        # Annotate each bar with its value
        for i, value in enumerate(values):
            ax.text(i, value + 0.5, str(value), ha='center')
        
        # Rotate x-axis labels for better readability
        ax.set_xticklabels(labels, rotation=15, ha='right', fontsize=10)
        ax.grid()  # Add a grid for better readability

    except Exception as e:
        # Handle any errors that occur during visualization
        print(f"Error in visualize_report: {e}")

def plot_benchmark_results(results, ax):
    try:
        # Unpack the results into sizes and corresponding times
        sizes, times = zip(*results)

        # Plot the benchmark results with points and lines
        ax.plot(sizes, times, marker='o', linestyle='-', color='b')
        
        # Set title and labels for the plot
        ax.set_title("Benchmarking Results")
        ax.set_xlabel("Data Size (Number of Points)")
        ax.set_ylabel("Time Taken (seconds)")
        ax.grid(True)  # Add a grid for better readability
        
        # Set x-ticks and rotate for better readability
        ax.set_xticks(sizes)
        ax.set_xticklabels(sizes, rotation=45, ha='right', fontsize=10)

    except Exception as e:
        # Handle any errors that occur during plotting
        print(f"Error in plot_benchmark_results: {e}")
