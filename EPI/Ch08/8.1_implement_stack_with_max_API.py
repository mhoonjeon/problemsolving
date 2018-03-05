# -*- coding: utf-8 -*-

__author__ = "MH Jeon"

import os
from unittest import main, TestCase
import sys

""" Solution for EPI 8.1: Implement stack with max API """

# To reuse code in data_structure directory, import sys.path from runtime
# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder/4383597
sys.path.append(os.environ.get('ROOT_PATH')+'/data_structure')
from stack import Stack


class StackWithMaxAPI(Stack):

    def __init__(self):
        super().__init__()
        self._max = 0

    def push(self, data):
        super().push(data)

        self._max = self._check_max(data)

    def pop(self):
        popped_node = super().pop()

        cur = self._head._next
        self._max = 0
        while cur:
            self._max = self._check_max(cur._data)
            cur = cur._next

        return popped_node

    def _check_max(self, data):
        if data > self._max:
            return data
        return self._max


class StackTest(TestCase):
    """Test case docstring."""
    def setUp(self):
        self.stack = StackWithMaxAPI()

    def tearDown(self):
        del self.stack

    def test_max_with_push_and_pop(self):
        self.stack.push(1)
        self.stack.push(4)
        self.stack.push(3)
        self.stack.push(5)
        assert self.stack._n == 4
        assert repr(self.stack._head) == "None -> 1 -> 4 -> 3 -> 5 -> None"
        self.assertEqual(self.stack._max, 5)

        self.stack.pop()
        self.assertEqual(self.stack._max, 4)
        self.stack.pop()
        self.assertEqual(self.stack._max, 4)


if __name__ == "__main__":
    main()
