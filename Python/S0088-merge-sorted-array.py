"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
	The number of elements initialized in nums1 and nums2 are m and n respectively.
	You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

Constraints:
	-10^9 <= nums1[i], nums2[i] <= 10^9
	nums1.length == m + n
	nums2.length == n
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution().merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [2, 2, 2, 0, 0]
    Solution().merge(nums1, 3, [2, 2], 2)
    assert nums1 == [2, 2, 2, 2, 2]

    nums1 = [1, 1, 1, 0, 0]
    Solution().merge(nums1, 3, [2, 2], 2)
    assert nums1 == [1, 1, 1, 2, 2]

    nums1 = [1]
    Solution().merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [3, 0]
    Solution().merge(nums1, 1, [1], 1)
    assert nums1 == [1, 3]

    nums1 = [0]
    Solution().merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = []
    Solution().merge(nums1, 0, [], 0)
    assert nums1 == []
