Usage
=====

This section shows how to use ``quMeas`` library to compute expectation values of Pauli strings. See ``/examples`` for more.


**Computing Expectation Values with Randomized Measurement and Cumulant Expansion**

In the first example, we will use measurement basis and outcomes (basis, bits) that is already available from a quantum simulation. For complete example, check ``lihCumulantBits_expectation.py`` and ``lihRandom_expectation.py`` in ``/examples``. Basically, basis is a list of Pauli strings, generated randomly and outcomes are list of classical bits from quantum measurement. Now, we will compute expectation values from classical shadow tomography and cumulant average expansion.::

  from qumeas import PauliContainer, RandomShadow, QCumulant

  # Get measurement basis and outcomes(basis, bits) from general quantum computing
  # packages. See documentation & examples for more details

  myPauli = PauliContainer(Nqubit=N, #Qubits
                     	   pauli_list=plist, # list of Pauli strings
		 	   pauli_list_coeff=clist) # list of coeffs for plist

  # Compute expectation with classical shadow tomography
  myRandom = RandomShadow(PauliObj=myPauli)
  expectation_random = myRandom.compute_expectation(basis, bits)

  # Compute expectation with cumulant expansion
  myCumu = QCumulant(PauliObj=myPauli,
		     measure_basis=basis,
		     measure_outcome_bits=bits)
  myCumu.generate_partitions(num_threads=4)
  expectation_cumulant = myCumu.compute_expectation_bits()



In the next example, we will first perform randomized measurement (and get the expectation value as well). Then, we use cumulant expansion with the measurement bits from the randomized measurement to estimate expectation value of the Hamiltonian of water molecule. This example uses functionalities from qiskit and so ``qiskit``, ``qiskit_nature``, and ``qiskit_aer`` needs to be installed.::
  
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

