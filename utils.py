from datetime import datetime

def log_event(event_type, message, batch=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {event_type}: {message}\n"
    try:
        if batch is not None:
            batch.append(log_entry)
        else:
            with open("stream_log.txt", "a") as log_file:
                log_file.write(log_entry)
    except IOError as e:
        print(f"File write error: {e}")

def generate_report(data, anomalies):
    try:
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
        with open("stream_report.txt", "w") as report_file:
            report_file.write(report)

        return total_points, num_anomalies, anomaly_percentage, mean_value, std_dev

    except Exception as e:
        log_event("ERROR", f"Error generating report: {e}")
        return 0, 0, 0, 0, 0

def flush_logs(batch):
    try:
        with open("stream_log.txt", "a") as log_file:
            log_file.writelines(batch)
    except IOError as e:
        print(f"Error flushing logs: {e}")
