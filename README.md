Efficient Data Stream Anomaly Detection

A project that detects anomalies in continuous data streams using a real-time Z-score-based detection algorithm. The project is designed to handle concept drift and seasonal variations, making it adaptable for real-world applications like financial transaction monitoring and system health tracking.

Table of Contents

Introduction

Features

Project Structure

Setup

Usage

Benchmarking

Future Improvements

Introduction

This project detects anomalies in a simulated continuous data stream using statistical methods. It employs a Z-score anomaly detection algorithm, capable of adapting to seasonal patterns and concept drift, which is useful in identifying unusual behaviors in large data sets.

Features

Real-Time Anomaly Detection: Detects outliers using a Z-score-based method on a rolling window of data.

Data Stream Simulation: Generates synthetic data with seasonal patterns, noise, and injected anomalies.

Robust Error Handling: Includes validations and handling for various data irregularities.

Visualization: Real-time plots of the data stream with highlighted anomalies, and a benchmarking chart to show performance at different data sizes.

Benchmarking: Performance analysis to assess scalability with varying data sizes.

Project Structure

├── main.py               # Main script to run anomaly detection and benchmarking

├── anomaly_detector.py   # Anomaly detection class with Z-score-based method

├── data_stream.py        # Data stream generator with seasonal patterns and noise

├── utils.py              # Utility functions for logging and report generation

├── visualization.py      # Visualization functions for data and benchmarking

├── requirements.txt      # Dependencies for the project (numpy, matplotlib)

└── README.md             # Project overview and instructions

Setup
Clone the Repository:

git clone https://github.com/meghakn03/anomaly-detection-system.git

cd anomaly-detection-system

Install Dependencies: Use the requirements.txt file to install necessary packages.


pip install -r requirements.txt
Usage
Run the main.py script to initiate anomaly detection on a simulated data stream. This will generate real-time visualizations, a report summary, and benchmark results.


python main.py

Key Parameters

window_size: Number of data points considered in the rolling window.

multiplier: Threshold multiplier for Z-score to flag anomalies.

data_sizes: A list of data stream sizes used for performance benchmarking.

Output

Visualizations:

Data stream plot with marked anomalies.

Benchmark results graph.

Logs and Report:

Log file (stream_log.txt) and report file (stream_report.txt) with summaries of detected anomalies and data statistics.

Benchmarking

The benchmarking feature in main.py evaluates the algorithm's scalability by testing it on data streams of increasing sizes. Benchmarking results are displayed in a line chart, showing how execution time scales with data size.

Future Improvements

Alternative Algorithms: Consider exploring Isolation Forest or Autoencoders for anomaly detection.

Optimization: Integrate parallel processing to enhance scalability for larger datasets.

User-Defined Thresholds: Enable user customization of detection parameters for added flexibility.
This project demonstrates the application of statistical methods for real-time anomaly detection in data streams, and it’s adaptable for various industry needs, including finance and IT monitoring. Contributions and suggestions are welcome!
