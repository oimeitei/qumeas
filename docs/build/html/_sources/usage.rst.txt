Usage Guide
===========

This section shows how to use ``QuMeas`` library to compute expectation values of Pauli strings. See ``/examples`` for more.


**Computing Expectation Values with Randomized Measurement and Cumulant Expansion**

In this example, we first perform randomized measurement (and get the expectation value as well). Then, we use cumulant expansion with the measurement bits from the randomized measurement to estimate expectation value of the Hamiltonian of water molecule.::
  
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

