import numpy as np

class AnomalyDetector:
    def __init__(self, window_size=30, multiplier=2):
        self.window_size = window_size
        self.multiplier = multiplier
        self.data_window = np.zeros(window_size)
        self.index = 0

    def is_anomaly(self, data_point):
        try:
            self.data_window[self.index % self.window_size] = data_point
            self.index += 1

            if self.index < self.window_size:
                return False

            mean = np.mean(self.data_window)
            std_dev = np.std(self.data_window)

            if std_dev == 0:
                return False

            z_score = np.abs(data_point - mean) / std_dev
            return z_score > self.multiplier

        except Exception as e:
            print(f"Error in anomaly detection: {e}")
            return False
