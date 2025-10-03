import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            chars = set()
            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                else:
                    chars.add(s[j])
                    if len(chars) > max_len:
                        max_len = len(chars)

        return max_len


class SlidingWindowSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        char_index = {}
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len


class TestCase(unittest.TestCase):
    def test_case_1(self):
        s = "abcabcbb"
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s))
        self.assertEqual(3, SlidingWindowSolution().lengthOfLongestSubstring(s))

    def test_case_2(self):
        s = "bbbbb"
        self.assertEqual(1, Solution().lengthOfLongestSubstring(s))
        self.assertEqual(1, SlidingWindowSolution().lengthOfLongestSubstring(s))

    def test_case_3(self):
        s = "pwwkew"
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s))
        self.assertEqual(3, SlidingWindowSolution().lengthOfLongestSubstring(s))

    def test_case_4(self):
        s = " "
        self.assertEqual(1, Solution().lengthOfLongestSubstring(s))
        self.assertEqual(1, SlidingWindowSolution().lengthOfLongestSubstring(s))