"""LeetCode 20: Valid Parentheses"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        matching = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in matching.values():
                stack.append(char)
            elif char in matching:
                if not stack or stack.pop() != matching[char]:
                    return False
            else:
                continue
        return not stack


if __name__ == "__main__":
    samples = ["()[]{}", "(]", "{[]}"]
    solver = Solution()
    for sample in samples:
        print(f"{sample!r} valid? {solver.isValid(sample)}")
