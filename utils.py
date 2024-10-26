from datetime import datetime

def log_event(event_type, message, batch=None):
    # Get the current timestamp in a formatted string
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create a log entry with the timestamp, event type, and message
    log_entry = f"[{timestamp}] {event_type}: {message}\n"
    
    try:
        # If a batch is provided, append the log entry to the batch
        if batch is not None:
            batch.append(log_entry)
        else:
            # If no batch is provided, write the log entry directly to the log file
            with open("stream_log.txt", "a") as log_file:
                log_file.write(log_entry)
    except IOError as e:
        # Handle file write errors and print an error message
        print(f"File write error: {e}")

def generate_report(data, anomalies):
    try:
        # Calculate the total number of data points
        total_points = len(data)
        # Calculate the number of detected anomalies
        num_anomalies = len(anomalies)
        # Calculate the percentage of anomalies in the data
        anomaly_percentage = (num_anomalies / total_points) * 100 if total_points > 0 else 0
        # Calculate the mean of the data stream
        mean_value = sum(data) / total_points if total_points > 0 else 0
        # Calculate the standard deviation of the data stream
        std_dev = (sum([(x - mean_value) ** 2 for x in data]) / total_points) ** 0.5 if total_points > 0 else 0

        # Create a formatted report string with the calculated statistics
        report = f"""
        --- Data Stream Report ---
        Total Data Points Processed: {total_points}
        Number of Anomalies Detected: {num_anomalies}
        Percentage of Anomalies: {anomaly_percentage:.2f}%
        Mean of Data Stream: {mean_value:.2f}
        Standard Deviation of Data Stream: {std_dev:.2f}
        """

        # Print the report to the console
        print(report)
        # Write the report to a text file
        with open("stream_report.txt", "w") as report_file:
            report_file.write(report)

        return total_points, num_anomalies, anomaly_percentage, mean_value, std_dev

    except Exception as e:
        # Log any errors encountered during report generation
        log_event("ERROR", f"Error generating report: {e}")
        # Return default values in case of error
        return 0, 0, 0, 0, 0

def flush_logs(batch):
    try:
        # Write all log entries in the batch to the log file
        with open("stream_log.txt", "a") as log_file:
            log_file.writelines(batch)
    except IOError as e:
        # Handle any errors encountered while flushing logs
        print(f"Error flushing logs: {e}")
