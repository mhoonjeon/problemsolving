import unittest


if __name__ == "__main__":
    num = int(input())
    sum = 0
    for i in range(1, num):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    print(sum)


class TestClass(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name(self):
        pass
