"""
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:

	A.length >= 3
	There exists some i with 0 < i < A.length - 1 such that:
		A[0] < A[1] < ... A[i-1] < A[i] 
		A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note:
	0 <= A.length <= 10000
	0 <= A[i] <= 10000
"""
from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        i = 1
        while i < len(A) and A[i] > A[i-1]:
            i += 1
        if i == 1 or i == len(A):
            return False
        while i < len(A) and A[i] < A[i-1]:
            i += 1
        return i == len(A)


if __name__ == '__main__':
    assert Solution().validMountainArray([2, 1]) == False
    assert Solution().validMountainArray([3, 5, 5]) == False
    assert Solution().validMountainArray([0, 3, 2, 1]) == True
    assert Solution().validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == False
    assert Solution().validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
