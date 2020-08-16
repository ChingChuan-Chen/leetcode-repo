"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]


"""
from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().findMissingRanges(0) == 0

