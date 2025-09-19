class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors_count = 0
        for i in range(1, min(1000, max(a, b)) + 1):
            if a % i == 0 and b % i == 0:
                factors_count += 1

        return factors_count