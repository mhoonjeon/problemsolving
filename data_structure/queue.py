from unittest import main, TestCase


class Node:

    def __init__(self, data, next):
        self._data = data
        self._next = next

    def __repr__(self):
        return "{} -> {}".format(self._data, self._next)


class Queue:
    """ Queue 구현(First in, First out)
    Interfaces:
        enque: add to tail of queue
        dequeue: delete first node from queue and return the node
        peek: get last node from stack without deleting
        is_empty: check if stack is empty(boolean)
    """
    def __init__(self):
        self._head = Node(None, None)
        self._tail = self._head
        self._n = 0

    def enqueue(self, data):
        """ add to tail """
        new_node = Node(data, None)
        if self._is_empty():
            self._head._next = new_node
            self._head = new_node
            self._tail = new_node
            self._n += 1
            return
        self._tail._next = new_node
        self._tail = new_node
        self._n += 1

    def dequeue(self):
        if self._is_empty():
            raise IndexError('queue is empty')
        new_head = self._head._next
        ret_data = self._head._data
        del self._head
        self._head = new_head
        self._n -= 1
        return ret_data

    def _is_empty(self):
        return (self._n == 0)


class QueueTest(TestCase):
    """Test case docstring."""

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        assert self.queue._n == 4
        assert repr(self.queue._head) == "1 -> 2 -> 3 -> 4 -> None"

    def test_deque(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)

        self.queue.dequeue()
        assert self.queue._n == 3
        assert repr(self.queue._head) == "2 -> 3 -> 4 -> None"

    def tearDown(self):
        del self.queue


if __name__ == "__main__":
    main()
