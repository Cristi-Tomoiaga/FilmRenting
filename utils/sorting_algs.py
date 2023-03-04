"""
Utility functions for sorting a list of objects using different implementations/algorithms
"""
from enum import Enum


class SortingMethod(Enum):
    """
    Enum for possible sorting methods
    """
    MERGE_SORT = 1
    BINGO_SORT = 2


class Sorting:
    """
    Wrapper class for the sorting algorithms
    """
    @staticmethod
    def __merge(list_obj1, list_obj2, compare):
        """
        Merges the two sorted lists list_obj1 and list_obj2 respecting the order relation compare

        :param list_obj1: a sorted list of objects
        :param list_obj2: a sorted list of objects
        :param compare: function of two parameters that returns True if the two parameters respect the order relation
        :return: the merged list of objects
        """
        merged_list = []
        i = 0
        j = 0
        while i < len(list_obj1) and j < len(list_obj2):
            if compare(list_obj1[i], list_obj2[j]):
                merged_list.append(list_obj1[i])
                i += 1
            else:
                merged_list.append(list_obj2[j])
                j += 1

        while i < len(list_obj1):  # copy remaining elements
            merged_list.append(list_obj1[i])
            i += 1

        while j < len(list_obj2):  # copy remaining elements
            merged_list.append(list_obj2[j])
            j += 1

        return merged_list

    @staticmethod
    def __merge_sort(list_obj, compare):
        """
        Returns the sorted list list_obj using the MergeSort algorithm and respecting the order relation compare

        :param list_obj: a list of objects
        :param compare: function of two parameters that returns True if the two parameters respect the order relation
        :return: the sorted list of objects
        """
        if len(list_obj) <= 1:
            return list_obj

        m = (0 + len(list_obj)) // 2
        lower_half = Sorting.__merge_sort(list_obj[:m], compare)
        higher_half = Sorting.__merge_sort(list_obj[m:], compare)

        return Sorting.__merge(lower_half, higher_half, compare)

    @staticmethod
    def __bingo_sort(list_obj, compare, key):
        """
        Returns the sorted list from list_obj using the BingoSort algorithm and respecting the order relation compare

        :param list_obj: a list of objects
        :param compare: a function of two parameters that returns True if the two parameters respect the order relation
        :param key: a function with one argument that returns the value to be compared for each element - optional, by default returns the element
        :return: the sorted list of objects
        """
        sorted_list = list_obj[:]  # make a copy

        if len(sorted_list) <= 1:  # trivial solution
            return sorted_list

        # find the first minimum - first step
        n = len(sorted_list)
        i = 0
        curr_min = sorted_list[i]
        for j in range(i + 1, n):
            if compare(sorted_list[j], curr_min):
                curr_min = sorted_list[j]

        # jump over equal minima at the start
        while i < n and key(sorted_list[i]) == key(curr_min):
            i += 1

        # repeat the previous steps
        while i < n:
            prev_min = curr_min
            curr_min = sorted_list[i]

            # find the next minimum and move the elements equal to prev_min to the start
            for j in range(i + 1, n):
                if compare(sorted_list[j], curr_min):
                    if key(sorted_list[j]) != key(prev_min):
                        curr_min = sorted_list[j]
                    else:
                        sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
                        i += 1

            # jump over equal minima at the start
            while i < n and key(sorted_list[i]) == key(curr_min):
                i += 1

        return sorted_list

    @staticmethod
    def sorted(list_obj, *, key=None, reverse=False, method):
        """
        Returns the sorted list from list_obj using the specified algorithm, direction of sorting and key

        :param list_obj: a list of objects
        :param key: a function with one argument that returns the value to be compared for each element - optional, by default returns the element
        :param reverse: sorts in descending order if True, ascending otherwise - optional, by default False
        :param method: the sorting method used
        :return: the sorted list of objects
        """
        key = (lambda x: x) if key is None else key
        compare = (lambda x, y: key(x) < key(y)) if not reverse else (lambda x, y: key(y) < key(x))

        if method == SortingMethod.MERGE_SORT:
            return Sorting.__merge_sort(list_obj, compare)
        elif method == SortingMethod.BINGO_SORT:
            return Sorting.__bingo_sort(list_obj, compare, key)
