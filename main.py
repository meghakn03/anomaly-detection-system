import time
import numpy as np
import matplotlib.pyplot as plt
from anomaly_detector import AnomalyDetector
from data_stream import generate_data_stream
from visualization import plot_stream, visualize_report, plot_benchmark_results
from utils import log_event, generate_report, flush_logs

# Initialize AnomalyDetector with a rolling window of 30 points and a Z-score threshold of 3
detector = AnomalyDetector(window_size=30, multiplier=2)

def benchmark_anomaly_detection(data_sizes):
    results = []

    for size in data_sizes:
        try:
            all_data = generate_data_stream(duration=60, freq=2, num_points=size)
            start_time = time.time()
            anomalies = []
            log_batch = []
            log_event("INFO", f"Data stream generation started for size: {size}.", log_batch)

            for data_point in all_data:
                try:
                    if detector.is_anomaly(data_point):
                        anomalies.append(data_point)
                        log_event("ANOMALY", f"Anomaly detected: {data_point}", log_batch)
                except Exception as e:
                    log_event("ERROR", f"Anomaly detection error for data point {data_point}: {e}", log_batch)

            flush_logs(log_batch)

            total_points, num_anomalies, anomaly_percentage, mean_value, std_dev = generate_report(all_data, anomalies)
            elapsed_time = time.time() - start_time
            results.append((size, elapsed_time))

        except Exception as e:
            print(f"Error in benchmark_anomaly_detection for data size {size}: {e}")
            log_event("ERROR", f"Benchmarking error for data size {size}: {e}")

    print("\n--- Benchmark Results ---")
    print("Data Size | Time Taken (seconds)")
    for size, elapsed_time in results:
        print(f"{size:10} | {elapsed_time:.4f}")

    return results

def main():
    anomalies = []
    try:
        all_data = generate_data_stream(duration=60, freq=2)
        log_batch = []
        log_event("INFO", "Data stream generation started.", log_batch)

        for data_point in all_data:
            try:
                if detector.is_anomaly(data_point):
                    anomalies.append(data_point)
                    log_event("ANOMALY", f"Anomaly detected: {data_point}", log_batch)
            except Exception as e:
                log_event("ERROR", f"Error detecting anomaly in data point {data_point}: {e}", log_batch)

        flush_logs(log_batch)
        total_points, num_anomalies, anomaly_percentage, mean_value, std_dev = generate_report(all_data, anomalies)

        fig, axs = plt.subplots(1, 3, figsize=(18, 6))
        plot_stream(all_data, anomalies, axs[0])
        visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev, axs[1])

        data_sizes = [100, 500, 1000, 5000, 10000]
        benchmark_results = benchmark_anomaly_detection(data_sizes)
        plot_benchmark_results(benchmark_results, axs[2])

        plt.tight_layout()
        plt.show()

    except Exception as e:
        log_event("ERROR", f"Unexpected error in main function: {e}")
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
