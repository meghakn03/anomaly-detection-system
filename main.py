import numpy as np
from anomaly_detector import AnomalyDetector
from data_stream import generate_data_stream
from visualization import plot_stream

# Initialize AnomalyDetector with a rolling window of 30 points and an initial Z-score threshold of 3
detector = AnomalyDetector(window_size=30, multiplier=2)

def main():
    anomalies = []
    all_data = generate_data_stream(duration=60, freq=2)  # Generate the entire data stream at once

    # Process data points in bulk
    for data_point in all_data:
        if detector.is_anomaly(data_point):
            anomalies.append(data_point)
            print(f"Anomaly detected: {data_point}")
        else:
            print(f"Data: {data_point} - Normal")

    # Plot results after stream ends
    plot_stream(all_data, anomalies)

if __name__ == "__main__":
    main()
