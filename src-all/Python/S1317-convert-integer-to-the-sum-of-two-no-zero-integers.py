"""
Given an integer n. No-Zero integer is a positive integer which doesn&#39;t contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

	A and B are No-Zero integers.
	A + B = n

It&#39;s guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.

 
Example 1:
Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B don&#39;t contain any 0 in their decimal representation.

Example 2:
Input: n = 11
Output: [2,9]

Example 3:
Input: n = 10000
Output: [1,9999]

Example 4:
Input: n = 69
Output: [1,68]

Example 5:
Input: n = 1010
Output: [11,999]

 
Constraints:
	2 <= n <= 10^4

"""
from typing import List
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        pass


if __name__ == '__main__':
    assert Solution().getNoZeroIntegers(0) == 0

