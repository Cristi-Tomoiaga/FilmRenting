"""
Test cases for random_generation module
"""
import unittest

from utils.random_generation import generate_random_string, generate_random_cnp


class TestCaseRandomGeneration(unittest.TestCase):
    def test_generate_random_string(self):
        """
        Test function for generate_random_string
        """
        length = 10
        res = generate_random_string(length)

        self.assertEqual(len(res), length)

    def test_generate_random_cnp(self):
        """
        Test function for generate_random_cnp
        """
        cnp = generate_random_cnp()
        self.assertEqual(len(cnp), 13)


if __name__ == '__main__':
    unittest.main()
