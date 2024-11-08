import pytest
from qumeas import PauliContainer, QCumulant

@pytest.mark.parametrize("max_size, expected_partitions", [
    (4, [[[]], [[[3]]], [[[2]]], [[[3], [2]], [[3, 2]]], [[[1]]], [[[3], [1]], [[3, 1]]], [[[1], [0]], [[1, 0]]], [[[3], [1], [0]], [[3], [1, 0]], [[3, 0], [1]], [[3, 1], [0]], [[3, 1, 0]]], [[[1], [0]], [[1, 0]]], [[[3], [1], [0]], [[3], [1, 0]], [[3, 0], [1]], [[3, 1], [0]], [[3, 1, 0]]], [[[0]]], [[[3], [0]], [[3, 0]]], [[[3], [2]], [[3, 2]]], [[[3], [2], [1]], [[3], [2, 1]], [[3, 1], [2]], [[3, 2], [1]], [[3, 2, 1]]], [[[3], [2]], [[3, 2]]], [[[3], [2], [1]], [[3], [2, 1]], [[3, 1], [2]], [[3, 2], [1]], [[3, 2, 1]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3], [2, 1, 0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 1, 0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]], [[3, 2, 0], [1]], [[3, 2, 1], [0]], [[3, 2, 1, 0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3], [2, 1, 0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 1, 0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]], [[3, 2, 0], [1]], [[3, 2, 1], [0]], [[3, 2, 1, 0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3], [2, 1, 0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 1, 0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]], [[3, 2, 0], [1]], [[3, 2, 1], [0]], [[3, 2, 1, 0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3], [2, 1, 0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 1, 0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]], [[3, 2, 0], [1]], [[3, 2, 1], [0]], [[3, 2, 1, 0]]], [[[3], [2], [0]], [[3], [2, 0]], [[3, 0], [2]], [[3, 2], [0]], [[3, 2, 0]]], [[[3], [2], [0]], [[3], [2, 0]], [[3, 0], [2]], [[3, 2], [0]], [[3, 2, 0]]], [[[2], [1]], [[2, 1]]], [[[2], [1], [0]], [[2], [1, 0]], [[2, 0], [1]], [[2, 1], [0]], [[2, 1, 0]]], [[[2], [1], [0]], [[2], [1, 0]], [[2, 0], [1]], [[2, 1], [0]], [[2, 1, 0]]], [[[2], [0]], [[2, 0]]], [[[1], [0]], [[1, 0]]]]),
    (3, [[[]], [[[3]]], [[[2]]], [[[3], [2]], [[3, 2]]], [[[1]]], [[[3], [1]], [[3, 1]]], [[[1], [0]], [[1, 0]]], [[[3], [1], [0]], [[3], [1, 0]], [[3, 0], [1]], [[3, 1], [0]], [[3, 1, 0]]], [[[1], [0]], [[1, 0]]], [[[3], [1], [0]], [[3], [1, 0]], [[3, 0], [1]], [[3, 1], [0]], [[3, 1, 0]]], [[[0]]], [[[3], [0]], [[3, 0]]], [[[3], [2]], [[3, 2]]], [[[3], [2], [1]], [[3], [2, 1]], [[3, 1], [2]], [[3, 2], [1]], [[3, 2, 1]]], [[[3], [2]], [[3, 2]]], [[[3], [2], [1]], [[3], [2, 1]], [[3, 1], [2]], [[3, 2], [1]], [[3, 2, 1]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3], [2, 1, 0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 1, 0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]], [[3, 2, 0], [1]], [[3, 2, 1], [0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3], [2, 1, 0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 1, 0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]], [[3, 2, 0], [1]], [[3, 2, 1], [0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3], [2, 1, 0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 1, 0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]], [[3, 2, 0], [1]], [[3, 2, 1], [0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3], [2, 1, 0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 1, 0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]], [[3, 2, 0], [1]], [[3, 2, 1], [0]]], [[[3], [2], [0]], [[3], [2, 0]], [[3, 0], [2]], [[3, 2], [0]], [[3, 2, 0]]], [[[3], [2], [0]], [[3], [2, 0]], [[3, 0], [2]], [[3, 2], [0]], [[3, 2, 0]]], [[[2], [1]], [[2, 1]]], [[[2], [1], [0]], [[2], [1, 0]], [[2, 0], [1]], [[2, 1], [0]], [[2, 1, 0]]], [[[2], [1], [0]], [[2], [1, 0]], [[2, 0], [1]], [[2, 1], [0]], [[2, 1, 0]]], [[[2], [0]], [[2, 0]]], [[[1], [0]], [[1, 0]]]]),
    (2, [[[]], [[[3]]], [[[2]]], [[[3], [2]], [[3, 2]]], [[[1]]], [[[3], [1]], [[3, 1]]], [[[1], [0]], [[1, 0]]], [[[3], [1], [0]], [[3], [1, 0]], [[3, 0], [1]], [[3, 1], [0]]], [[[1], [0]], [[1, 0]]], [[[3], [1], [0]], [[3], [1, 0]], [[3, 0], [1]], [[3, 1], [0]]], [[[0]]], [[[3], [0]], [[3, 0]]], [[[3], [2]], [[3, 2]]], [[[3], [2], [1]], [[3], [2, 1]], [[3, 1], [2]], [[3, 2], [1]]], [[[3], [2]], [[3, 2]]], [[[3], [2], [1]], [[3], [2, 1]], [[3, 1], [2]], [[3, 2], [1]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]]], [[[3], [2], [1], [0]], [[3], [2], [1, 0]], [[3], [2, 0], [1]], [[3, 0], [1], [2]], [[3], [2, 1], [0]], [[3, 0], [2, 1]], [[3, 1], [0], [2]], [[3, 2], [1], [0]], [[3, 2], [1, 0]]], [[[3], [2], [0]], [[3], [2, 0]], [[3, 0], [2]], [[3, 2], [0]]], [[[3], [2], [0]], [[3], [2, 0]], [[3, 0], [2]], [[3, 2], [0]]], [[[2], [1]], [[2, 1]]], [[[2], [1], [0]], [[2], [1, 0]], [[2, 0], [1]], [[2, 1], [0]]], [[[2], [1], [0]], [[2], [1, 0]], [[2, 0], [1]], [[2, 1], [0]]], [[[2], [0]], [[2, 0]]], [[[1], [0]], [[1, 0]]]]),
    (1, [[[]], [[[3]]], [[[2]]], [[[3], [2]]], [[[1]]], [[[3], [1]]], [[[1], [0]]], [[[3], [1], [0]]], [[[1], [0]]], [[[3], [1], [0]]], [[[0]]], [[[3], [0]]], [[[3], [2]]], [[[3], [2], [1]]], [[[3], [2]]], [[[3], [2], [1]]], [[[3], [2], [1], [0]]], [[[3], [2], [1], [0]]], [[[3], [2], [1], [0]]], [[[3], [2], [1], [0]]], [[[3], [2], [0]]], [[[3], [2], [0]]], [[[2], [1]]], [[[2], [1], [0]]], [[[2], [1], [0]]], [[[2], [0]]], [[[1], [0]]]])
])


