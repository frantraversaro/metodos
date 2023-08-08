import unittest

from source.matrix_class import Matrix
from source.vector_class import Vector


class TestVectorClass(unittest.TestCase):
    def test_repr(self):
        A = Matrix([Vector([1, 0]), Vector([2, -5]), Vector([-1, 3])])
        self.assertEqual(str(A), 'Matrix ( \n1, 2, -1\n0, -5, 3\n)')

    def test_vector_mult(self):
        A = Matrix([Vector([1,0]), Vector([2,-5]), Vector([-1,3])])
        x = Vector([4,3,7])
        self.assertEqual(A * x, Vector([3,6]))

        A = Matrix(
            [Vector([2, 8, -5]), Vector([-3, 0, 2])]
        )

        x = Vector([4, 7])

        self.assertEqual(A * x, Vector([-13, 32, -6]))


