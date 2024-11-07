# quMeas

**quMeas** is a high-performance multi-threaded library for computing expectation values of Pauli strings using randomized measurement techniques and cumulant expansion of Pauli operators (strings). It combines **classical shadow tomography** with **statistical cumulant expansion** to efficiently estimate Pauli expectation values. Designed with a multi-layered parallelization strategy and optimized C++ backend, quMeas scales efficiently on multi-core systems, making it ideal to incorporate in large-scale quantum algorithms such as **VQE** for molecular simulation, **QAOA** for combinatorial optimization, or any other quantum algorithm with requires *expectation value of Pauli operators*.

## Features
- **Randomized Measurements**: Implements an efficient classical shadow tomography quantum measurement to estimate expectation values with randomized measurement bases.
- **Cumulant Expansion**: Computes expectation values of Pauli operators from a truncated cumulant average expansion utilizing a non-crossing partitioning of the Pauli operators.
- **High-Performance Architecture**: Built with C++ for performance-critical tasks and exposed to Python via Pybind11, with a robust, multi-threaded layered parallelization strategy.

## Installation

### Prerequisites

quMeas requires Python 3.7 or higher, a C++ compiler, and CMake, along with the following dependencies:
Ensure you have the following dependencies installed:
- **Python packages**:
	- `numpy`
	- `scipy`
- **Build tools**:
	- **C++ compiler**: A modern C++ compiler that supports C++17 or later (e.g., GCC 7+, Clang 5+)
	- **CMake**: Version 3.12 or higher

quMeas depends on `Eigen` (for numerical linear algebra) and `pybind11`  (for C++/Python bindings). If these libraries are not installed on your system, quMeas includes them in the `/external` directory and will use them automatically.

Additionally, to use functionalities from Qiskit for obtaining Pauli operators of Hamiltonian, state preparation, and to get measurement bits, make sure `qiskit`, `qiskit-nature`, and `qiskit-aqua` are installed.

### Cloning the Repository

Clone the repository with submodules (use `--recursive` if `Eigen` and `pybind11` are not installed)

```bash
git clone --recursive https://github.com/oimeitei/qumeas.git
```

### Installation with pip

In the root directory, run
```bash
pip install .
```

### Building with CMake

Alternatively, build and install quMeas using CMake:

1. Create a build directory:
	```bash
	mkdir build && cd build
	```
2. Configure with CMake:
	```bash
	cmake ..
	```
3. Compile:
	```bash
	make -j$(nproc)
	```
4. Make Python find qumeas:
	```bash
	export PYTHONPATH=/path/to/qumeas/python:$PYTHONPATH
	```
## Basic Usage

```bash
	from qumeas.qiskit_utils import Mole
	from qumeas import RandomShadow, QCumulant
	
	# Set up the molecule (H2O)
	h2o_mol = Mole(atom='h2o')
	
	# Initialize randomized measurements
	random_measure = RandomShadow(h2o_mol)
	
	# Perform randomized measurements
	expectation_random = random_measure.measure(M=1000, nproc=1)
	print(f'Randomized measurement expectation: {expectation_random:>12.8f}')
	
	# Initialize cumulant expansion with random_measure
	cumulant = QCumulant(protocol=random_measure)
	
	# Generate non-crossing partitions (max block size of 4) and compute expectation
	cumulant.generate_partitions(max_size=4, num_threads=4)
	expectation_cumulant = cumulant.compute_expectation_bits()
	print(f'Cumulant expansion expectation: {expectation_cumulant:>12.8f}')
```

## Documentation

Documentation on Python API, `libmeas` which expose C++ functions as well as installation instruction and usage are available at `/docs`. To build the documentation locally, simply navigate to `docs` and build using `make html` or `make latexpdf`.

Latest documentation is available online at [quemb.readthedocs.io](http://qumeas.readthedocs.io/)..
