# Definition for singly-linked list.
import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        original_head = head
        reversed = None
        while head:
            reversed = ListNode(head.val, reversed)
            head = head.next

        while original_head and reversed:
            if original_head.val != reversed.val:
                return False
            original_head = original_head.next
            reversed = reversed.next

        return True

class InPlaceSolution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_half_reversed = self.reverseList(slow)
        first_half = head

        while first_half and second_half_reversed:
            if first_half.val != second_half_reversed.val:
                return False
            first_half = first_half.next
            second_half_reversed = second_half_reversed.next

        return True

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
        head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        self.assertTrue(Solution().isPalindrome(head))
        self.assertTrue(InPlaceSolution().isPalindrome(head))

    def test_example2(self):
        head = ListNode(1, ListNode(2))
        self.assertFalse(Solution().isPalindrome(head))
        self.assertFalse(InPlaceSolution().isPalindrome(head))

    def test_example3(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
        self.assertTrue(Solution().isPalindrome(head))
        self.assertTrue(InPlaceSolution().isPalindrome(head))

    def test_example4(self):
        head = ListNode(1)
        self.assertTrue(Solution().isPalindrome(head))
        self.assertTrue(InPlaceSolution().isPalindrome(head))

    def test_example5(self):
        head = None
        self.assertTrue(Solution().isPalindrome(head))
        self.assertTrue(InPlaceSolution().isPalindrome(head))