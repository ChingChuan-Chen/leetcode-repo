"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to
solve this problem. Could you do it in-place with O(1) extra space?

Example 1:
 Input: nums = [1,2,3,4,5,6,7], k = 3
 Output: [5,6,7,1,2,3,4]
 Explanation:
  rotate 1 steps to the right: [7,1,2,3,4,5,6]
  rotate 2 steps to the right: [6,7,1,2,3,4,5]
  rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
 Input: nums = [-1,-100,3,99], k = 2
 Output: [3,99,-1,-100]
 Explanation:
  rotate 1 steps to the right: [99,-1,-100,3]
  rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
 1 <= nums.length <= 2 * 10^4
 It's guaranteed that nums[i] fits in a 32 bit-signed integer.
 k >= 0
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end - 1] = nums[end - 1], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        reverse(nums, 0, len(nums) - k)
        reverse(nums, len(nums) - k, len(nums))
        reverse(nums, 0, len(nums))

        # Solution 2
        """
        k %= len(nums)
        for i in range(k):
            nums.insert(0, nums.pop())
        """


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 1)
    assert nums == [7, 1, 2, 3, 4, 5, 6]

    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 10)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    Solution().rotate(nums, 2)
    assert nums == [3, 99, -1, -100]
