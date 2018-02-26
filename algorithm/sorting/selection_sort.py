# -*- coding: utf-8 -*-

__author__ = 'Myong-Hoon Jeon'

from unittest import TestCase, main


def selection_sort(input_list):
    """ 선택정렬 구현

    args:
        input_list: int를 원소로 가지는 리스트

    returns:
        원소들이 오름차순으로 정렬된 리스트

    raises:

    """

    try:
        for i, value in enumerate(input_list):
            local_min_index, local_min = i, value
            k = i + 1

            while k < len(input_list):
                if input_list[k] < local_min:
                    local_min_index, local_min = k, input_list[k]
                k = k + 1

            if input_list[i] != local_min:
                input_list[i], input_list[local_min_index] = input_list[local_min_index], input_list[i]

        return input_list

    except TypeError as e:
        raise Exception("리스트 원소의 타입은 동일해야 제대로 된 비교가 가능합니다.\
              에러메세지는 다음과 같습니다: {}".format(e))


class SelectionSortTest(TestCase):

    def setUp(self):
        self.unordered_list_without_order = [5, 2, 3, 1, 4]
        self.unordered_list_without_str_and_int = [5, 2, 'A', 1, 4]

    def test_selection_sort_should_return_ordered_list(self):
        self.assertEqual([1, 2, 3, 4, 5],
                         selection_sort(self.unordered_list_without_order))

    def test_should_raise_error_if_inputlist_contains_str_and_int(self):
        self.assertRaises(Exception,
                          lambda: selection_sort(
                              self.unordered_list_without_str_and_int)
                          )


if __name__ == "__main__":
    main()