def test_partition_generation(max_size, expected_partitions):
    # Test partition generation with various max_size configurations

    Pauli_strings = ['IIII', 'IIIZ', 'IIZI', 'IIZZ', 'IZII', 'IZIZ', 'YYII', 'YYIZ', 'XXII', 'XXIZ', 'ZIII', 'ZIIZ', 'IIYY', 'IZYY', 'IIXX', 'IZXX', 'YYYY', 'XXYY', 'YYXX', 'XXXX', 'ZIYY', 'ZIXX', 'IZZI', 'YYZI', 'XXZI', 'ZIZI', 'ZZII']
    Pauli_strings_coeff = [-0.72913365, 0.16199478, -0.01324373, 0.05413045, 0.16199478, 0.12444773, 0.01291061, 0.01153635, 0.01291061, 0.01153635, -0.01324373, 0.05706341, 0.01291061, 0.01153635, 0.01291061, 0.01153635, 0.00293297, 0.00293297, 0.00293297, 0.00293297, -0.00137435, -0.00137435, 0.05706341, -0.00137435, -0.00137435, 0.08479611, 0.05413045]
    state_vector = [-7.00740547e-17+2.19218907e-16j, -5.51473089e-17-1.08265379e-16j,
                    -2.63334581e-16-2.57419584e-16j,  3.30631448e-16-6.69417684e-16j,
                    6.37659070e-18+9.99839007e-18j, -9.99721473e-01+1.39820785e-02j,
                    -5.25016201e-03+7.34286290e-05j,  2.56192699e-17+5.08469704e-16j,
                    -3.61975093e-16+3.01851169e-16j, -5.25016201e-03+7.34286290e-05j,
                    1.75008307e-02-2.44766162e-04j, -4.40672406e-17-9.17420415e-18j,
                    -2.44561606e-16+7.29023410e-16j, -6.92817642e-16-7.35213677e-16j,
                    -1.04233679e-16-3.10075922e-17j, -1.09342202e-16-1.17476009e-15j]

    # Define a PauliContainer object
    myPauli = PauliContainer(Nqubit=4, pauli_list=Pauli_strings, pauli_list_coeff=Pauli_strings_coeff, state_vector=state_vector)

    # Initialize QCumulant
    myCumu = QCumulant(PauliObj=myPauli)

    # Generate partitions
    myCumu.generate_partitions(max_size=max_size, num_threads=4)

    # Verify the partitions match the expected output
    assert myCumu.partitions == expected_partitions
