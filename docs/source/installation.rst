Installation Guide
==================

This section provides instructions to install quMeas. quMeas depends on ``Eigen`` and ``pybind11``, if they are not installed on your system, they are provided in the ``/external`` directory and will be used automatically.

Furthermore, ``qiskit``, including ``qiskit-nature`` and ``qiskit-aer`` is required to use ``qumeas.Mole`` and ``qumeas.qiskitStatePreparation``.

Prerequisites
^^^^^^^^^^^^^

- **Python** (3.8 or higher)
- **CMake** (3.30.0 or higher)
- **numpy**: For handling numerical arrays
- **scipy**: For scientific computations

**Optional Dependencies**:

- **Eigen**: C++ template library for linear algebra
- **pybind11**: Library for binding C++ code to Python
- **qiskit**, **qiskit-nature**, **qiskit-aer**: Quantum computing SDK

If `Eigen` and `pybind11` are not installed, quMeas will use the versions included in the `/external` directory. When cloning the repository, make sure to include the `--recursive` flag to download all submodules:

::
   
   git clone --recursive https://github.com/oimeitei/qumeas.git


Installation Options
^^^^^^^^^^^^^^^^^^^^

quMeas can be installed using either ``pip`` or ``CMake``:

Option 1: Install with ``pip``
""""""""""""""""""""""""""""""

To install quMeas via ``pip``, at the root directory, simply run::

  pip install .


This will automatically handle dependencies and build C++ components.

Option 2: Build and Install with ``CMake``
""""""""""""""""""""""""""""""""""""""""""

1. Create a build directory at the root directory: ::

     mkdir build && cd build

2. Run ``CMake`` to configure the build: ::

     cmake ..

3. Compile: ::

     make -j$(nproc)

4. Make Python find qumeas: ::

     export PYTHONPATH=/path/to/qumeas/python:$PYTHONPATH
