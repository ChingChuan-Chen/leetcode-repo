# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#  Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#  You may assume nums1 and nums2 cannot be both empty.
#
#  Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#  Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

# https://www.youtube.com/watch?v=LPFhl65R7ww

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        n = len(nums1)
        m = len(nums2)
        low = 0
        high = n
        target = (n + m + 1) // 2
        while low <= high:
            partition1_loc = (low + high)//2
            partition2_loc = target - partition1_loc

            partition1_left_max = float('-inf') if partition1_loc == 0 else nums1[partition1_loc-1]
            partition1_right_min = float('inf') if partition1_loc == n else nums1[partition1_loc]

            partition2_left_max = float('-inf') if partition2_loc == 0 else nums2[partition2_loc-1]
            partition2_right_min = float('inf') if partition2_loc == m else nums2[partition2_loc]

            if (partition1_left_max <= partition2_right_min) and (partition1_right_min >= partition2_left_max):
                if (m + n) % 2 == 1:
                    return float(max(partition1_left_max, partition2_left_max))
                else:
                    return (max(partition1_left_max, partition2_left_max)+min(partition1_right_min, partition2_right_min))/2.
            else:
                if partition1_left_max > partition2_right_min:
                    high = partition1_loc - 1
                elif partition2_left_max > partition1_right_min:
                    low = partition1_loc + 1

if __name__ == '__main__':
    assert Solution().findMedianSortedArrays([], [1]) == 1.
    assert Solution().findMedianSortedArrays([], [1, 3, 5]) == 3.
    assert Solution().findMedianSortedArrays([], [1, 2]) == 1.5
    assert Solution().findMedianSortedArrays([], [0, 1, 2, 3]) == 1.5
    assert Solution().findMedianSortedArrays([3], [-2, -1]) == -1.
    assert Solution().findMedianSortedArrays([1], [2, 3]) == 2.
    assert Solution().findMedianSortedArrays([2, 7, 11, 15], [2, 7, 15]) == 7.
    assert Solution().findMedianSortedArrays([2, 7, 11, 15], [2, 9, 13, 15]) == 10.
    assert Solution().findMedianSortedArrays([2, 7, 11, 15], [-2, -1]) == 4.5
    assert Solution().findMedianSortedArrays([2, 7, 11, 15], [-5, -2, -1]) == 2.
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5

