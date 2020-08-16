"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:
Input: str1 = &quot;abac&quot;, str2 = &quot;cab&quot;
Output: &quot;cabac&quot;
Explanation: 
str1 = &quot;abac&quot; is a subsequence of &quot;cabac&quot; because we can delete the first &quot;c&quot;.
str2 = &quot;cab&quot; is a subsequence of &quot;cabac&quot; because we can delete the last &quot;ac&quot;.
The answer provided is the shortest such string that satisfies these properties.

 

Note:
	1 <= str1.length, str2.length <= 1000
	str1 and str2 consist of lowercase English letters.


"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().shortestCommonSupersequence(0) == 0

