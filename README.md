# Quantum State Preparation: Two-Qubit Amplitudes (QC Screening Task)

## Overview

This repository contains a simple Python implementation for preparing a two-qubit quantum state from user-supplied complex amplitudes.  
This project was created as part of the QC Mentorship Program screening tasks.

- **No advanced quantum libraries required** (uses only NumPy)
- **Perfect for beginners**: easy code, step-by-step explanations

## Features

- Accepts an array of **4 complex amplitudes** (for a two-qubit quantum state)
- **Automatically normalizes** the state if needed
- Returns the normalized state as a NumPy array
- Includes basic **unit tests** for correctness

## Getting Started

### Prerequisites

- Python 3.x
- [NumPy](https://numpy.org/)  
  Install via pip:
pip install numpy

### Usage

1. Clone or download this repository.
2. Open the main Python file, for example `quantum_state.py`.
3. Run with your amplitudes as follows:

import numpy as np
from quantum_state import prepare_two_qubit_state

Example usage
ampls = [1, 1j, 0, 0.5]
state = prepare_two_qubit_state(ampls)
print("Prepared state:", state)

## Unit Tests

Simple tests are included. They verify that:
- The state is always normalized
- The output vector has length 4

To run the tests, simply execute the script:

python quantum_state.py

You should see output similar to:

Prepared state: [0.89442719+0.j 0.+0.89442719j 0.+0.j 0.4472136+0.j]
All tests passed.


## Task Requirements

- Normalize input amplitudes so their squared magnitudes sum to 1
- Output the normalized quantum state vector as a NumPy array of size 4
- **No use of high-level quantum state preparation functions** (e.g., Qiskit)
- Clear code, beginner-friendly, reliable

## Stretch Goal

You can easily extend the code to prepare a three-qubit state (8 amplitudes).  
Contributions and improvements are welcome!

## License

MIT License

## Contact

Questions or suggestions?  
Open an issue or start a pull request!
