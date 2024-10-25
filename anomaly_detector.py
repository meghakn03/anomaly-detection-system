import numpy as np

class AnomalyDetector:
    def __init__(self, window_size=30, multiplier=2):
        self.window_size = window_size
        self.multiplier = multiplier
        self.data_window = np.zeros(window_size)  # Pre-allocate window as a NumPy array
        self.index = 0  # Track the position in the window

    def is_anomaly(self, data_point):
        # Add the new data point to the window
        self.data_window[self.index % self.window_size] = data_point
        self.index += 1

        # If window is not full, no anomaly detection
        if self.index < self.window_size:
            return False

        # Calculate mean and standard deviation over the window
        mean = np.mean(self.data_window)
        std_dev = np.std(self.data_window)

        # Calculate Z-score and dynamic threshold
        dynamic_threshold = mean + self.multiplier * std_dev
        z_score = np.abs(data_point - mean) / std_dev if std_dev > 0 else 0

        # Debugging information
        # print(f"Data Point: {data_point}, Mean: {mean}, Std Dev: {std_dev}, Z-Score: {z_score}, Dynamic Threshold: {dynamic_threshold}")

        # Return whether the Z-score exceeds the multiplier
        return z_score > self.multiplier
