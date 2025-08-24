# Definition for singly-linked list.
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        while head:
            reversed = ListNode(head.val, reversed)
            head = head.next

        return reversed

class InPlaceSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

class TestCase(unittest.TestCase):
    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        self.assertEqual(expected, Solution().reverseList(head))
        self.assertEqual(expected, InPlaceSolution().reverseList(head))

    def test_example2(self):
        head = ListNode(1, ListNode(2))
        expected = ListNode(2, ListNode(1))
        self.assertEqual(expected, Solution().reverseList(head))
        self.assertEqual(expected, InPlaceSolution().reverseList(head))

    def test_example3(self):
        head = None
        expected = None
        self.assertEqual(expected, Solution().reverseList(head))
        self.assertEqual(expected, InPlaceSolution().reverseList(head))