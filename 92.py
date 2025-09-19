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
        return f"ListNode({'->'.join(values)}{suffix})"

    __str__ = __repr__

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp_head = head
        before = head
        previous = None
        reversed_head = None
        reversed_tail = None
        position = 0
        while temp_head:
            position += 1
            if position == left:
                before = previous
                reversed_head = reversed_tail = ListNode(temp_head.val)
            elif left < position < right:
                reversed_head = ListNode(temp_head.val, reversed_head)
            elif position == right:
                reversed_head = ListNode(temp_head.val, reversed_head)
                if before:
                    before.next = reversed_head
                else:
                    head = reversed_head
            elif position > right:
                if reversed_tail:
                    reversed_tail.next = temp_head
                break

            previous = temp_head
            temp_head = temp_head.next

        return head



class Test(unittest.TestCase):
    def test1(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)

        solution = Solution()
        actual = solution.reverseBetween(head, 2,4)

        expected = ListNode(1)
        expected.next = ListNode(4)
        expected.next.next = ListNode(3)
        expected.next.next.next = ListNode(2)
        expected.next.next.next.next = ListNode(5)

        self.assertEqual(actual, expected)

    def test2(self):
        head = ListNode(5)

        solution = Solution()
        actual = solution.reverseBetween(head, 1,1)

        expected = ListNode(5)
        self.assertEqual(actual, expected)

    def test3(self):
        head = ListNode(3)
        head.next = ListNode(5)

        solution = Solution()
        actual = solution.reverseBetween(head, 1,2)

        expected = ListNode(5)
        expected.next = ListNode(3)

        self.assertEqual(actual, expected)

