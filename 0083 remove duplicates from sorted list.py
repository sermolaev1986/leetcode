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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original_head = head
        previous = None
        while head:
            if previous and head.val == previous.val:
                previous.next = head.next
            else:
                previous = head
            head = head.next
        return original_head

class TestCase(unittest.TestCase):
    def test_example1(self):
        head = ListNode(1, ListNode(1, ListNode(2)))
        expected = ListNode(1, ListNode(2))
        self.assertEqual(expected, Solution().deleteDuplicates(head))

    def test_example2(self):
        head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        expected = ListNode(1, ListNode(2, ListNode(3)))
        self.assertEqual(expected, Solution().deleteDuplicates(head))
