import unittest
from Function import function



class Function_Test(unittest.TestCase):

    def test_T0(self):
        f = function(8)
        f.vect = [0, 1, 0, 1, 0, 1, 0, 1]
        self.assertTrue(f.T0())

    def test_T1(self):
        f = function(8)
        f.vect = [0, 1, 0, 1, 0, 1, 0, 1]
        self.assertTrue(f.T1())

    def test_S(self):
        f = function(8)
        f.vect = [0, 1, 0, 1, 0, 1, 0, 1]
        self.assertTrue(f.S())

    def test_M(self):
        f = function(8)
        f.vect = [0, 1, 0, 1, 0, 1, 0, 1]
        self.assertTrue(f.M())

    def test_L(self):
        f = function(8)
        f.vect = [0, 0, 0, 0, 0, 0, 0, 1]
        self.assertTrue(f.L())


if __name__ == '__main__':
    unittest.main()