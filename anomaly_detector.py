import numpy as np

class AnomalyDetector:
    def __init__(self, window_size=30, multiplier=2):
        # Initialize the anomaly detector with a specified window size and multiplier
        self.window_size = window_size  # Number of points to consider for anomaly detection
        self.multiplier = multiplier      # Z-score multiplier for anomaly threshold
        self.data_window = np.zeros(window_size)  # Preallocate an array to store data points
        self.index = 0  # Current index in the data window

    def is_anomaly(self, data_point):
        try:
            # Update the data window with the new data point at the current index
            self.data_window[self.index % self.window_size] = data_point
            self.index += 1  # Increment the index for the next data point

            # If we haven't filled the data window yet, do not check for anomalies
            if self.index < self.window_size:
                return False

            # Calculate the mean and standard deviation of the current data window
            mean = np.mean(self.data_window)
            std_dev = np.std(self.data_window)

            # If standard deviation is zero, we can't calculate a z-score, so no anomaly
            if std_dev == 0:
                return False

            # Calculate the z-score for the current data point
            z_score = np.abs(data_point - mean) / std_dev
            
            # Return True if the z-score exceeds the threshold set by the multiplier, indicating an anomaly
            return z_score > self.multiplier

        except Exception as e:
            # Handle any errors that occur during anomaly detection
            print(f"Error in anomaly detection: {e}")
            return False
