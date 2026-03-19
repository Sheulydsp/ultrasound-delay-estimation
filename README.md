Ultrasound Delay Estimation using Cross-Correlation
Overview

This project demonstrates delay estimation in multi-channel ultrasound signals using cross-correlation methods. The objective is to estimate relative time delays between signals under noisy conditions, which is essential for phase aberration correction and beamforming in ultrasound imaging systems.

The implementation is a simplified and structured version of a larger Master’s thesis project focused on analyzing the robustness of delay estimation methods under noise.

Motivation

In ultrasound imaging, signals received by different transducer elements arrive at slightly different times due to variations in propagation paths and tissue properties. Accurate estimation of these delays is critical for:

Coherent signal alignment

Beamforming

Image quality improvement

Noise and sampling limitations affect delay estimation accuracy. This project explores how delay estimation performs under such conditions.

Methodology

The simulation follows a complete signal processing pipeline:

1. Signal Generation

A reference signal is created as a windowed sinusoidal pulse representing an ultrasound RF signal.

2. Delay Modeling

Multiple delayed versions of the reference signal are generated to simulate multi-channel acquisition.

3. Noise Modeling

Additive White Gaussian Noise is applied to simulate measurement noise.

4. Signal Conditioning

Bandpass filtering using an elliptic filter

Windowing using a Tukey window to reduce edge effects

5. Delay Estimation

Cross-correlation is used to estimate relative delays.
Parabolic interpolation is applied to achieve sub-sample accuracy.

6. Performance Evaluation

Monte Carlo simulations are performed across multiple trials.
Error is computed as the difference between estimated and true delays.
Statistical metrics include:

Mean error (bias)

Standard deviation (variability)

Project Structure
.
├── main.py
├── requirements.txt
└── README.md
How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run simulation
python main.py

The script will output:

Mean delay estimation error

Standard deviation of the error

Key Concepts Demonstrated

Cross-correlation-based delay estimation

Sub-sample estimation using interpolation

Multi-channel signal simulation

Noise robustness analysis

Monte Carlo evaluation of system performance

Relation to Thesis Work

This repository represents a simplified implementation of a Master’s thesis focused on:

Delay estimation methods (NNCC and beamsum correlation)

Multi-channel ultrasound signal modeling

Analysis of noise effects on estimation accuracy

Evaluation using statistical metrics such as bias, variance, and correlation

The full thesis includes more advanced simulations, realistic parameter settings, and extensive evaluation across multiple configurations.

Skills Demonstrated

Signal processing for ultrasound systems

Algorithm implementation and evaluation

Statistical analysis of system performance

Simulation of real-world conditions

Clean and structured code design

Future Improvements

Implement fractional delay modeling

Extend to beamsum-based delay estimation

Incorporate real ultrasound datasets

Evaluate impact on reconstructed image quality

Author

Sheuly Debnath
Master’s in Signal Processing and Imaging
University of Oslo
