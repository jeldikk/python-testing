import unittest
from arithmetic import addition, multiplication, division, remainder

print("TestArithmeticError class")

class TestArithmeticError(unittest.TestCase):

    def test_add(self):
        self.assertEqual(addition.add([3],2),5,"Should be an ValueError")


    def test_multiply(self):
        self.assertEqual(multiplication.multiply(3,[2]),5,"Should be an ValueError")


if __name__ == "__main__":
    unittest.main()