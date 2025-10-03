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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0:
            return head

        length = 0
        original_last = None
        temp_head = head
        while temp_head:
            original_last = temp_head
            length += 1
            temp_head = temp_head.next

        shift = length - k % length

        new_head = head
        if shift != length:
            new_last = head
            for i in range(1, shift):
                new_last = new_last.next
            new_head = new_last.next

            new_last.next = None
            original_last.next = head

        return new_head


class TestCase(unittest.TestCase):
    def test1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        solution = Solution()
        actual = solution.rotateRight(head, 2)

        expected = ListNode(4)
        expected.next = ListNode(5)
        expected.next.next = ListNode(1)
        expected.next.next.next = ListNode(2)
        expected.next.next.next.next = ListNode(3)

        self.assertEqual(expected, actual)

    def test2(self):
        head = ListNode(0)
        head.next = ListNode(1)
        head.next.next = ListNode(2)

        solution = Solution()
        actual = solution.rotateRight(head, 4)

        expected = ListNode(2)
        expected.next = ListNode(0)
        expected.next.next = ListNode(1)

        self.assertEqual(expected, actual)

    def test3(self):
        head = ListNode(1)

        solution = Solution()
        actual = solution.rotateRight(head, 1)

        self.assertEqual(head, actual)

    def test4(self):
        solution = Solution()
        actual = solution.rotateRight(None, 1)

        self.assertEqual(None, actual)

    def test5(self):
        head = ListNode(1)

        solution = Solution()
        actual = solution.rotateRight(head, 0)

        self.assertEqual(head, actual)