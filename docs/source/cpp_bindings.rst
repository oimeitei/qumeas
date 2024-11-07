libmeas
=======

Qumeas includes a set of high-performance C++ functions for quantum measurement using classical shadow tomography and cumulant exansion, compiled into ``libmeas``. These functions are accessible in Python through Pybind11 bindings. They can be simply imported like any other Python modules

::

  from qumeas.libmeas import *

- **generate_partition_non_crossing**: Function to generate non-crossing partitioning for a list of Pauli strings. To generate paritions, pass in list of Pauli strings, maximum size of a block in the partition, and number of threads. Pauli strings are a list of ``int``, with ``X = 1, Y = 2, Z = 3, I = 0``.
- **partition_expectation_bits**: Function to compute expectation values of a list of Pauli strings using cumulant expansion from quantum measurement output bits. The quantum measurement outbits can be from measurement using random basis in the classical shadow protocol. See ``QCumulant.compute_expectation_bits`` for details.
- **partition_expectation_state**: Function to compute expectation values of a list of Pauli strings using cumulant expansion from state vector. See ``QCumulant.compute_expectation_state`` for details.
- **compute_expectation_basis**: Function to compute expectation values of a list of Pauli strings using classical shadow tomography. See ``RandomMeasurement._compute_expectation`` for details.
