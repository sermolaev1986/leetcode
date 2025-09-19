# Definition for singly-linked list.
import unittest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length = self.find_length(head)

        result = 0
        for i in range(length, 0, -1):
            factor = 2 ** (i -1)
            result += head.val * factor
            head = head.next

        return result

    def find_length(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

class TestCase(unittest.TestCase):
    def test_example1(self):
        head = ListNode(1)
        head.next = ListNode(0)
        head.next.next = ListNode(1)

        solution = Solution()
        self.assertEqual(solution.getDecimalValue(head), 5)