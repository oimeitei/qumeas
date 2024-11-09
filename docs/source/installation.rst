Installation Guide
==================

This section provides instructions to various ways of installing quMeas. The recommended option is to use ``pip``:::

  pip install qumeas

PyPI also host pre-built binary wheels for Linux, Windows, and MacOS. Wheels are available for Python 3.8 - 3.12. For a more low-level installation, see below to install from source. 


Installation from source
^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisites
"""""""""""""

- **Python** (3.8 or higher)
- **CMake** (3.30.0 or higher)
- **numpy**: For handling numerical arrays
- **scipy**: For scientific computations

**Optional Dependencies**:

- **Eigen**: C++ template library for linear algebra
- **pybind11**: Library for binding C++ code to Python
- **qiskit**, **qiskit-nature**, **qiskit-aer**: Quantum computing SDK

If `Eigen` and `pybind11` are not installed, quMeas will automatically install during build at `/external` directory. Qiskit is required to use ``qumeas.qiskit_utils.Mole`` and ``qumeas.qiskit_utils.qiskitStatePreparation``, to get Hamiltonian for molecules and to use qiskit's funcitonalities to get measurement outcomes.

Clone the repository:

::
   
   git clone https://github.com/oimeitei/qumeas.git


Option 1: Install with ``build`` and ``pip``
""""""""""""""""""""""""""""""""""""""""""""

Navigate to the roor directory and run the following to build wheel and install::

  python -m build --wheel
  pip install dist/qumeas-*.whl

This will automatically handle dependencies and build C++ components.

Option 2: Build with ``CMake`` and add to ``PYTHONPATH``
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

1. Create a build directory at the root directory: ::

     mkdir build && cd build

2. Run ``CMake`` to configure the build: ::

     cmake ..

3. Compile: ::

     make -j$(nproc)

4. Make Python find qumeas: ::

     export PYTHONPATH=/path/to/qumeas/python:$PYTHONPATH
