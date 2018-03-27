# 561. Array Partition


def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s_list = sorted(nums)
    sum = 0
    for i in range(0, len(s_list), 2):
        sum += min(s_list[i], s_list[i+1])

    return sum


""" Better Code
    https://leetcode.com/problems/array-partition-i/discuss/102161/\
    Python-1-line-(sorting-is-accepted)

def arrayPairSum(self, nums):
    return sum(sorted(nums)[::2])
"""