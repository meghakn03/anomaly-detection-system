import numpy as np

def generate_data_stream(num_points=None, duration=60, freq=2):
    # If num_points is provided, adjust the duration based on the desired number of points and frequency
    if num_points is not None:
        duration = num_points / freq  # Calculate duration to fit the number of points at the given frequency

    # Create an array of time points from 0 to duration with intervals defined by the frequency
    time_points = np.arange(0, duration, 1/freq)

    # Preallocate the data_stream array to improve performance
    data_stream = np.zeros(len(time_points))

    # Generate seasonal patterns and noise in one go
    seasonal_amplitudes = 10 + np.floor(time_points / 30)  # Concept drift every 30 points, increasing amplitude
    seasonal_patterns = seasonal_amplitudes * np.sin(time_points / 10)  # Create sinusoidal seasonal patterns
    noise = np.random.normal(0, 5, len(time_points))  # Generate random noise with mean 0 and standard deviation 5

    # Combine base value (50) with seasonal patterns and noise to form the data stream
    data_stream = 50 + seasonal_patterns + noise

    # Generate indices where anomalies will occur (every 30th point)
    anomaly_indices = np.arange(30, len(data_stream), 30)

    # Introduce anomalies by adding a significant spike at the generated indices
    data_stream[anomaly_indices] += 50  # Add a large spike to indicate an anomaly

    return data_stream  # Return the generated data stream with anomalies
