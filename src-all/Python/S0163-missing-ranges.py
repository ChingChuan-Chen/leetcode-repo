"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: [&quot;2&quot;, &quot;4->49&quot;, &quot;51->74&quot;, &quot;76->99&quot;]


"""
from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().findMissingRanges(0) == 0

