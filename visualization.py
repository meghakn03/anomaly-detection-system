import matplotlib.pyplot as plt

def plot_stream(data, anomalies, ax):
    try:
        anomaly_indices = [i for i, point in enumerate(data) if point in anomalies]
        ax.plot(data, label="Data Stream", color='blue')
        for idx in anomaly_indices:
            ax.plot(idx, data[idx], "ro", markersize=8, label="Anomaly")
        ax.set_title("Data Stream Visualization")
        ax.set_xlabel("Data Point Index")
        ax.set_ylabel("Value")
        ax.legend()
        ax.grid()

    except Exception as e:
        print(f"Error in plot_stream: {e}")

def visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev, ax):
    try:
        labels = ['Total Points Processed', 'Number of Anomalies Detected', 'Percentage of Anomalies', 'Mean', 'Standard Deviation']
        values = [total_points, num_anomalies, anomaly_percentage, mean_value, std_dev]
        ax.bar(labels, values, color=['blue', 'red', 'orange', 'green', 'purple'])
        ax.set_ylabel('Values')
        ax.set_title('Data Stream Report Visualization')
        ax.set_ylim(0, max(values) + 10)
        for i, value in enumerate(values):
            ax.text(i, value + 0.5, str(value), ha='center')
        ax.set_xticklabels(labels, rotation=15, ha='right', fontsize=10)
        ax.grid()

    except Exception as e:
        print(f"Error in visualize_report: {e}")

def plot_benchmark_results(results, ax):
    try:
        sizes, times = zip(*results)
        ax.plot(sizes, times, marker='o', linestyle='-', color='b')
        ax.set_title("Benchmarking Results")
        ax.set_xlabel("Data Size (Number of Points)")
        ax.set_ylabel("Time Taken (seconds)")
        ax.grid(True)
        ax.set_xticks(sizes)
        ax.set_xticklabels(sizes, rotation=45, ha='right', fontsize=10)

    except Exception as e:
        print(f"Error in plot_benchmark_results: {e}")
