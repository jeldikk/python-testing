from arithmetic import addition, multiplication, division, remainder

import unittest

print("TestArithmetic tests")

class TestArthimetic(unittest.TestCase):

    def test_add(self):
        # print("test_add is here")
        self.assertEqual(addition.add(3,2),5,"Should be 5")

    def test_division(self):
        self.assertEqual(division.divide(3,2),1,"Should be 1.5")

    def test_multiplication(self):
        self.assertEqual(multiplication.multiply(2,3),6,"Should be 6")

    def test_remainder(self):
        self.assertEqual(remainder.rem(10,4),3,"Should be 2")

if __name__ == "__main__":
    unittest.main()