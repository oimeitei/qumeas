.. quMeas master file, created by
   sphinx-quickstart on Tue Nov  5 09:49:11 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

quMeas Documentation
====================

quMeas is a high-performance multi-threaded library for computing expectation values of Pauli strings using randomized measurement techniques. It combines **classical shadow tomography** with **cumulant average expansion** and statistical partitioning of Pauli strings, providing a powerful toolset for Pauli measurement. quMeas is designed to integrate seamlessly with other quantum computing software, such as Qiskit, enabling flexible use in a variety of quantum simulation and optimization tasks.

High-Performance Design
"""""""""""""""""""""""

To achieve optimal performance, quMeas employs a multi-layered parallelization strategy and is implemented in C++ for performance-critical operations. This architecture allows quMeas to scale efficiently on multi-core systems, delivering high performance in the estimation of Pauli expectation values from quantum measurement outcomes.

The core library, **libmeas**, is built in C++ to leverage its speed and fine-grained control over computational resources. Using **Pybind11**, these C++ components are directly accessible in Python, making quMeas a high-performance backend for Python applications. quMeas is compatible with quantum algorithms such as **Variational Quantum Eigensolver (VQE)** for molecular simulation and **Quantum Approximate Optimization Algorithm (QAOA)** for combinatorial optimization, providing reliable expectation value estimations within these frameworks.

Efficient Parallelization
"""""""""""""""""""""""""

quMeas employs a robust, multi-threaded architecture to manage large datasets and compute-independent tasks in parallel. Key features of this parallelization strategy include:
- **Task Queues and Asynchronous Parallelism**: For complex tasks like generating non-crossing partitions, quMeas uses task queues and asynchronous tasks to distribute computations across available CPU cores, achieving high concurrency.
- **OpenMP Acceleration**: Critical loops and data processing operations are parallelized using OpenMP, allowing data-intensive computations to be efficiently split across multiple cores.

This layered approach to parallelism maximizes CPU utilization, ensuring that quMeas performs efficiently and scales well on modern hardware for demanding quantum simulation workloads.


.. toctree::
   :maxdepth: 1

   installation
   usage
   modules
   cpp_bindings
