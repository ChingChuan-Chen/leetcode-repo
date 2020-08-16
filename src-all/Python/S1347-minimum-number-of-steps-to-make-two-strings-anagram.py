"""
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 
Example 1:
Input: s = &quot;bab&quot;, t = &quot;aba&quot;
Output: 1
Explanation: Replace the first &#39;a&#39; in t with b, t = &quot;bba&quot; which is anagram of s.

Example 2:
Input: s = &quot;leetcode&quot;, t = &quot;practice&quot;
Output: 5
Explanation: Replace &#39;p&#39;, &#39;r&#39;, &#39;a&#39;, &#39;i&#39; and &#39;c&#39; from t with proper characters to make t anagram of s.

Example 3:
Input: s = &quot;anagram&quot;, t = &quot;mangaar&quot;
Output: 0
Explanation: &quot;anagram&quot; and &quot;mangaar&quot; are anagrams. 

Example 4:
Input: s = &quot;xxyyzz&quot;, t = &quot;xxyyzz&quot;
Output: 0

Example 5:
Input: s = &quot;friend&quot;, t = &quot;family&quot;
Output: 4

 
Constraints:
	1 <= s.length <= 50000
	s.length == t.length
	s and t contain lower-case English letters only.


"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minSteps(0) == 0

