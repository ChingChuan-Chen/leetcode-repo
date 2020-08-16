"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum &ge; s. If there isn&#39;t one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

"""
from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minSubArrayLen(0) == 0

