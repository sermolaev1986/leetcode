# Definition for singly-linked list.
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self):
        values = []
        current = self
        max_nodes_to_show = 100
        nodes_seen = 0
        while current is not None and nodes_seen < max_nodes_to_show:
            values.append(str(current.val))
            current = current.next
            nodes_seen += 1
        suffix = "" if current is None else "..."
        return f"ListNode({ '->'.join(values) }{suffix})"

    __str__ = __repr__

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        previous = node
        while node and node.next:
            node.val = node.next.val
            previous = node
            node = node.next

        previous.next = None


class TestCase(unittest.TestCase):
    def test_example1(self):
        head = ListNode(4)
        head.next = ListNode(5)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(9)
        node_to_delete = head.next  # Node with value 5
        Solution().deleteNode(node_to_delete)
        expected = ListNode(4)
        expected.next = ListNode(1)
        expected.next.next = ListNode(9)
        self.assertEqual(expected, head)

    def test_example2(self):
        head = ListNode(4)
        head.next = ListNode(5)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(9)
        node_to_delete = head  # Node with value 4
        Solution().deleteNode(node_to_delete)
        expected = ListNode(5)
        expected.next = ListNode(1)
        expected.next.next = ListNode(9)

        self.assertEqual(expected, head)