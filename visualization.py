import matplotlib.pyplot as plt

# Real-time plotting for anomalies
def plot_stream(data, anomalies):
    plt.ion()
    fig, ax = plt.subplots()

    anomaly_indices = [i for i, point in enumerate(data) if point in anomalies]
    for i in range(len(data)):
        ax.clear()
        ax.plot(data[:i+1], label="Data Stream")

        # Highlight anomalies
        if i in anomaly_indices:
            ax.plot(i, data[i], "ro", label="Anomaly")

        ax.legend()
        plt.pause(0.05)

    plt.ioff()
    plt.show()
