"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Constraints:
	0 <= nums.length <= 10^5
	-10^9 <= nums[i] <= 10^9
	nums is a non decreasing array.
	-10^9 <= target <= 10^9
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(compare):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if compare(nums[mid], target):
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        lb = binarySearch(lambda x, y: x >= y)
        if lb >= len(nums) or nums[lb] != target:
            return [-1, -1]
        rb = binarySearch(lambda x, y: x > y)
        return [lb, rb-1]


if __name__ == '__main__':
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    assert Solution().searchRange([1], 1) == [0, 0]