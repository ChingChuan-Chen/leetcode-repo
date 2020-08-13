"""
Given an array of integers, return indices of the two numbers such
that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = dict()
        for index, num in enumerate(nums):
            if target - num in diff_dict.keys():
                return [diff_dict[target-num], index]
            else:
                diff_dict[num] = index
        return []

if __name__ == '__main__':
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([2, 7, 11, 15], 18) == [1, 2]
    assert Solution().twoSum([2, 7, 11, 15], 17) == [0, 3]


