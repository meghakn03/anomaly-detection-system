import numpy as np
import time

#include a known anomaly at specific intervals, rather than having a random chance of anomalies. This ensures you can verify if expected anomalies appear on the graph.

def generate_data_stream(duration=60, freq=2):
    time_step = 1 / freq
    for i in range(int(duration * freq)):
        seasonal_pattern = 10 * np.sin(i / 10)
        noise = np.random.normal(0, 5)
        data_point = 50 + seasonal_pattern + noise

        # Introduce a known anomaly every 30 data points
        if i % 30 == 0 and i != 0:
            data_point += 50  # More significant spike anomaly

        yield data_point
        time.sleep(time_step)

