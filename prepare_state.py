# -*- coding: utf-8 -*-
"""
@author: Q-core team

This script prepares a quantum state vector for a 2-qubit or 3-qubit system.
You can enter amplitudes manually or use a test state.
It includes unit tests to check normalization and output size.
Uses only NumPy.
"""

import numpy as np

def prepare_state(amplitudes):
    """
    Converts input list to a NumPy array and normalizes it
    so the norm is 1. Returns the normalized state vector.
    """
    amplitudes = np.array(amplitudes, dtype=np.complex128)
    amplitudes = amplitudes / np.linalg.norm(amplitudes)
    return amplitudes

def get_user_input(n):
    """
    Prompts the user to enter amplitudes for a quantum state.
    Accepts 'real' or 'complex' numbers separated by spaces.
    Verifies length matches required number (4 or 8).
    """
    print(f"Enter {2 ** n} amplitudes (real or complex, e.g. 1 or 1j), separated by spaces:")
    entries = input("> ").split()
    amplitudes = [complex(entry) for entry in entries]
    if len(amplitudes) != 2 ** n:
        print(f"You must enter exactly {2 ** n} numbers.")
        exit(1)
    return amplitudes

def test_set(n):
    """
    Returns the default test state: first amplitude = 1, rest = 0.
    """
    amplitudes = [0] * (2 ** n)
    amplitudes[0] = 1
    return amplitudes

def test_two_qubit_state():
    in_state = [1, 0, 0, 0]
    s = prepare_state(in_state)
    assert np.isclose(np.linalg.norm(s), 1.0), "Two-qubit: not normalized!"
    assert s.shape == (4,), "Two-qubit: wrong shape!"

def test_three_qubit_state():
    in_state = [1, 0, 0, 0, 0, 0, 0, 0]
    s = prepare_state(in_state)
    assert np.isclose(np.linalg.norm(s), 1.0), "Three-qubit: not normalized!"
    assert s.shape == (8,), "Three-qubit: wrong shape!"

def main():
    # Prompt for number of qubits: 2 or 3 only
    n = int(input("How many qubits? Enter 2 or 3 only:\n> "))
    if n not in [2, 3]:
        print("This script only supports 2 or 3 qubits!")
        exit(1)
    # Ask for input mode
    method = input("Type 'manual' / 'm' to enter amplitudes or 'test' / 't' for test state: ").lower().strip()
    if method == 'manual' or method == 'm':
        amplitudes = get_user_input(n)
    elif method == 'test' or method == 't':
        amplitudes = test_set(n)
        print("Using test state:", amplitudes)
    else:
        print("Invalid input. Please enter 'manual'/'m' or 'test'/'t'.")
        exit(1)
    # Prepare and output normalized state
    state = prepare_state(amplitudes)
    print("Normalized state:", state)

if __name__ == "__main__":
    main()
    # Run required tests after interactive part
    test_two_qubit_state()
    test_three_qubit_state()
    print("All unit tests passed!")
