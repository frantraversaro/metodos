import unittest
import numpy as np

from source.vector_class import Vector


class TestVectorClass(unittest.TestCase):
    def test_sum(self):
        v1 = Vector([4, -1, 5, 10])
        v2 = Vector([1, 6, -1, 5])
        v3 = v1 + v2

        self.assertEqual(v3, Vector([5,5,4,15]))

    def test_scalar_mult(self):
        v1 = Vector([4, -1, 5, 10])
        v2 = 3 * v1
        self.assertEqual(v2, Vector([12, -3, 15, 30]))

        v3 = Vector([1, 6, -1, 5])
        v4 = -1 * v3

        self.assertEqual(v4, Vector([-1, -6, 1, -5]))

    def test_representation(self):
        v1 = Vector([4, -1, 5, 10])

        self.assertEqual(str(v1), "Vector(4, -1, 5, 10)")