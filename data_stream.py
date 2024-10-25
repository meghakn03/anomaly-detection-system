import numpy as np
import time

def generate_data_stream(duration=60, freq=2):
    time_step = 1 / freq
    for i in range(int(duration * freq)):
        # Vary the amplitude of the seasonal pattern to simulate concept drift
        seasonal_amplitude = 10 + (i // 30)  # Increase amplitude every 30 points
        seasonal_pattern = seasonal_amplitude * np.sin(i / 10)
        noise = np.random.normal(0, 5)
        data_point = 50 + seasonal_pattern + noise

        # Introduce a known anomaly every 30 data points
        if i % 30 == 0 and i != 0:
            data_point += 50  # More significant spike anomaly

        yield data_point
        time.sleep(time_step)
