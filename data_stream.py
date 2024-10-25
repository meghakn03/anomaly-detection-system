import numpy as np

def generate_data_stream(num_points=None, duration=60, freq=2):
    if num_points is not None:
        duration = num_points / freq  # Adjust duration based on the number of points and frequency

    time_points = np.arange(0, duration, 1/freq)

    # Preallocate the data_stream array
    data_stream = np.zeros(len(time_points))

    # Generate seasonal patterns and noise in one go
    seasonal_amplitudes = 10 + np.floor(time_points / 30)  # Concept drift every 30 points
    seasonal_patterns = seasonal_amplitudes * np.sin(time_points / 10)
    noise = np.random.normal(0, 5, len(time_points))

    data_stream = 50 + seasonal_patterns + noise

    # Generate anomaly indices
    anomaly_indices = np.arange(30, len(data_stream), 30)

    # Add anomalies
    data_stream[anomaly_indices] += 50  # Add a large spike every 30 points

    return data_stream
