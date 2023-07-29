import unittest
import numpy as np

from source.reduce_matrix import reduce_matrix


class TestReduceMatrix(unittest.TestCase):

    def test_trivial(self):
        mtx = np.array([
            [1, 0, 3],
            [0, 1, 2],

        ])

        reduced_mtx = reduce_matrix(mtx)
        expected_output = np.array([[1., 0., 3.], [0., 1., 2.]])

        self.assertTrue(np.array_equal(reduced_mtx, expected_output))

    def test_simple_matrix(self):
        mtx = np.array([
            [1, 3, 4],
            [-4, 2, -6],

        ])

        reduced_mtx = reduce_matrix(mtx)
        expected_output = np.array([[1., 0., 1.86], [0., 1., 0.71]])

        self.assertTrue(np.array_equal(reduced_mtx, expected_output))

    def test_inconsistent(self):
        mtx = np.array([
            [1, 0, 3],
            [0, 0, 2],

        ])

        reduced_mtx = reduce_matrix(mtx)
        expected_output = np.array([[1., 0., 0.], [0., 0., 1.]])

        self.assertTrue(np.array_equal(reduced_mtx, expected_output))

    def test_flow_problem(self):
        mtx = np.array([
            [1, -1, 0, 0, 0, 100],
            [0, 1, -1, -1, 0, -400],
            [0, 0, 0, 1, -1, 200],
            [-1, 0, 0, 0, 1, -300],
            [0, 0, 1, 0, 0, 400],
        ])

        reduced_mtx = reduce_matrix(mtx)
        expected_output = np.array([[1., 0., 0., 0., -1., 300.],
                                    [0., 1., 0., 0., -1., 200.],
                                    [0., 0., 1., 0., 0., 400.],
                                    [0., 0., 0., 1., -1., 200.],
                                    [0., 0., 0., 0., 0., 0.]])

        self.assertTrue(np.array_equal(reduced_mtx, expected_output))


if __name__ == '__main__':
    unittest.main()
