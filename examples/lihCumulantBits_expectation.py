'''
Computes expectation value using the cumulant expansion, provide random measurement outcomes.
'''
from qumeas import PauliContainer, QCumulant

# Pauli operators and their coefficients in the Hamiltonian, H = \sum_i c_i * P_i
Pauli_strings = ['IIII', 'IIIZ', 'IIZI', 'IIZZ', 'IZII', 'IZIZ', 'YYII', 'YYIZ', 'XXII', 'XXIZ', 'ZIII', 'ZIIZ', 'IIYY', 'IZYY', 'IIXX', 'IZXX', 'YYYY', 'XXYY', 'YYXX', 'XXXX', 'ZIYY', 'ZIXX', 'IZZI', 'YYZI', 'XXZI', 'ZIZI', 'ZZII']

Pauli_strings_coeff = [-0.72913365, 0.16199478, -0.01324373, 0.05413045, 0.16199478, 0.12444773, 0.01291061, 0.01153635, 0.01291061, 0.01153635, -0.01324373, 0.05706341,0.01291061, 0.01153635, 0.01291061, 0.01153635, 0.00293297, 0.00293297, 0.00293297, 0.00293297, -0.00137435, -0.00137435, 0.05706341, -0.00137435, -0.00137435, 0.08479611, 0.05413045]

basis = ['XYZX', 'ZYYZ', 'YYZY', 'ZXXZ', 'YYYY', 'ZYXY', 'ZZXX', 'YYYY', 'YZZX', 'ZXXY', 'YZXY', 'XZYX', 'XZZY', 'XZZX', 'ZXZZ', 'YZZZ', 'YXZZ', 'ZYZX', 'YXYY', 'ZXYZ', 'ZXXZ', 'XZXZ', 'ZXXX', 'XYZY', 'ZXYX', 'YZXY', 'ZXXY', 'ZZYX', 'XXXZ', 'ZZYX', 'ZZXY', 'ZZZX', 'YYYZ', 'ZXXY', 'ZYZY', 'YZXZ', 'YYYX', 'ZYZZ', 'ZZZX', 'XYYY', 'XYZX', 'ZYZZ', 'XZYY', 'ZZXX', 'XXZY', 'ZYYX', 'ZXXX', 'XZYX', 'YZZX', 'XZZZ', 'ZZXX', 'XYYZ', 'ZXZY', 'XZZY', 'XXXY', 'XXXX', 'ZYXZ', 'ZXYZ', 'YZYX', 'XZZY', 'ZXXZ', 'ZYZY', 'XXXY', 'YZZY', 'ZXXZ', 'YYZZ', 'ZYYZ', 'ZZYY', 'XZYZ', 'ZXZZ', 'ZYZY', 'YXZX', 'ZZXX', 'YZZY', 'ZXZY', 'XYXX', 'XZZX', 'YYXZ', 'ZYYY', 'XYYX', 'XXZX', 'ZXYY', 'ZYXY', 'ZZXZ', 'YZYX', 'YZZZ', 'XXZX', 'XZZZ', 'ZYXZ', 'XYYZ', 'XZZX', 'YXXY', 'XXXZ', 'ZYXX', 'XZZZ', 'YYXX', 'XXZY', 'XXYX', 'ZXYY', 'YZZX']

bits = ['0101', '0111', '1000', '0001', '1011', '0000', '0100', '0100', '1101', '0010', '0101', '0111', '1100', '0101', '0001', '0101', '0001', '0001', '0010', '0111', '0001', '1111', '0100', '1100', '0110', '0111', '0010', '0110', '1111', '0111', '0101', '0100', '1001', '0000', '0000', '1101', '0101', '0101', '0100', '0010', '1001', '0101', '0111', '0110', '0100', '0001', '0100', '0111', '0101', '1101', '0111', '0001', '0000', '1100', '1000', '0100', '0111', '0001', '1111', '1100', '0001', '0001', '0000', '0101', '0111', '0101', '0011', '0111', '1101', '0001', '0000', '0100', '0101', '1100', '0100', '0010', '1101', '1101', '0101', '0111', '1001', '0111', '0111', '0111', '1100', '1101', '0101', '0101', '0011', '1001', '0100', '1110', '0001', '0010', '0101', '0000', '0001', '0011', '0110', '0101']

# Define a PauliContainer object
myPauli = PauliContainer(Nqubit=4, 
                         pauli_list=Pauli_strings,
                         pauli_list_coeff=Pauli_strings_coeff)

# Initialize RandomShadow
myCumu = QCumulant(PauliObj=myPauli,
                   measure_basis=basis,
                   measure_outcome_bits=bits)

# Generate partitions
myCumu.generate_partitions(max_size=2, num_threads=4)

# Compute expectation value
expectation_val = myCumu.compute_expectation_bits()
                                   
print(f'Expectation value from Cumulant expansion is: {expectation_val:>12.8f}')
