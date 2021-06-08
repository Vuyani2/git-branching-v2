import unittest
from main import MiniCalculator


class TestMiniCalculator(unittest.TestCase):

    def test_add(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2,2), 4, "Adding 2 to 2 should equal 4")

        def test_subtract(self):
            mini_instance = MiniCalculator()
            self.assertEqual(mini_instance.subtract((2,2), 0, "Subtracting two from two should give you zero"))
