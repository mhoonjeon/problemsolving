# # 728. Self Dividing Numbers
import unittest


class Solution:
    @staticmethod
    def _check_if_self_divisible(num):
        new_num = num

        while new_num > 0:
            rightmost_digit = new_num % 10

            if rightmost_digit == 0 or num % rightmost_digit != 0:
                return False

            new_num = new_num // 10

        return True

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left, right+1):
            if self._check_if_self_divisible(i):
                ret.append(i)

        return ret


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.selfDividingNumbers(47, 85), [48, 55, 66, 77])


if __name__ == "__main__":
    unittest.main()


# 476. Number Complement
class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = count = 0
        while num > 0:
            q, r  = divmod(num, 2)
            if r == 1:
                r = 0
            else:
                r = 1
            sum += 2 ** count * r
            count += 1
            num = q

        return sum


class Test(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.findComplement(5), 2)
        self.assertEqual(s.findComplement(1), 0)

if __name__ == "__main__":
    unittest.main()

""" Better solution
https://leetcode.com/problems/number-complement/discuss/96009/Simple-Python

class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
"""
