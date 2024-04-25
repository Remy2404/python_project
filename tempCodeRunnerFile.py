import unittest
from Gram_Schmidt_process import gram_schmidt
import numpy as np

class TestGramSchmidt(unittest.TestCase):
    
    def test_gram_schmidt_orthonormal(self):
        a = np.array([1, 0, 0])
        b = np.array([0, 1, 0])
        c = np.array([0, 0, 1])
        
        q = gram_schmidt(a, b, c)
        
        self.assertAlmostEqual(np.dot(q[0], q[1]), 0)
        self.assertAlmostEqual(np.dot(q[0], q[2]), 0)
        self.assertAlmostEqual(np.dot(q[1], q[2]), 0)
        
        self.assertAlmostEqual(np.linalg.norm(q[0]), 1)
        self.assertAlmostEqual(np.linalg.norm(q[1]), 1)
        self.assertAlmostEqual(np.linalg.norm(q[2]), 1)

    def test_gram_schmidt_r_matrix(self):
        a = np.array([1, -1, 0])
        b = np.array([2, 0, -2])
        c = np.array([3, -3, 3])
        
        q, r = gram_schmidt(a, b, c, full_matrices=True)
        
        expected_r = np.array([[1, -1, 0], 
                               [0, 2, -2],
                               [0, 0, 3]])
        
        self.assertTrue(np.allclose(r, expected_r))
        
if __name__ == '__main__':
    unittest.main()
