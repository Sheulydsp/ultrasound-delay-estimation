# Ultrasound Delay Estimation using Cross-Correlation

## Overview
This project demonstrates delay estimation in multi-channel ultrasound signals using cross-correlation methods. The goal is to estimate relative time delays between signals under noisy conditions, which is essential for phase aberration correction and beamforming in ultrasound imaging systems.

This implementation is a simplified and structured version of my Master's thesis work, where I analyzed the robustness of delay estimation methods under noise.

---

## Motivation
In ultrasound imaging, signals received by different transducer elements arrive at slightly different times due to variations in propagation paths and tissue properties. Accurate estimation of these delays is critical for:

- Coherent signal alignment  
- Beamforming  
- Image quality improvement  

Noise and sampling limitations affect delay estimation accuracy. This project explores how delay estimation performs under such conditions.

---

## Methodology

The simulation follows a complete signal processing pipeline:

### Signal Generation
A reference signal is generated as a windowed sinusoidal pulse representing an ultrasound RF signal.

### Delay Modeling
Multiple delayed versions of the reference signal are created to simulate multi-channel acquisition.

### Noise Modeling
Additive White Gaussian Noise (AWGN) is applied to simulate measurement noise.

### Signal Conditioning
- Bandpass filtering using an elliptic filter  
- Windowing using a Tukey window to reduce edge effects  

### Delay Estimation
- Cross-correlation is used to estimate relative delays  
- Parabolic interpolation is applied for sub-sample accuracy  

### Performance Evaluation
Monte Carlo simulations are performed across multiple trials.  
Error is computed as the difference between estimated and true delays.  

Metrics used:
- Mean error (bias)  
- Standard deviation (variability)  

---

## Project Structure
.
├── main.py
├── requirements.txt
└── README.md

---

## How to Run

### Install dependencies

pip install -r requirements.txt


### Run simulation

python main.py


The script will output:
- Mean delay estimation error  
- Standard deviation of the error  

---

## Key Concepts Demonstrated

- Cross-correlation-based delay estimation  
- Sub-sample estimation using interpolation  
- Multi-channel signal simulation  
- Noise robustness analysis  
- Monte Carlo evaluation of system performance  

---

## Relation to Thesis Work

This project is based on my Master's thesis:

**Analysis of Noise Effects on Delay Estimation for Ultrasound Phase Aberration Correction**

The full thesis includes:
- Multi-channel simulation (up to 64 channels)  
- Advanced delay estimation methods (NNCC and beamsum)  
- Detailed analysis of noise impact on bias and variance  
- Extensive statistical evaluation  

This repository provides a simplified version focusing on the core concepts and implementation.

---

## Skills Demonstrated

- Signal processing for ultrasound systems  
- Algorithm development and validation  
- Statistical performance analysis  
- Simulation of real-world conditions  
- Clean and structured code design  

---

## Future Improvements
   
- Use real ultrasound datasets  
- Evaluate impact on reconstructed image quality  

---

## Author

Sheuly Debnath  
Master’s in Signal Processing and Imaging  
University of Oslo  
