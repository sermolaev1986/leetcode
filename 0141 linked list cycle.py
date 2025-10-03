# Definition for singly-linked list.
import unittest
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False


class TwoPointersSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False


class TestCase(unittest.TestCase):
    def test_example1(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next  # Create a cycle here
        self.assertTrue(Solution().hasCycle(head))
        self.assertTrue(TwoPointersSolution().hasCycle(head))


    def test_example2(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = head  # Create a cycle here
        self.assertTrue(Solution().hasCycle(head))
        self.assertTrue(TwoPointersSolution().hasCycle(head))

    def test_example3(self):
        head = ListNode(1)
        head.next = ListNode(2)
        self.assertFalse(Solution().hasCycle(head))
        self.assertFalse(TwoPointersSolution().hasCycle(head))


    def test_example4(self):
        head = ListNode(1)
        self.assertFalse(Solution().hasCycle(head))
        self.assertFalse(TwoPointersSolution().hasCycle(head))
