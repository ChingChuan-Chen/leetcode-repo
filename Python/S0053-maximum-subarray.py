"""
Given an integer array nums, find the contiguous sub-array (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum = float("-inf")
        s = 0
        for v in nums:
            s += v
            max_sum = max(max_sum, s)
            if s < 0:
                s = 0
        return max_sum


if __name__ == '__main__':
    assert Solution().maxSubArray([-1]) == -1
    assert Solution().maxSubArray([1]) == 1
    assert Solution().maxSubArray([-2, 1]) == 1
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([-2, 4, -3, 4, -1, 2, 1, -5, 4]) == 7
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 6]) == 7
    assert Solution().maxSubArray([1, 2, 5, -6, -3, 100]) == 100
