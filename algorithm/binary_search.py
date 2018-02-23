# -*- coding: utf-8 -*-

from math import floor
from unittest import TestCase, main

__author__ = "MH Jeon"


def binary_search(data, target, low, high):
    """ Binary search 구현

    Args:
        data (python list): 파이썬 리스트
        target (int): 찾고자 하는 값
        low (int): data의 첫 인덱스
        high (int): data의 마지막 인덱스
        mid (int): data의 중간 인덱스

    Returns:
        None: target이 data에 없을 때
        (int): target이 data에 있을 때, target값의 인덱스

    Raises:
        TypeError: target이 string으로 주어졌을 때
    """
    data.sort()  # binary_search를 위해서는 input 리스트가 항상 정렬되어 있어야 한다.

    try:
        if low > high:
            return None

        mid = (low + high) // 2

        if target == data[mid]:  # target을 찾았을 때
            return mid

        elif target > data[mid]:
            return binary_search(data, target, mid+1, high)

        else:
            return binary_search(data, target, low, mid-1)

    except TypeError as e:
        return print("입력값은 int 형태여야 합니다. {}".format(e))


class BinarySearchTest(TestCase):
    """ binary_search()를 테스트하기 위한 클래스

    Cases:
        1. target이 data에 없는 경우: return None
        2. target이 int가 아닌 str이 주어진 경우: return TypeError
        3. target이 data에 없는 경우: return Index of target
    """
    def setUp(self):
        self.list = [1,2,3,4,5]

    def test_search_should_return_none_if_target_not_in_list(self):
        targets = [
            -3,
            0,
            6
        ]

        for target in targets:
            self.assertIsNone(binary_search(self.list, target, 0, 4))

    def test_search_should_raise_error_if_string_is_given_as_input(self):
        targets = [
            "넷"
        ]

        for target in targets:
            self.assertRaises(TypeError, binary_search, (self.list, target, 0, 4))

    def test_search_should_return_target_index_if_targe_is_in_list(self):
        targets = [
            1,
            2,
            5
        ]

        for target in targets:
            self.assertEqual(binary_search(self.list, target, 0, 4), self.list.index(target))

    def test_search_should_be_possible_with_unordered_input_list(self):
        unordered_list = [4, 3, 2, 1, 5]
        targets = [
            1,
            2,
            5
        ]

        for target in targets:
            self.assertEqual(binary_search(unordered_list, target, 0, 4), self.list.index(target))

    def tearDown(self):
        pass


if __name__ == "__main__":
    main()
