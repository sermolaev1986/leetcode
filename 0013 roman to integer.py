# https://leetcode.com/problems/roman-to-integer/
roman_to_int = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        previous = 0

        for char in reversed(s):
            current = roman_to_int[char]
            if current < previous:
                result -= current
            else:
                result += current
            previous = current

        return result