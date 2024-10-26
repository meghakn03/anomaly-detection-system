import time
import numpy as np
import matplotlib.pyplot as plt
from anomaly_detector import AnomalyDetector
from data_stream import generate_data_stream
from visualization import plot_stream, visualize_report, plot_benchmark_results
from utils import log_event, generate_report, flush_logs

# Initialize AnomalyDetector with a rolling window of 30 points and a Z-score threshold of 2
detector = AnomalyDetector(window_size=30, multiplier=2)

def benchmark_anomaly_detection(data_sizes):
    results = []  # Store benchmarking results (data size and time taken)

    for size in data_sizes:
        try:
            # Generate a data stream of a specified size
            all_data = generate_data_stream(duration=60, freq=2, num_points=size)
            start_time = time.time()  # Record start time for benchmarking
            anomalies = []  # List to hold detected anomalies
            log_batch = []  # Batch for logging events
            log_event("INFO", f"Data stream generation started for size: {size}.", log_batch)

            # Process each data point in the generated stream
            for data_point in all_data:
                try:
                    # Check if the current data point is an anomaly
                    if detector.is_anomaly(data_point):
                        anomalies.append(data_point)  # Add to anomalies list if detected
                        log_event("ANOMALY", f"Anomaly detected: {data_point}", log_batch)
                except Exception as e:
                    # Log any errors encountered during anomaly detection
                    log_event("ERROR", f"Anomaly detection error for data point {data_point}: {e}", log_batch)

            flush_logs(log_batch)  # Write all logged events to the log file

            # Generate a report on the data stream and detected anomalies
            total_points, num_anomalies, anomaly_percentage, mean_value, std_dev = generate_report(all_data, anomalies)
            elapsed_time = time.time() - start_time  # Calculate time taken
            results.append((size, elapsed_time))  # Store results

        except Exception as e:
            # Handle and log errors that occur during benchmarking
            print(f"Error in benchmark_anomaly_detection for data size {size}: {e}")
            log_event("ERROR", f"Benchmarking error for data size {size}: {e}")

    # Output benchmarking results
    print("\n--- Benchmark Results ---")
    print("Data Size | Time Taken (seconds)")
    for size, elapsed_time in results:
        print(f"{size:10} | {elapsed_time:.4f}")

    return results  # Return the collected results

def main():
    anomalies = []  # List to hold detected anomalies
    try:
        # Generate the initial data stream for anomaly detection
        all_data = generate_data_stream(duration=60, freq=2)
        log_batch = []  # Batch for logging events
        log_event("INFO", "Data stream generation started.", log_batch)

        # Process each data point in the generated stream
        for data_point in all_data:
            try:
                # Check if the current data point is an anomaly
                if detector.is_anomaly(data_point):
                    anomalies.append(data_point)  # Add to anomalies list if detected
                    log_event("ANOMALY", f"Anomaly detected: {data_point}", log_batch)
            except Exception as e:
                # Log any errors encountered during anomaly detection
                log_event("ERROR", f"Error detecting anomaly in data point {data_point}: {e}", log_batch)

        flush_logs(log_batch)  # Write all logged events to the log file
        # Generate a report on the data stream and detected anomalies
        total_points, num_anomalies, anomaly_percentage, mean_value, std_dev = generate_report(all_data, anomalies)

        # Set up the visualization with three subplots
        fig, axs = plt.subplots(1, 3, figsize=(18, 6))
        # Visualize the data stream and detected anomalies
        plot_stream(all_data, anomalies, axs[0])
        # Visualize the report statistics
        visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev, axs[1])

        # Define different data sizes for benchmarking
        data_sizes = [100, 500, 1000, 5000, 10000]
        benchmark_results = benchmark_anomaly_detection(data_sizes)  # Perform benchmarking
        # Visualize the benchmarking results
        plot_benchmark_results(benchmark_results, axs[2])

        plt.tight_layout()  # Adjust subplot layout for better spacing
        plt.show()  # Display the visualizations

    except Exception as e:
        # Handle and log any unexpected errors
        log_event("ERROR", f"Unexpected error in main function: {e}")
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
