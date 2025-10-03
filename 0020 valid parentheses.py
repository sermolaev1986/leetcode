# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack or {")": "(", "}": "{", "]": "["}[char] != stack.pop():
                    return False

        return not stack
