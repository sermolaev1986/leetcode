class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        digital_root = num % 9
        if digital_root == 0:
            return 9
        return digital_root