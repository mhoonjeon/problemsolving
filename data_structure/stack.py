from unittest import main, TestCase


class Node:

    def __init__(self, data, next):
        self._data = data
        self._next = next

    def __repr__(self):
        return "{} -> {}".format(self._data, self._next)


class Stack:
    """ Stack 구현
    Interfaces:
        push: add to stack as last node
        pop: delete last node from stack and return the node
        peek: get last node from stack without deleting
        is_empty: check if stack is empty(boolean)
    """
    def __init__(self):
        self._head = Node(None, None)
        self._tail = self._head
        self._n = 0

    def push(self, data):
        new_node = Node(data, None)
        self._tail._next = new_node
        self._tail = new_node
        self._n += 1

    def pop(self):
        if self._head == self._tail:
            raise IndexError
        cur = self._head
        while cur._next._next is not None:
            cur = cur._next
        last = cur._next
        cur._next = None
        self._tail = cur
        self._n -= 1
        return last

    def peek(self):
        return self._tail._data

    def is_empty(self):
        return (self._n == 0)


class StackTest(TestCase):
    """Test case docstring."""

    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        del self.stack

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        assert self.stack._n == 4
        assert repr(self.stack._head) == "None -> 1 -> 2 -> 3 -> 4 -> None"

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.pop()
        assert self.stack._n == 3
        assert repr(self.stack._head) == "None -> 1 -> 2 -> 3 -> None"
        self.stack.pop()
        assert self.stack._n == 2
        assert repr(self.stack._head) == "None -> 1 -> 2 -> None"
        self.stack.pop()
        self.stack.pop()

    def test_pop_from_empty_stack_should_return_index_error(self):
        self.assertRaises(IndexError, self.stack.pop)

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.assertEqual(self.stack.peek(), 4)


if __name__ == "__main__":
    main()
