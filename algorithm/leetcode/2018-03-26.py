# 461. Hamming distance


class Solution:

    @classmethod
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        while x or y:
            if x % 2 != y % 2:
                count += 1
            x //= 2
            y //= 2
        return count


if __name__ == "__main__":
    x, y = [int(x) for x in input().split()]
    print(Solution.hammingDistance(x, y))

""" Fastest python code

https://leetcode.com/problems/hamming-distance/discuss/94789/Beats-100-Python

class Solution(object):
    def hammingDistance(self, x, y):
        ""
        :type x: int
        :type y: int
        :rtype: int
        ""
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y
"""

# 657. Judge Route Circle, 84.25%
# https://leetcode.com/problems/judge-route-circle/description/


def judgeCircle(moves):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count = {
            "R": 0, "L": 0,
            "U": 0, "D": 0
        }

        for ch in moves:
            count[ch] += 1

        if count['U'] == count["D"] and count['R'] == count["L"]:
            return True
        return False


""" Official Solution

https://leetcode.com/problems/judge-route-circle/solution/

def judgeCircle(self, moves):
    x = y = 0
    for move in moves:
        if move == 'U': y -= 1
        elif move == 'D': y += 1
        elif move == 'L': x -= 1
        elif move == 'R': x += 1

    return x == y == 0
"""
