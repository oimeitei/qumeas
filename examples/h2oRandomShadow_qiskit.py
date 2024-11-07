'''
Compute expectation value using randomized measurement protocol within
the framework of classical shadow tomography.
'''
from qumeas.qiskit_utils import Mole
from qumeas import RandomShadow

# Get pre-defined molecule
h2o_mol = Mole(atom='h2o')

# Inititalize random measurements
my_state = RandomShadow(h2o_mol)

# Measure using default setups
expectation_val = my_state.measure(M = 1000, # M: number of random measurement basis
                                   nproc = 1)

print(f'Expectation value from random measurement protocol is: {expectation_val:>12.8f}')
