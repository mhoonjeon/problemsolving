# -*- coding: utf-8 -*-

__author__ = "Myong-Hoon Jeon"

from unittest import TestCase, main


def merge(sorted_leftlist, sorted_rightlist):
    """ Get two sorted lists and merge into one
    args:
        sorted_leftlist, sorted_rightlist: 정렬된 2개의 리스트
    returns:
        sorted_leftlist, rigthlist의 모든 element가 정렬된 리스트
    raises:
         TypeError: 사용자가 integer가 아닌 다른 원소를 포함한 리스트를 입력한 경우
    """
    i = j = 0  # i, j는 각각 sorted_leftlist, sorted_rightlist에서 비교가 끝난 element 갯수
    sorted_list = []

    """ 3가지 케이스
        1. sorted_leftlist, sorted_rightlist 모두 중간의 element를 비교하는 경우
        2. sorted_rightlist는 비교가 끝난 경우
        3. sorted_leftlist는 비교가 끝난 경우
    """
    try:
        while i < len(sorted_leftlist) and j < len(sorted_rightlist):
            if sorted_leftlist[i] < sorted_rightlist[j]:
                sorted_list.append(sorted_leftlist[i])
                i = 1
            else:
                sorted_list.append(sorted_rightlist[j])
                j += 1

        while i < len(sorted_leftlist):
            sorted_list.append(sorted_leftlist[i])
            i += 1

        while j < len(sorted_rightlist):
            sorted_list.append(sorted_rightlist[j])
            j += 1
    except TypeError as e:
        print('{}'.format(e))
        raise TypeError('error: {}'.format(e))

    return sorted_list


def merge_sort(input_list):
    """ python implementation of merge_sort
    args:
        input_list: 정렬되지 않은 raw input list of integers
    returns:
        input_list의 모든 원소가 정렬이 된 상태의 리스트
    """
    n = len(input_list)

    if n < 2:
        return input_list

    mid = n // 2

    lefthalf = input_list[:mid]
    righthalf = input_list[mid:]

    sorted_leftlist = merge_sort(lefthalf)
    sorted_rightlist = merge_sort(righthalf)

    return merge(sorted_leftlist, sorted_rightlist)


class MergeSortTest(TestCase):

    def setUp(self):
        self.unordered_list = [5, 4, 2, 1, 3]
        self.unordered_list_without_str_and_int = [5, 2, 'A', 1, 4]

    def test_merge_sort_should_return_ordered_list(self):
        self.assertEqual([1, 2, 3, 4, 5], merge_sort(self.unordered_list))

    def test_should_raise_error_if_inputlist_contains_str_and_int(self):
        self.assertRaises(TypeError, merge_sort, self.unordered_list_without_str_and_int)

    def tearDown(self):
        del self.unordered_list


if __name__ == '__main__':
    main()
