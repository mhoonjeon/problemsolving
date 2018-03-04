# -*- coding: utf-8 -*-

__author__ = "Myong-Hoon Jeon"

from unittest import main, TestCase


class Node:
    """ 연결리스트의 Node. """

    def __init__(self, data, prev, next):
        self._data = data
        self._prev = prev  # point to previous node
        self._next = next

    def __repr__(self):
        return "{} -> {}".format(self._data, self._next)


class DoublyLinkedList(object):

    def __init__(self):
        """
        Create sentinel dummy node for both ends
        """
        self._head = Node(None, None, None)
        self._tail = Node(None, None, None)
        self._tail.prev = self._head
        self._head.next = self._tail

        self._size = 0

    def __len__(self):
        return self._size

    def insert_between(self, new_data, before=None, after=None):
        """
        args
            before: integer
            after: integer
        """
        before = self._search(before) if before else self._head
        after = self._search(after) if after else self._tail

        if before is False or after is False:
            raise Exception('기존 리스트에 숫자가 없습니다.')

        if before or after:
            new_node = Node(new_data, before, after)
            after._prev = new_node
            before._next = new_node
        else:
            new_node = Node(new_data, self._head, self._tail)
            self._head._next = new_node
            self._tail._prev = new_node

        self._size += 1

    def delete(self, data):
        cur = self._head
        while cur._next._data != data:  # cur = 삭제할 데이터 앞의 노드
            cur = cur._next

        after = cur._next._next
        del cur._next
        cur._next = after
        after._prev = cur
        self._size -= 1

    def _search(self, data):
        """ 리스트에 데이터가 있는지 확인한다.
        args:
            data: 확인할 데이터
        returns:
            None: data가 없는 경우
            cur: data가 리스트에 있는 경우
        """
        if not data:
            return None
        cur = self._head._next
        while cur._data is not None:
            if cur._data == data:
                return cur
            cur = cur._next
        return None

    def _traverse(self):
        """ 모든 데이터를 포함한 리스트를 반환한다. """
        cur = self._head._next
        full_list = []
        while cur._next is not None:
            full_list.append(cur._data)
            cur = cur._next
        return full_list


class LinkedListTest(TestCase):

    def setUp(self):
        self.ll = DoublyLinkedList()

    def test_insert_between(self):
        self.ll.insert_between(new_data=2, before=None, after=None)
        self.assertEqual(self.ll._traverse(), [2])
        self.ll.insert_between(new_data=3, before=2, after=None)
        self.assertEqual(self.ll._traverse(), [2, 3])
        self.ll.insert_between(new_data=1, before=None, after=2)
        self.assertEqual(self.ll._traverse(), [1, 2, 3])
        self.ll.insert_between(new_data=5, before=3, after=None)
        self.assertEqual(self.ll._traverse(), [1, 2, 3, 5])
        self.ll.insert_between(new_data=4, before=3, after=5)
        self.assertEqual(self.ll._traverse(), [1, 2, 3, 4, 5])
        self.assertEqual(len(self.ll), 5)

        self.assertRaises(Exception, self.ll._traverse, (4, 7, 5))

    def test_delete(self):
        self.ll.insert_between(new_data=2, before=None, after=None)
        self.ll.insert_between(new_data=3, before=2, after=None)
        self.ll.insert_between(new_data=1, before=None, after=2)
        self.ll.insert_between(new_data=5, before=3, after=None)
        self.ll.insert_between(new_data=4, before=3, after=5)
        self.assertEqual(self.ll._traverse(), [1, 2, 3, 4, 5])

        self.ll.delete(5)
        self.assertEqual(self.ll._traverse(), [1, 2, 3, 4])
        self.ll.delete(2)
        self.assertEqual(self.ll._traverse(), [1, 3, 4])
        self.ll.delete(1)
        self.assertEqual(self.ll._traverse(), [3, 4])
        self.assertEqual(len(self.ll), 2)

    def tearDown(self):
        del self.ll


if __name__ == "__main__":
    main()
