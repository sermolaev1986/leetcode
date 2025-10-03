# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(len(nums)):
            num_to_index[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            num_to_index.get()
            if complement in num_to_index and num_to_index[complement] != i:
                return [i, num_to_index[complement]]