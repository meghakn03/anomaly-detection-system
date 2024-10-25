import time  # Import time for benchmarking
import numpy as np
import matplotlib.pyplot as plt  # Import plt here
from anomaly_detector import AnomalyDetector
from data_stream import generate_data_stream
from visualization import plot_stream, visualize_report, plot_benchmark_results
from utils import log_event, generate_report, flush_logs

# Initialize AnomalyDetector with a rolling window of 30 points and a Z-score threshold of 3
detector = AnomalyDetector(window_size=30, multiplier=2)

def benchmark_anomaly_detection(data_sizes):
    results = []

    for size in data_sizes:
        all_data = generate_data_stream(duration=60, freq=2, num_points=size)  # Generate data stream with varying size
        
        start_time = time.time()  # Start timing
        anomalies = []
        log_batch = []  # Create a log batch for accumulation

        log_event("INFO", f"Data stream generation started for size: {size}.", log_batch)

        # Process data points
        for data_point in all_data:
            if detector.is_anomaly(data_point):
                anomalies.append(data_point)
                log_event("ANOMALY", f"Anomaly detected: {data_point}", log_batch)
        
        # Flush the accumulated log entries to the file after processing
        flush_logs(log_batch)

        log_event("INFO", "Data stream processing completed.", log_batch)

        total_points, num_anomalies, anomaly_percentage, mean_value, std_dev = generate_report(all_data, anomalies)

        elapsed_time = time.time() - start_time  # Calculate elapsed time
        results.append((size, elapsed_time))  # Store size and time

    # Print benchmark results
    print("\n--- Benchmark Results ---")
    print("Data Size | Time Taken (seconds)")
    for size, elapsed_time in results:
        print(f"{size:10} | {elapsed_time:.4f}")

    return results  # Return results for plotting



def main():
    anomalies = []
    all_data = generate_data_stream(duration=60, freq=2)  # Generate data stream

    log_batch = []  # Create a log batch for accumulation
    log_event("INFO", "Data stream generation started.", log_batch)

    # Process data points
    for data_point in all_data:
        if detector.is_anomaly(data_point):
            anomalies.append(data_point)
            log_event("ANOMALY", f"Anomaly detected: {data_point}", log_batch)
        else:
            # Optional: log only significant normal events
            pass  # Omit logging for normal data points unless required

    # Flush logs to file after processing
    flush_logs(log_batch)

    log_event("INFO", "Data stream processing completed.", log_batch)
    
    # Generate report
    total_points, num_anomalies, anomaly_percentage, mean_value, std_dev = generate_report(all_data, anomalies)
    
    # Create a figure with three subplots
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # 1 row, 3 columns

    # Plot the data stream results with anomalies
    plot_stream(all_data, anomalies, axs[0])

    # Visualize the report
    visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev, axs[1])

    # Benchmarking visualization
    data_sizes = [100, 500, 1000, 5000, 10000]  # Define different sizes for testing
    benchmark_results = benchmark_anomaly_detection(data_sizes)  # Get benchmark results
    plot_benchmark_results(benchmark_results, axs[2])  # Visualize the results

    # Show the combined plot
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

