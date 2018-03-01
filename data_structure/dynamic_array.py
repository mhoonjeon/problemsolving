# -*- coding: utf-8 -*-

""" Python implementation of dynamic arrays

Available class:
- DynamicArray: 배열 내 빈 공간의 유무에 상관없이 마지막 인덱스에 데이터를
                추가할 수 있는 메소드를 가지는 클래스

TODO:
- delete() 구현
"""

import ctypes
from unittest import main, TestCase

__author__ = 'Myong-Hoon Jeon'


class DynamicArray(object):
    """ Dynamic Array 구현

    Dynamic Array란 정해진 크기의 배열이 꽉 찬 경우에도 데이터를 추가할 수 있는
    배열을 의미한다. 이 경우, 더 큰 크기의 새 배열이 만들어지고, 이후 데이터가
    복사된다.

    Public methods:
    - append(data): data를 배열의 마지막 인덱스에 추가한다.
    """
    def __init__(self):
        """빈 배열을 생성"""
        self._n = 0                 # 배열내의 데이터 갯수
        self._capacity = 1          # 배열의 크기
        self._array = self._make_array(self._capacity)  # 배열생성(low-level)

    def __len__(self):
        """배열 내 갯수 리턴"""
        return self._n

    def __getitem__(self, i):
        """인덱스 i를 통한 배열의 접근
        args:
        - i: integer i

        raises:
        - i가 배열보다 큰 경우: IndexError
        - i가 배열보다 작지만, 해당 인덱스에 데이터가 없는 경우: IndexError

        returns:
        - i번째 인덱스에 있는 데이터
        """
        if self._capacity < i:
            raise IndexError('배열의 크기보다 큰 인덱스입니다.')
        elif self._n < i:
            raise IndexError('배열내 해당 인덱스에 데이터가 없습니다.')
        return self._array[i]

    def append(self, data):
        """ array크기에 *상관없이* 배열의 마지막에 데이터 삽입

        배열이 꽉 차있는 경우, 현재 배열의 두배 크기의 배열을 만들고, 기존 배열의
        데이터를 복사한 후, 클래스내의 배열을 새로운 배열을 참조하게 만든다.
        """
        if self._n == self._capacity:
            self._resize(self._capacity * 2)
        self._array[self._n] = data
        self._n += 1

    def _resize(self, c):
        """ 배열이 꽉 찬 경우, 데이터 추가를 위해 더 큰 크기의 배열을 생성
        """
        new_array = self._make_array(c * 2)         # 더 큰 배열 생성
        for index, data in enumerate(self._array):  # 기존 배열의 데이터 복사
            new_array[index] = data
        self._array = new_array                     # 새로 생성된 배열을 참조
        self._capacity = c

    def _make_array(self, _capacity):
        """ c언어처럼 low-level의 배열 생성"""
        return (_capacity * ctypes.py_object)()


class DynamicArrayTest(TestCase):
    """ Dynamic Array 구현을 테스트

    DynamicArray() 구현한 append기능을 테스트하기 위한 클래스. 배열의 크기에
    상관없이 append가 가능해야 한다.

    Available methods for testing:
    - test_dynamic_array_should_be_able_to_append_if_array_is_not_full:
        빈 공간이 있을 때 데이터 삽입이 가능한지 테스트
    - test_dynamic_array_should_be_able_to_append_even_if_array_is_full
        빈 공간이 없을 때 데이터 삽입이 가능한지 테스트
    """

    def setUp(self):
        """빈 배열 생성"""
        self.empty_array = DynamicArray()

    def test_dynamic_array_should_be_able_to_append_if_array_is_not_full(self):
        """배열내 공간이 남는 경우 데이터 추가가 가능한지 확인"""
        self.empty_array.append(1)
        full_array = self.empty_array
        self.assertEqual(len(full_array), 1)
        self.assertEqual(full_array[0], 1)

    def test_dynamic_array_should_be_able_to_append_even_if_array_is_full(self):
        """배열이 꽉 차있어도 데이터 추가가 가능한지 확인"""
        self.empty_array.append(1)
        full_array = self.empty_array
        self.assertEqual(len(full_array), full_array._n)

        full_array.append(2)
        self.assertEqual(len(full_array), 2)
        self.assertEqual(full_array[1], 2)

    def tearDown(self):
        """setUp()에서 생성된 테스트용 배열을 삭제"""
        del self.empty_array


if __name__ == '__main__':
    main()
