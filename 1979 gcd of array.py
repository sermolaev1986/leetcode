from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        if not nums:
            return 0

        smallest = nums[0]
        largest = nums[0]

        for num in nums:
            if num < smallest:
                smallest = num
            if num > largest:
                largest = num

        return self.gcd(smallest, largest)

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b

        return a