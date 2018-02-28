# -*- coding: utf-8 -*-

# python implementation of quicksort using Divide and Conquer

import random
from unittest import TestCase, main


def quick_sort(input_list):
    """
    args:
        input_list: 정렬되지 않은 int를 원소로 갖는 리스트
    returns:
        input_list의 원소를 오름차순으로 정렬한 리스트
    """
    # base case for D&C: 리스트의 크기가 0 or 1이면 이미 정렬된 상태
    if len(input_list) < 2:
        return input_list

    pivot = input_list[0]  # use first element as pivot
    left_list = []  # pivot보다 작은 element의 리스트
    right_list = []  # pivot보다 큰 element의 리스트

    for element in input_list[1:]:
        if element < pivot:
            left_list.append(element)
        else:
            right_list.append(element)

    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


def swap(input_list, a, b):
    """ 자주 쓰는 swap 기능을 모듈화
    args:
        input_list: self-explanatory
        a, b: 리스트(input_list)내의 인덱스
    returns:
        리스트(input_list)에서 인덱스 a, b에 위치한 값을 바꿔준다.
    """
    input_list[a], input_list[b] = input_list[b], input_list[a]


def pick_random_pivot(start, end):
    """ 랜덤하게 pivot을 구한다.
    Randomized pivot selection heuristically proven to prevent worst case
    O(n**2) time (already sorted list)
    """
    pivot_index = random.randint(start, end)
    return pivot_index


def partition(input_list, start, end):
    """ Helper function for randomized_inplace_quick_sort
    Randomly picks pivot index, move the pivot to the last index within list and
    narrows down

    args:
        input_list: self-explanatory
        start: 리스트의 첫번째 원소의 인덱스
        end: 리스트의 마지막 원소의 인덱스
    returns:
        리스트를 랜덤하게 추출된 pivot을 중심으로, 왼쪽에 작은 수 리스트,
        오른쪽에 큰 수 리스트로 정렬한 후, 중간의 pivot 값의 인덱스를 리턴
    """
    pivot_index = pick_random_pivot(start, end)
    swap(input_list, pivot_index, end)  # pivot을 마지막 원소와 위치를 바꾼다.

    pivot = input_list[end]
    low = start
    high = end - 1

    while low <= high:
        while low <= high and input_list[low] <= pivot:
            low += 1
        while low <= high and input_list[high] > pivot:
            high -= 1
        if low <= high:
            swap(input_list, low, high)
            low, high = low + 1, high - 1

    swap(input_list, low, end)

    return low


def randomized_inplace_quick_sort(input_list, start, end):
    """ Optimazation of quicksort: randomized & inplace quicksort
    Reasons: in-place algorithm uses less memory in addtion to that needed for
             original input. Recurisve function quick_sort() requires additional
             container lists.
    Args:
        input_list: python list of integers
        start: starting index of search range
        end: last index of search range
    Returns:
        ordered input_list
    """

    # sublist가 한개 일 때까지 반복한다.
    if end > start:

        # partition 헬퍼 함수를 통해 pivot 기준으로 sorting하고
        # pivot의 인덱스를 리턴한다.
        pivot_index = partition(input_list, start, end)

        # pivot의 인덱스를 기준으로 좌우로 sublist를 나눠 재귀적으로
        # sorting한다.
        randomized_inplace_quick_sort(input_list, start, pivot_index - 1)
        randomized_inplace_quick_sort(input_list, pivot_index + 1, end)

    return input_list


class QuickSortTest(TestCase):

    def setUp(self):
        self.unordered_list = [5, 4, 2, 1, 3]

    def test_quick_sort_should_return_ordered_list(self):
        self.assertEqual([1, 2, 3, 4, 5], quick_sort(self.unordered_list))

    def test_randomized_inplace_quick_sort_should_return_ordered_list(self):
        self.assertEqual([1, 2, 3, 4, 5],
                         randomized_inplace_quick_sort(
                             self.unordered_list,
                             0,
                             len(self.unordered_list) - 1)
                         )

    def tearDown(self):
        del self.unordered_list


if __name__ == '__main__':
    main()
