import math
import unittest
from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next

    def __hash__(self):
        return id(self)

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
    def minimumPairRemoval(self, nums: List[int]) -> int:
        head = self.to_linked_list(nums)

        print(head)

        operations_count = 0
        while self.is_decreasing(head):
            print(head, "is not sorted, continue")
            min_index, min_sum = self.find_minimum_pair(head)
            self.replace_with_sum(head, min_index, min_sum)
            operations_count += 1

        print(head, "is sorted now, done in steps: ", operations_count)

        return operations_count

    def to_linked_list(self, nums: List[int]) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        for num in nums:
            next = ListNode(num)
            head.next = next
            next.prev = head if head is not dummy else None
            head = head.next

        return dummy.next

    def is_decreasing(self, head: ListNode) -> bool:
        while head and head.next:
            if head.val > head.next.val:
                return True
            head = head.next

        return False

    def find_minimum_pair(self, head: ListNode):
        min_sum = math.inf
        index = -1
        min_index = -1
        while head and head.next:
            index += 1
            sum = head.val + head.next.val
            if sum < min_sum:
                min_sum = sum
                min_index = index

            head = head.next

        return min_index, min_sum

    def replace_with_sum(self, head, index, sum):
        for i in range(index):
            head = head.next

        head.val = sum
        head.next = head.next.next


class SolutionWithOptimizations:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        head = self.to_linked_list(nums)
        self._uid = 0
        heap = self.get_min_heap(head)

        print(head)

        operations_count = 0
        while self.is_decreasing(head):
            print(head, "is not sorted, continue")
            if not heap:
                print("heap is empty")
                break

            self.merge_min_pair(heap)
            operations_count += 1


        print(head, "is sorted now, done in steps: ", operations_count)

        return operations_count

    def to_linked_list(self, nums: List[int]) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        for num in nums:
            next = ListNode(num)
            head.next = next
            next.prev = head if head is not dummy else None
            head = head.next

        return dummy.next

    def get_min_heap(self, head: ListNode):
        heap = []
        while head and head.next:
            heapq.heappush(heap, (head.val + head.next.val, self._next_uid(), head, head.next))
            head = head.next

        return heap

    def _next_uid(self):
        self._uid += 1
        return self._uid

    def is_decreasing(self, head: ListNode) -> bool:
        while head and head.next:
            if head.val > head.next.val:
                return True
            head = head.next

        return False

    def merge_min_pair(self, heap: list):
        while heap:
            min_sum, _, left, right = heapq.heappop(heap)
            # Validate the pair is still adjacent and unchanged
            if left.next is not right:
                continue
            if left.val + right.val != min_sum:
                continue

            # Merge right into left
            left.val = min_sum
            left.next = right.next
            if right.next is not None:
                right.next.prev = left

            # Push affected neighbors only
            if left.next is not None:
                heapq.heappush(heap, (left.val + left.next.val, self._next_uid(), left, left.next))

            left_prev = left.prev
            if left_prev is not None:
                heapq.heappush(heap, (left_prev.val + left.val, self._next_uid(), left_prev, left))

            return min_sum, left

        return None, None


class Test(unittest.TestCase):
    def test_case_1(self):
        # solution = Solution()
        # actual = solution.minimumPairRemoval([5,3,2,1])
        # self.assertEqual(actual, 2)

        solution = SolutionWithOptimizations()
        actual = solution.minimumPairRemoval([5, 3, 2, 1])
        self.assertEqual(actual, 2)