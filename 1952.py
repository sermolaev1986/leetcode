import unittest

class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for divisor in range(1, n + 1):
            if n % divisor == 0:
                count += 1

            if count > 3:
                return False

        return count == 3

class PrimeSquareSolution:
    def isThree(self, n: int) -> bool:
        if n < 2:
            return False

        root = int(n**0.5)

        # Check if it's a perfect square
        if root * root != n:
            return False

        # Check if the square root is prime
        for i in range(2, int(root**0.5) + 1):
            if root % i == 0:
                return False

        return True

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertFalse(Solution().isThree(1))
        self.assertFalse(PrimeSquareSolution().isThree(1))

    def test4(self):
        self.assertTrue(Solution().isThree(4))
        self.assertTrue(PrimeSquareSolution().isThree(4))

    def test12(self):
        self.assertFalse(Solution().isThree(12))
        self.assertFalse(PrimeSquareSolution().isThree(12))
