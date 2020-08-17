"""
Given an array nums of n integers and an integer target, find three integers in nums such that
the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Constraints:
	3 <= nums.length <= 10^3
	-10^3 <= nums[i] <= 10^3
	-10^4 <= target <= 10^4
"""
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")
        n = len(nums)
        nums.sort()
        print(nums)
        for i in range(0, n-2):
            j, k = i+1, n-1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if abs(tmp-target) < abs(res-target):
                    res = tmp
                if tmp > target:
                    k -= 1
                elif tmp < target:
                    j += 1
                else:
                    break
        return res


if __name__ == '__main__':
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert Solution().threeSumClosest([1, 1, 1, 0], 100) == 3
    assert Solution().threeSumClosest([0, 2, 1, -3], 1) == 0
