class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2147483647
        sign = 1 if x > 0 else -1
        result = 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            if (result > max_int // 10) or (result == max_int // 10 and digit > max_int % 10):
                return 0

            result = result * 10 + digit

        return sign * result