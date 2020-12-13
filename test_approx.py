import unittest
from rovel import approximate_number

class TestApprox(unittest.TestCase):
    def test1(self):
        for i in range(1, 11):
            self.assertEqual(approximate_number(i), str(i))

    def test2(self):
        for i in range(1000, 1500):
            self.assertEqual(approximate_number(i), f"{str(i)[0]}k")

if __name__ == '__main__':
    unittest.main()