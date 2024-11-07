'''
Compute expectation value using cumulant expansion of Pauli strings.
This uses measurement uses state vector stored in Mole.PauliObj.

'''
from qumeas.qiskit_utils import Mole
from qumeas import QCumulant

# Get pre-defined molecule
h2o_mol = Mole(atom='h2o')

# Initialize QCumulant
myCumu = QCumulant(protocol=h2o_mol

# Generate non-crossing partition up to a maximum block size of 4
myCumu.generate_partitions(max_size=4,
                           num_threads=4)

expectationCumu = myCumu.compute_expectation_bits()
print(f'Expectation value from random measurement protocol is: {expectationCumu:>12.8f}')


      
