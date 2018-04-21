"""
정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.

예제)
Input: [10, 5, 4, 3, -1]
Output: 5

Input: [3, 3, 3]
Output: Does not exist.
"""
import unittest


def print_second_largest_num(l):
    if len(l) < 2:
        return "Does not exist."
    first = second = 0

    for n in l:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n

    if not second:
        return "Does not exist."
    return second


class TestClass(unittest.TestCase):

    """Test case docstring."""

    def test_case1(self):
        list1 = [10, 5, 4, 3, -1]
        self.assertEqual(print_second_largest_num(list1), 5)

    def test_case2(self):
        list2 = [3, 3, 3]
        self.assertEqual(print_second_largest_num(list2), "Does not exist.")

    def test_case3(self):
        list2 = [10, 5, 6, 3, 7]
        self.assertEqual(print_second_largest_num(list2), 7)

if __name__ == "__main__":
    unittest.main()
