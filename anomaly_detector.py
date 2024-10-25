from collections import deque
import numpy as np

class AnomalyDetector:
    def __init__(self, window_size=30, threshold=2.5):
        self.data_window = deque(maxlen=window_size)
        self.threshold = threshold  # Fixed threshold for testing purposes
        self.mean = None
        self.std_dev = None

    def is_anomaly(self, data_point):
        if len(self.data_window) < self.data_window.maxlen:
            self.data_window.append(data_point)
            return False  # No anomaly check until window is full

        # Update the window with the new data point
        self.data_window.append(data_point)

        # Calculate mean and standard deviation
        self.mean = np.mean(self.data_window)
        self.std_dev = np.std(self.data_window)

        # Calculate Z-score
        z_score = abs(data_point - self.mean) / self.std_dev if self.std_dev > 0 else 0

        # Debugging information
        print(f"Data Point: {data_point}, Mean: {self.mean}, Std Dev: {self.std_dev}, Z-Score: {z_score}, Threshold: {self.threshold}")

        return z_score > self.threshold
