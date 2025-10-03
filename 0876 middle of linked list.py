import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        size = 0
        while head:
            size += 1
            if size % 2 == 0:
                middle = middle.next

            head = head.next

        return middle

class TestCase(unittest.TestCase):
    def test_example1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(3, ListNode(4, ListNode(5)))
        self.assertEqual(expected.val, Solution().middleNode(head).val)

    def test_example2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        expected = ListNode(4, ListNode(5, ListNode(6)))
        self.assertEqual(expected.val, Solution().middleNode(head).val)


