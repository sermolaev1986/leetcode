from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        beautiful_pairs = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if self.is_beautiful(nums[i], nums[j]):
                    beautiful_pairs += 1

        return beautiful_pairs

    def is_beautiful(self, num1: int, num2: int) -> bool:
        first_digit = int(str(num1)[0])
        last_digit = int(str(num2)[-1])

        return self.gcd(first_digit, last_digit) == 1

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b

        return a