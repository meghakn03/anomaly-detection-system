import matplotlib.pyplot as plt

def plot_stream(data, anomalies):
    plt.ion()  # Interactive mode on
    fig, ax = plt.subplots()

    # Create a list of anomaly indices
    anomaly_indices = [i for i, point in enumerate(data) if point in anomalies]

    # Plot all data points first
    ax.plot(data, label="Data Stream", color='blue')

    # Highlight anomalies
    for idx in anomaly_indices:
        ax.plot(idx, data[idx], "ro", markersize=8, label="Anomaly")  # Mark anomalies with red dots

    ax.legend()
    plt.pause(0.05)
    plt.ioff()  # Interactive mode off
    plt.show()
