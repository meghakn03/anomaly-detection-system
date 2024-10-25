import numpy as np

def generate_data_stream(duration=60, freq=2):
    time_points = np.arange(0, duration, 1/freq)
    
    # Generate seasonal patterns and noise in one go
    seasonal_amplitudes = 10 + np.floor(time_points / 30)  # Concept drift every 30 points
    seasonal_patterns = seasonal_amplitudes * np.sin(time_points / 10)
    noise = np.random.normal(0, 5, len(time_points))
    
    data_stream = 50 + seasonal_patterns + noise
    
    # Add anomalies
    anomaly_indices = np.arange(30, len(data_stream), 30)
    data_stream[anomaly_indices] += 50  # Add a large spike every 30 points

    return data_stream
