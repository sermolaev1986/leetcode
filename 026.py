import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

            right += 1

        return left + 1

class LoopSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left + 1

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().removeDuplicates([1, 1, 2]))
        self.assertEqual(2, LoopSolution().removeDuplicates([1, 1, 2]))

    def test2(self):
        self.assertEqual(5, Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
        self.assertEqual(5, LoopSolution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
