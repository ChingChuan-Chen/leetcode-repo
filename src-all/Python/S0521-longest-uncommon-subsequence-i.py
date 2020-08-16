"""
Given two strings, you need to find the longest uncommon subsequence of this two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other string.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn&#39;t exist, return -1.

 
Example 1:
Input: a = &quot;aba&quot;, b = &quot;cdc&quot;
Output: 3
Explanation: The longest uncommon subsequence is &quot;aba&quot;, 
because &quot;aba&quot; is a subsequence of &quot;aba&quot;, 
but not a subsequence of the other string &quot;cdc&quot;.
Note that &quot;cdc&quot; can be also a longest uncommon subsequence.

Example 2:
Input: a = &quot;aaa&quot;, b = &quot;bbb&quot;
Output: 3

Example 3:
Input: a = &quot;aaa&quot;, b = &quot;aaa&quot;
Output: -1

 
Constraints:
	Both strings&#39; lengths will be between [1 - 100].
	Only letters from a ~ z will appear in input strings.


"""
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().findLUSlength(0) == 0

