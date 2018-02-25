# -*- coding: utf-8 -*-

__author__ = 'Myong-Hoon Jeon'

from unittest import main, TestCase


def insertion_sort(li):
    """ Python implementation of insertion sort
    args:
        li = 정렬되지 않은 int의 리스트
    returns:
        li를 오른차순으로 정렬한 int의 리스트
    """
    list_length = len(li)

    for i in range(1, list_length):
        current_element = li[i]  # 삽입해야하는 element
        correct_index = i  # current_element의 올바른 index

        # li[correct_index - 1] 는 current_element 보다 뒤에 있어야 한다.
        while current_element < li[correct_index - 1] and correct_index > 0:
            li[correct_index] = li[correct_index - 1]
            correct_index = correct_index - 1

        li[correct_index] = current_element

    return li


class InsertionSortTest(TestCase):

    def setUp(self):
        self.unordered_list_in_reverse_order = [5, 4, 3, 2, 1]
        self.unordered_list_without_order = [2, 4, 5, 3, 1]

    def test_insertion_sort_should_return_ordered_list_from_unordered_list(self):
        self.assertEqual([1, 2, 3, 4, 5],
                         insertion_sort(self.unordered_list_in_reverse_order))
        self.assertEqual([1, 2, 3, 4, 5],
                         insertion_sort(self.unordered_list_without_order))


if __name__ == '__main__':
    main()
