"""
Given two arrays, write a function to compute their intersection. 

Example 1:
 Input: nums1 = [1,2,2,1], nums2 = [2,2]
 Output: [2]

Example 2:
 Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
 Output: [9,4]

Note:
 Each element in the result must be unique.
 The result can be in any order. 
"""

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        res = []
        for i in nums2:
            if i in nums1_set:
                res.append(i)
                nums1_set.remove(i)
        return res

if __name__ == '__main__':
    assert Solution().intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]