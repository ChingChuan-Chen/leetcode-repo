"""
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.

 

Example 1:
Input: [&quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot;]
Output: &quot;alexlovesleetcode&quot;
Explanation: All permutations of &quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot; would also be accepted.

Example 2:
Input: [&quot;catg&quot;,&quot;ctaagt&quot;,&quot;gcta&quot;,&quot;ttca&quot;,&quot;atgcatc&quot;]
Output: &quot;gctaagttcatgcatc&quot;

 

Note:
	1 <= A.length <= 12
	1 <= A[i].length <= 20

 

"""
from typing import List
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().shortestSuperstring(0) == 0

