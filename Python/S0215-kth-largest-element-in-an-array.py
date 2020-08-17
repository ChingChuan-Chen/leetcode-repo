"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 <= k <= array's length.

"""
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums)-1
        while True:
            pivot = nums[left]
            l = left+1
            r = right
            while l <= r:
                if nums[l] < pivot < nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[left], nums[r] = nums[r], nums[left]

            if r == k-1:
                return nums[r]
            if r > k-1:
                right = r - 1
            else:
                left = r + 1

if __name__ == '__main__':
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

