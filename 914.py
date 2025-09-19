import unittest
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if not deck:
            return False

        counts = {}
        for card in deck:
            counts[card] = counts.get(card, 0) + 1

        return self.gcd_for_nums(list(counts.values())) != 1

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b

        return a

    def gcd_for_nums(self, nums: list[int]) -> int:
        result = nums[0]
        for num in nums[1:]:
            result = self.gcd(result, num)

        return result


class TestSolution(unittest.TestCase):
    def test_example1(self):
        deck = [1,2,3,4,4,3,2,1]
        self.assertTrue(Solution().hasGroupsSizeX(deck))
    def test_example2(self):
        deck = [1,1,1,2,2,2,3,3]
        self.assertFalse(Solution().hasGroupsSizeX(deck))
    def test_single_card(self):
        deck = [1]
        self.assertFalse(Solution().hasGroupsSizeX(deck))
    def test_all_same(self):
        deck = [2,2,2,2]
        self.assertTrue(Solution().hasGroupsSizeX(deck))
    def test_empty(self):
        deck = []
        self.assertFalse(Solution().hasGroupsSizeX(deck))
    def test_1(self):
        deck = [1, 1, 2, 2, 2, 2]
        self.assertTrue(Solution().hasGroupsSizeX(deck))