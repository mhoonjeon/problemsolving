from unittest import main, TestCase


class Node:
    """ 연결리스트의 Node. """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    """ Python implementation of linked list with dummy_head.

    Dummy head를 사용하면, 매번 리스트가 빈 리스트인지 확인할 필요가 없어서
    코드량이 줄어든다.

    Availabe APIs:
        Public:
            insert
            delete
            is_in_list
        Private:
            _append
            _traverse

    Common variable names used in methods:
        cur: current node
        head: first node in linked list
        tail: last node in linke list
    """

    def __init__(self):
        dummy_head = Node(None)
        self.head = dummy_head
        self.tail = dummy_head

    def insert(self, new_data, after=None):
        """ Implement insert_after specific node function
        Insert new_data after specific node, or if 'after' is not
        given append at the end
        """
        if not after or self.tail.data == after:
            self._append(new_data)

        else:
            node = Node(data=new_data)
            cur = self.head
            while cur.data is not after:  # break when cur is after
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def _append(self, new_data):
        """ Append new_data at the end of list """
        node = Node(new_data)
        self.tail.next = node
        node.next = None
        self.tail = node

    def delete(self, data):
        cur = self.head
        while cur.next.data != data:  # cur = 삭제할 데이터 앞의 노드
            cur = cur.next
        temp = cur.next
        cur.next = cur.next.next
        del temp

    def is_in_list(self, data):
        """ 리스트에 데이터가 있는지 확인한다.
        args:
            data: 확인할 데이터
        returns:
            True: 데이터가 있는 경우
            False: 데이터가 없는 경우
        """
        cur = self.head
        while cur.data != self.tail.data:
            if cur.next.data == data:
                return True
            cur = cur.next
        return False

    def _traverse(self):
        """ 모든 데이터를 포함한 리스트를 반환한다. """
        cur = self.head.next
        full_list = []
        while cur is not None:
            full_list.append(cur.data)
            cur = cur.next
        return full_list


class LinkedListTest(TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_insert(self):
        self.ll.insert(1)
        self.assertEqual(self.ll._traverse(), [1])
        self.ll.insert(new_data=2, after=1)
        self.assertEqual(self.ll._traverse(), [1, 2])
        self.ll.insert(new_data=3, after=2)
        self.assertEqual(self.ll._traverse(), [1, 2, 3])

        self.ll.insert(new_data=4, after=2)
        self.assertEqual(self.ll._traverse(), [1, 2, 4, 3])
        self.ll.insert(new_data=5, after=1)
        self.assertEqual(self.ll._traverse(), [1, 5, 2, 4, 3])

        self.ll.insert(new_data=6)
        self.assertEqual(self.ll._traverse(), [1, 5, 2, 4, 3, 6])

    def test_delete(self):
        self.ll.insert(1)
        self.ll.insert(new_data=2, after=1)
        self.ll.insert(new_data=3, after=2)
        self.ll.insert(new_data=4, after=3)
        self.ll.insert(new_data=5, after=4)
        self.assertEqual(self.ll._traverse(), [1, 2, 3, 4, 5])

        self.ll.delete(5)
        self.assertEqual(self.ll._traverse(), [1, 2, 3, 4])
        self.ll.delete(2)
        self.assertEqual(self.ll._traverse(), [1, 3, 4])
        self.ll.delete(1)
        self.assertEqual(self.ll._traverse(), [3, 4])

    def test_is_in_list(self):
        self.ll.insert(1)
        self.ll.insert(new_data=2, after=1)
        self.ll.insert(new_data=3, after=2)
        self.ll.insert(new_data=4, after=3)
        self.ll.insert(new_data=5, after=4)
        self.assertEqual(self.ll._traverse(), [1, 2, 3, 4, 5])

        self.assertTrue(self.ll.is_in_list(5))
        self.assertTrue(self.ll.is_in_list(3))
        self.assertTrue(self.ll.is_in_list(1))
        self.assertFalse(self.ll.is_in_list(6))

    def tearDown(self):
        del self.ll


if __name__ == "__main__":
    main()
