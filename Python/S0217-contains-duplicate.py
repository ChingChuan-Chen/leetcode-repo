"""
Given an array of integers, find if the array contains any duplicates. 

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:
 Input: [1,2,3,1]
 Output: true

Example 2:
 Input: [1,2,3,4]
 Output: false

Example 3:
 Input: [1,1,1,3,3,4,3,2,4,2]
 Output: true
"""

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False

if __name__ == '__main__':
    assert Solution().containsDuplicate([1, 2, 3, 1]) == True
    assert Solution().containsDuplicate([1, 2, 3, 4]) == False
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
