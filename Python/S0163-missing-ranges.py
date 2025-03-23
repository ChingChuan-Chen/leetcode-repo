"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        prev = lower - 1  # Start one before lower

        for num in nums + [upper + 1]:  # Add sentinel to handle final range
            if num - prev == 2:
                result.append(str(prev + 1))
            elif num - prev > 2:
                result.append(f"{prev + 1}->{num - 1}")
            prev = num

        return result


if __name__ == '__main__':
    assert Solution().findMissingRanges([0, 2], 0, 3) == ["1"]
    assert Solution().findMissingRanges([0, 3], 0, 3) == ["1->2"]
    assert Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99) == ["2", "4->49", "51->74", "76->99"]
    assert Solution().findMissingRanges([0, 1, 3, 10, 15], 0, 16) == ["2", "4->9", "11->14", "16"]
