# Definition for singly-linked list.
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

import unittest


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if slow.next:
            slow.next = slow.next.next
        return dummy.next


class TestCase(unittest.TestCase):
    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        n = 2
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        self.assertEqual(expected, Solution().removeNthFromEnd(head, n))

    def test_example2(self):
        head = ListNode(1)
        n = 1
        expected = None
        self.assertEqual(expected, Solution().removeNthFromEnd(head, n))

    def test_example3(self):
        head = ListNode(1, ListNode(2))
        n = 1
        expected = ListNode(1)
        self.assertEqual(expected, Solution().removeNthFromEnd(head, n))