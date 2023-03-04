"""
Test cases for sorting_algs module
"""
import unittest

from utils.sorting_algs import Sorting, SortingMethod


class TestCaseSorting(unittest.TestCase):
    def setUp(self):
        self.l1 = []
        self.l2 = [1, 2, 3]
        self.l3 = [3, 2, 1]
        self.l4 = [1]
        self.l5 = [1, 5, 2, 11, 3, 7, 8, 2]
        self.l5 = [1, 7, 2, 11, 3, 5, 8, 4]
        self.l6 = ["abc", "bcd", "adcse", "sjdhe"]
        self.key1 = lambda x: -x if x >= 5 else x
        self.key2 = lambda x: x[0:2]

    def test_all_sorts(self):
        for _method in [SortingMethod.BINGO_SORT]:
            self.assertEqual(Sorting.sorted(self.l1, method=_method), sorted(self.l1))
            self.assertEqual(Sorting.sorted(self.l2, method=_method), sorted(self.l2))
            self.assertEqual(Sorting.sorted(self.l3, method=_method), sorted(self.l3))
            self.assertEqual(Sorting.sorted(self.l4, method=_method), sorted(self.l4))
            self.assertEqual(Sorting.sorted(self.l5, method=_method), sorted(self.l5))
            self.assertEqual(Sorting.sorted(self.l6, method=_method), sorted(self.l6))

            self.assertEqual(Sorting.sorted(self.l1, reverse=True, method=_method), sorted(self.l1, reverse=True))
            self.assertEqual(Sorting.sorted(self.l2, reverse=True, method=_method), sorted(self.l2, reverse=True))
            self.assertEqual(Sorting.sorted(self.l3, reverse=True, method=_method), sorted(self.l3, reverse=True))
            self.assertEqual(Sorting.sorted(self.l4, reverse=True, method=_method), sorted(self.l4, reverse=True))
            self.assertEqual(Sorting.sorted(self.l5, reverse=True, method=_method), sorted(self.l5, reverse=True))
            self.assertEqual(Sorting.sorted(self.l6, reverse=True, method=_method), sorted(self.l6, reverse=True))

            self.assertEqual(Sorting.sorted(self.l1, key=self.key1, method=_method), sorted(self.l1, key=self.key1))
            self.assertEqual(Sorting.sorted(self.l2, key=self.key1, method=_method), sorted(self.l2, key=self.key1))
            self.assertEqual(Sorting.sorted(self.l3, key=self.key1, method=_method), sorted(self.l3, key=self.key1))
            self.assertEqual(Sorting.sorted(self.l4, key=self.key1, method=_method), sorted(self.l4, key=self.key1))
            self.assertEqual(Sorting.sorted(self.l5, key=self.key1, method=_method), sorted(self.l5, key=self.key1))
            self.assertEqual(Sorting.sorted(self.l6, key=self.key2, method=_method), sorted(self.l6, key=self.key2))


if __name__ == '__main__':
    unittest.main()
