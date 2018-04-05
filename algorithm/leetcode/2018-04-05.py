# 411. Fizz Buzz
def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    ret = []
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            ret.append("FizzBuzz")
        elif i % 3 == 0:
            ret.append("Fizz")
        elif i % 5 == 0:
            ret.append("Buzz")
        else:
            ret.append(str(i))
    return ret


"""
def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i)
            for i
            in range(1, n+1)]
"""


# 575. Distribute Candies
def distributeCandies(self, candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    kind_of_candies = set(candies)
    if len(kind_of_candies) > len(candies) // 2:
        return len(candies) // 2

    return len(kind_of_candies)


"""
여동생, 남동생을 차례대로 한번씩 번갈아가며 배분해야하는 줄 알았으나, 상관없다.
그냥 여동생은 먼저 본인이 최대한 다양한 캔디를 먹을 수 있도록 뽑으면 되므로,
남동생은 고려할 필요가 없다.
"""


# 682. Baseball Game
def calPoints(self, ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    sum = 0
    ints = []

    for op in ops:
        if op == "C":
            sum -= ints[-1]
            ints.pop()

        elif op == "D":
            cur = ints[-1] * 2
            sum += cur
            ints.append(cur)

        elif op == "+":
            cur = ints[-1] + ints[-2]
            sum += cur
            ints.append(cur)

        else:
            cur = int(op)
            sum += int(op)
            ints.append(int(op))

    return sum


"""
https://leetcode.com/problems/baseball-game/discuss/107871/Straightforward-Python

def calPoints(self, ops):
    # Time: O(n)
    # Space: O(n)
    history = []
    for op in ops:
        if op == 'C':
            history.pop()
        elif op == 'D':
            history.append(history[-1] * 2)
        elif op == '+':
            history.append(history[-1] + history[-2])
        else:
            history.append(int(op))
    return sum(history)
"""
