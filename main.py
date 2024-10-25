import numpy as np
import matplotlib.pyplot as plt  # Import plt here
from anomaly_detector import AnomalyDetector
from data_stream import generate_data_stream
from visualization import plot_stream, visualize_report
from utils import log_event, generate_report

# Initialize AnomalyDetector with a rolling window of 30 points and a Z-score threshold of 3
detector = AnomalyDetector(window_size=30, multiplier=2)

def main():
    anomalies = []
    all_data = generate_data_stream(duration=60, freq=2)  # Generate data stream

    log_event("INFO", "Data stream generation started.")
    # Process data points
    for data_point in all_data:
        if detector.is_anomaly(data_point):
            anomalies.append(data_point)
            log_event("ANOMALY", f"Anomaly detected: {data_point}")
        else:
            log_event("NORMAL", f"Data: {data_point} - Normal")

    log_event("INFO", "Data stream processing completed.")
    
    # Generate report
    total_points, num_anomalies, anomaly_percentage, mean_value, std_dev = generate_report(all_data, anomalies)
    
    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns

    # Plot the data stream results with anomalies
    plot_stream(all_data, anomalies, axs[0])

    # Visualize the report
    visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev, axs[1])

    # Show the combined plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
