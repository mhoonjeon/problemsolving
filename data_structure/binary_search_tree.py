# -*- coding: utf-8 -*-

from unittest import TestCase, main

__author__ = 'MH Jeon'


class Node:

    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def _num_children(self):
        count = 0
        if self._left:
            count += 1
        if self._right:
            count += 1
        return count

    def _is_leaf(self):
        return (self._num_children() == 0)


class BinaryTree:

    def __init__(self):
        self._root = Node(None)

    def add(self, data):
        if self._root._data is None:
            self._root = Node(data)
        else:
            self._add_node(self._root, data)

    def _add_node(self, cur, data):
        if data <= cur._data:
            if cur._left is None:
                cur._left = Node(data)
            else:
                self._add_node(cur._left, data)
        else:
            if cur._right is None:
                cur._right = Node(data)
            else:
                self._add_node(cur._right, data)

    def search(self, data):
        if self._root is None:
            return False
        else:
            return self._search(self._root, data)

    def _search(self, cur, data):
        if data == cur._data:
            return cur
        else:
            if data < cur._data:
                if cur._left:
                    return self._search(cur._left, data)
                else:
                    return False
            elif data > cur._data:
                if cur._right:
                    return self._search(cur._right, data)
                else:
                    return False

    def delete(self, data):
        """ 노드를 삭제하기
        케이스:
            1. 삭제하려는 노드가 자식노드가 없는 경우
            2. 삭제하려는 노드가 자식노드가 1개인 경우
            3. 삭제하려는 노드가 자식노드가 2개인 경우
                -오른쪽의 subtree에서 가장 왼쪽의 노드와 바꾼후 삭제

        returns:
            False: 빈 트리인 경우나 삭제하려는 데이터가 없는 경우
        """
        if self._root is None:
            return False
        else:
            delete_node = self._search(self._root, data)
            self._delete_node(delete_node)

    def _delete_node(self, node):
        if node._is_leaf():
            node = None
        elif node._num_children() == 1:
            if node._left:
                node = node._left
            else:
                node = node._right
        else:
            min_node_from_right_subtree = self._find_min_node_from_right_subtree(node)
            node._data, min_node_from_right_subtree._data = min_node_from_right_subtree._data, node._data
            self._delete_min_node_from_right_subtree(node, node._right, min_node_from_right_subtree._data)

    def _delete_min_node_from_right_subtree(self, parent, cur, data):
        """ 삭제하려는 노드의 자식이 2개인 경우 필요

        오른쪽 subtree의 최소값을 가진 노드와 바꿔줘야 한다.
        """

        if cur._data == data:
            if parent._left == cur:
                parent._left = None
            else:
                parent._right = None
        else:
            if cur._data > data:
                self._delete_min_node_from_right_subtree(cur, cur._left, data)
            else:
                self._delete_min_node_from_right_subtree(cur, cur._right, data)

    def _find_min_node_from_right_subtree(self, node):
        if node._is_leaf():
            return node
        elif node._right:
            node = node._right
            return self._find_min_node_from_right_subtree(node)
        else:
            node = node._left
            return self._find_min_node_from_right_subtree(node)


class TestClass(TestCase):

    """Test case docstring."""

    def setUp(self):
        self.bt = BinaryTree()

    def tearDown(self):
        del self.bt

    def test_add(self):
        self.bt.add(1)
        self.assertEqual(self.bt._root._data, 1)
        self.bt.add(4)
        self.assertEqual(self.bt._root._right._data, 4)
        self.bt.add(5)
        self.assertEqual(self.bt._root._right._right._data, 5)
        self.bt.add(3)
        self.assertEqual(self.bt._root._right._left._data, 3)

    def test_search(self):
        """
            1
                50
            40      70
          20  24   60
        """
        self.bt.add(1)
        self.bt.add(5)
        self.bt.add(4)
        self.bt.add(7)
        self.bt.add(2)
        self.assertEqual(self.bt.search(2)._data, 2)
        self.assertFalse(self.bt.search(10))

    def test_delete(self):
        """
            1
                50
            40      70
          20  24   60
        """
        self.bt.add(1)
        self.bt.add(50)
        self.bt.add(40)
        self.bt.add(70)
        self.bt.add(20)
        self.bt.add(24)
        self.bt.add(60)
        self.bt.delete(70)
        self.assertTrue(self.bt.search(60)._is_leaf())
        self.bt.delete(24)
        self.assertEqual(self.bt.search(40)._num_children(), 1)
        self.bt.delete(50)
        self.assertEqual(self.bt._root._right._data, 60)
        self.assertIsNone(self.bt._root._right._right._left)


if __name__ == "__main__":
    main()
