# Quantum State Preparation: Two- and Three-Qubit Systems (QC Screening Task)

## Overview

This repository contains a Python script for preparing and normalizing quantum state vectors for 2-qubit and 3-qubit systems, using only NumPy.  
It is designed specifically for the QC Mentorship Program screening tasks and rigorously follows the program’s requirements.


## Features

- Supports **2-qubit (4 amplitudes)** and **3-qubit (8 amplitudes)** states.
- Allows entry of amplitudes manually (real or complex) or selection of a default test state.
- Normalizes any input state automatically.
- Clear and simple code with plain-English comments.
- **Includes unit tests** ensuring output is always normalized and correct in dimension.


## Getting Started

### Prerequisites

- Python 3.x
- [NumPy](https://numpy.org/)  
  Install with:
pip install numpy


### Running the Script

1. Save the script as `prepare_state.py`.
2. Run in terminal or command prompt:
python prepare_state.py


### Example Interactive Usage

How many qubits? Enter 2 or 3 only: 2

Type 'manual' / 'm' to enter amplitudes or 'test' / 't' for test state:
manual

Enter 4 amplitudes (real or complex, e.g. 1 or 1j), separated by spaces:

1 1j 0 0.5

Normalized state: [0.66666667+0.j 0. +0.66666667j 0. +0.j
0.33333333+0.j ]
All unit tests passed!



## File Structure

- `prepare_state.py` — Main script (copy from this repo!)


## Task Requirements (Checklist)

- [x] Accept input as a list or array of amplitudes (4 or 8, as required).
- [x] Ensure the state is normalized (\(|a_0|^2 + ... = 1\)).
- [x] Output as a NumPy array, shape (4,) for 2 qubits, (8,) for 3 qubits.
- [x] No quantum-specific state preparation functions, only NumPy.
- [x] Contains unit tests for normalization and vector size.


## License

MIT License


## Contact

Questions or suggestions?  
Open an issue or start a pull request!
