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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = last = None
        carry = False
        while l1 or l2 or carry:
            sum = 0
            sum += l1.val if l1 else 0
            sum += l2.val if l2 else 0
            sum += 1 if carry else 0

            carry = sum > 9

            next = ListNode(sum % 10)
            if last:
                last.next = next
            last = next

            if not head:
                head = last

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head


class Test(unittest.TestCase):
    def test1(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        solution = Solution()
        actual = solution.addTwoNumbers(l1, l2)

        expected = ListNode(7)
        expected.next = ListNode(0)
        expected.next.next = ListNode(8)

        self.assertEqual(expected, actual)