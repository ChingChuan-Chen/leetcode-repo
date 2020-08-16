"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


"""
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().summaryRanges(0) == 0

