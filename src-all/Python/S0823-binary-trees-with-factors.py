"""
Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any number of times.

Each non-leaf node&#39;s value should be equal to the product of the values of it&#39;s children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:
Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:
Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

 

Note:
	1 <= A.length <= 1000.
	2 <= A[i] <= 10 ^ 9.


"""
from typing import List
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numFactoredBinaryTrees(0) == 0

