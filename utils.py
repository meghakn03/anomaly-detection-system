from datetime import datetime
from report_visualization import visualize_report

# Basic logger to write events to a log file
def log_event(event_type, message, batch=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {event_type}: {message}\n"

    if batch is not None:
        batch.append(log_entry)  # Accumulate logs in the batch
    else:
        with open("stream_log.txt", "a") as log_file:
            log_file.write(log_entry)

# Function to generate a final report
def generate_report(data, anomalies):
    total_points = len(data)
    num_anomalies = len(anomalies)
    anomaly_percentage = (num_anomalies / total_points) * 100 if total_points > 0 else 0
    mean_value = sum(data) / total_points if total_points > 0 else 0
    std_dev = (sum([(x - mean_value) ** 2 for x in data]) / total_points) ** 0.5 if total_points > 0 else 0
    
    report = f"""
    --- Data Stream Report ---
    Total Data Points Processed: {total_points}
    Number of Anomalies Detected: {num_anomalies}
    Percentage of Anomalies: {anomaly_percentage:.2f}%
    Mean of Data Stream: {mean_value:.2f}
    Standard Deviation of Data Stream: {std_dev:.2f}
    """
    
    print(report)
    # visualize_report(total_points, num_anomalies, anomaly_percentage, mean_value, std_dev)

    with open("stream_report.txt", "w") as report_file:
        report_file.write(report)
    
    # Return the values needed for plotting
    return total_points, num_anomalies, anomaly_percentage, mean_value, std_dev

def flush_logs(batch):
    with open("stream_log.txt", "a") as log_file:
        log_file.writelines(batch)  # Write all accumulated logs