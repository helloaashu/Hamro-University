"""LeetCode 1: Two Sum"""

from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = {}
        for idx, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], idx]
            seen[number] = idx
        raise ValueError("No valid pair found")


if __name__ == "__main__":
    inputs = [2, 7, 11, 15]
    result = Solution().twoSum(inputs, 9)
    print("Two Sum indices:", result)
