# Definition for singly-linked list.
import unittest
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TwoPointersSolution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a= headA; b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a

class LengthsSolution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length_a = self.find_length(headA)
        length_b = self.find_length(headB)

        length_diff = length_a - length_b
        if length_diff > 0:
            headA = self.go_n_steps(headA, length_diff)
        elif length_diff < 0:
            headB = self.go_n_steps(headB, -length_diff)

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

    def go_n_steps(self, head: ListNode, n: int) -> ListNode:
        for i in range(n):
            head = head.next

        return head

    def find_length(self, head: ListNode) -> int:
        length = 0
        while head:
            head = head.next
            length += 1

        return length


class TestCase2(unittest.TestCase):
    def test_example1(self):
        shared_list = ListNode(8)
        shared_list.next = ListNode(4)
        shared_list.next.next = ListNode(5)

        headA = ListNode(4)
        headA.next = ListNode(1)
        headA.next.next = shared_list

        headB = ListNode(5)
        headB.next = ListNode(6)
        headB.next.next = ListNode(1)
        headB.next.next.next = shared_list

        solution = TwoPointersSolution().getIntersectionNode(headA, headB)
        self.assertEqual(solution.val, 8)

        solution = LengthsSolution().getIntersectionNode(headA, headB)
        self.assertEqual(solution.val, 8)