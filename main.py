import time
from anomaly_detector import AnomalyDetector
from data_stream import generate_data_stream
from visualization import plot_stream

# Initialize AnomalyDetector with a rolling window of 30 points and a Z-score threshold of 3
detector = AnomalyDetector(window_size=30, threshold=3)

# Process the data stream
def main():
    anomalies = []
    all_data = []  # New list to capture all data points

    # Process data points
    for data_point in generate_data_stream(duration=60, freq=2):  # Simulate a 60-second stream at 2 Hz
        all_data.append(data_point)
        if detector.is_anomaly(data_point):
            anomalies.append(data_point)
            print(f"Anomaly detected: {data_point}")
        else:
            print(f"Data: {data_point} - Normal")
    
    # Write all data and anomalies to files for comparison
    with open("all_data.txt", "w") as f:
        f.write("\n".join(map(str, all_data)))

    with open("anomalies.txt", "w") as f:
        f.write("\n".join(map(str, anomalies)))

    # Plot results after stream ends
    plot_stream(anomalies, all_data)  # Pass both anomalies and all_data

if __name__ == "__main__":
    main()
