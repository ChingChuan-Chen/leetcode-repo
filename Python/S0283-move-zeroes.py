"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Example:
 Input: [0,1,0,3,12]
 Output: [1,3,12,0,0]

Note:
 You must do this in-place without making a copy of the array.
 Minimize the total number of operations.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] > 0 or nums[i] < 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0, 0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0, 0]

    nums = [0, 0, -1, 0, 3, 12]
    Solution().moveZeroes(nums)
    assert nums == [-1, 3, 12, 0, 0, 0]

    nums = [0, 0]
    Solution().moveZeroes(nums)
    assert nums == [0, 0]

    nums = [1, 2]
    Solution().moveZeroes(nums)
    assert nums == [1, 2]
