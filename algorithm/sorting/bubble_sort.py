# -*- coding: utf-8 -*-

from unittest import TestCase, main

__author__ = 'MH Jeon'


def bubble_sort(li):
    """ Python implementation of bubble sort
    args:
        li = unordered list of elements in integer
    returns:
        ordered list of input li in ascending order
    BigO:
        O(n**2): there are better ways to implemet sorting
                 i.e)quicksort, mergesort
    """
    li_length = len(li)

    for i in range(li_length - 1):
        for j in range(li_length - 1):
            if li[j] > li[j + 1]:
                temp = li[j+1]
                li[j+1] = li[j]
                li[j] = temp
                ''' better code
                reference: https://github.com/minsuk-heo/problemsolving\
                           /blob/master/sort/BubbleSort.py

                alist[j], alist[j+1] = alist[j+1], alist[j]
                '''
    return li


class BubbleSortTest(TestCase):

    def setUp(self):
        self.unordered_list = [4, 3, 1, 5, 2]
        self.unordered_list_with_duplicates = [4, 3, 1, 1, 5, 2]

    def test_sort_function_should_return_ordered_list_in_ascending_order(self):
        self.assertEqual(bubble_sort(self.unordered_list),
                         [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort(self.unordered_list_with_duplicates),
                         [1, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    main()
