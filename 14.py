import math
import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        matrix = []
        smallest = math.inf

        for str in strs:
            smallest = min(smallest, len(str))
            for i in range(smallest):
                if i >= len(matrix):
                    matrix.append([])
                matrix[i].append(str[i])

        print(matrix)

        prefix = ""
        for row in matrix:
            if len(row) == len(strs) and len(set(row)) == 1:
                prefix += row.pop()
            else:
                break

        return prefix

class VerticalScanningSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs) if strs else ""


class UnitTest(unittest.TestCase):
    def test1(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(Solution().longestCommonPrefix(strs), "fl")
        self.assertEqual(VerticalScanningSolution().longestCommonPrefix(strs), "fl")

    def test2(self):
        strs = ["dog", "racecar", "car"]
        self.assertEqual(Solution().longestCommonPrefix(strs), "")
        self.assertEqual(VerticalScanningSolution().longestCommonPrefix(strs), "")

    def test3(self):
        strs = ["ab", "a"]
        self.assertEqual(Solution().longestCommonPrefix(strs), "a")
        self.assertEqual(VerticalScanningSolution().longestCommonPrefix(strs), "a")
