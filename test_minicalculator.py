import unittest
from main import MiniCalculator


class TestMiniCalculator(unittest.TestCase):

    def test_add(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2, 2), 4, "Adding 2 to 2 should equal 4")

    def test_subtract(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.subtract(2, 2), 0, "Subtracting two from two should give you zero")

    def test_multiplication(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.multiplication(2, 2), 4, "Multiplying 2 qnd 2 should equal to 4")

    def test_divition(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.divition(2, 2), 1, "Dividing 2 by 2 should equal to 1")


