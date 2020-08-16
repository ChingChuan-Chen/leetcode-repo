"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for &#39;.&#39; and &#39;*&#39;.

&#39;.&#39; Matches any single character.
&#39;*&#39; Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:
	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = &quot;aa&quot;
p = &quot;a&quot;
Output: false
Explanation: &quot;a&quot; does not match the entire string &quot;aa&quot;.

Example 2:
Input:
s = &quot;aa&quot;
p = &quot;a*&quot;
Output: true
Explanation: &#39;*&#39; means zero or more of the preceding element, &#39;a&#39;. Therefore, by repeating &#39;a&#39; once, it becomes &quot;aa&quot;.

Example 3:
Input:
s = &quot;ab&quot;
p = &quot;.*&quot;
Output: true
Explanation: &quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.

Example 4:
Input:
s = &quot;aab&quot;
p = &quot;c*a*b&quot;
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches &quot;aab&quot;.

Example 5:
Input:
s = &quot;mississippi&quot;
p = &quot;mis*is*p*.&quot;
Output: false


"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isMatch(0) == 0

