"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for &#39;?&#39; and &#39;*&#39;.

&#39;?&#39; Matches any single character.
&#39;*&#39; Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = &quot;aa&quot;
p = &quot;a&quot;
Output: false
Explanation: &quot;a&quot; does not match the entire string &quot;aa&quot;.

Example 2:
Input:
s = &quot;aa&quot;
p = &quot;*&quot;
Output: true
Explanation: &#39;*&#39; matches any sequence.

Example 3:
Input:
s = &quot;cb&quot;
p = &quot;?a&quot;
Output: false
Explanation: &#39;?&#39; matches &#39;c&#39;, but the second letter is &#39;a&#39;, which does not match &#39;b&#39;.

Example 4:
Input:
s = &quot;adceb&quot;
p = &quot;*a*b&quot;
Output: true
Explanation: The first &#39;*&#39; matches the empty sequence, while the second &#39;*&#39; matches the substring &quot;dce&quot;.

Example 5:
Input:
s = &quot;acdcb&quot;
p = &quot;a*c?b&quot;
Output: false


"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isMatch(0) == 0

