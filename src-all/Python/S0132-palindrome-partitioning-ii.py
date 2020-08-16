"""
Given a string s, partition s such that every substring of the partition is a palindrome

Return the minimum cuts needed for a palindrome partitioning of s.

 
Example 1:
Input: s = &quot;aab&quot;
Output: 1
Explanation: The palindrome partitioning [&quot;aa&quot;,&quot;b&quot;] could be produced using 1 cut.

Example 2:
Input: s = &quot;a&quot;
Output: 0

Example 3:
Input: s = &quot;ab&quot;
Output: 1

 
Constraints:
	1 <= s.length <= 2000
	s consists of lower-case English letters only.


"""
class Solution:
    def minCut(self, s: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minCut(0) == 0

