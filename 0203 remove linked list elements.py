# Definition for singly-linked list.
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        original_head = head
        previous = None
        while head:
            if head.val == val:
                if previous:
                    previous.next = head.next
                else:
                    original_head = head.next
            else:
                previous = head
            head = head.next

        return original_head

class TestCase(unittest.TestCase):
    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(expected.val, Solution().removeElements(head, 6).val)

    # test case for [7,7,7,7]
    def test_example2(self):
        head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
        expected = None
        self.assertEqual(expected, Solution().removeElements(head, 7))
