# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        candidates = []
        while i < m + n:
            if i < m:
                candidates.append(nums1[i])
            if i < n:
                candidates.append(nums2[i])
            minimum = None
            for candidate in candidates:
                if minimum is None or candidate < minimum:
                    minimum = candidate
            candidates.remove(minimum)

            nums1[i] = minimum

            i += 1
        