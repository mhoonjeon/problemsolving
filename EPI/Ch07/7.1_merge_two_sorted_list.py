# -*- coding: utf-8 -*-

__author__ = "MH Jeon"

import os
from unittest import main, TestCase
import sys

from linked_list import LinkedList

""" To reuse code in data_structure directory, import sys.path from runtime

https://stackoverflow.com/questions/4383571/importing-files-from-different-folder/4383597
"""
sys.path.append(os.environ.get('ROOT_PATH')+'/data_structure')


class LinkedList(LinkedList):
    """ Override previous LinkedList class

    Newly Avaiable methods:
        next: get next node in list
    """

    def __init__(self):
        super().__init__()

    def next(self):
        cur = self.head
        return cur.next


def merge_two_sorted_lists(L1, L2):
    """ merge two sorted list in ascending order
    args:
        L1: list of integers in ascending order
        L2: list of integers in ascending order
    returns:
        list of ALL integers in L1, L2 in ascending order
    """
    new_list = []
    cur1 = L1.head.next
    cur2 = L2.head.next

    while cur1 is not None and cur2 is not None:
        if cur1.data > cur2.data:
            new_list.append(cur2)
            cur2 = cur2.next
        else:
            new_list.append(cur1)
            cur1 = cur1.next

    if cur1 is None:
        while cur2 is not None:
            new_list.append(cur2)
            cur2 = cur2.next

    else:
        while cur1 is not None:
            new_list.append(cur1)
            cur1 = cur1.next

    return new_list


class MergeTwoSortedListTest(TestCase):

    """"""

    def setUp(self):
        self.list1 = LinkedList()  # [1, 2, 3, 4, 7]
        self.list2 = LinkedList()  # [2, 2, 5, 6]

        self.list1.insert(1)
        self.list1.insert(2)
        self.list1.insert(3)
        self.list1.insert(4)
        self.list1.insert(7)

        self.list2.insert(2)
        self.list2.insert(2)
        self.list2.insert(5)
        self.list2.insert(6)

    def test_merge_two_ordered_list_should_return_ordered_list(self):
        merged_list = merge_two_sorted_lists(self.list1, self.list2)
        self.assertEqual([node.data for node in merged_list],
                         [1, 2, 2, 2, 3, 4, 5, 6, 7])

    def tearDown(self):
        del self.list1
        del self.list2


if __name__ == "__main__":
    main()
