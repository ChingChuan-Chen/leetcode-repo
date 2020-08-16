"""
Given a parentheses string s containing only the characters &#39;(&#39; and &#39;)&#39;. A parentheses string is balanced if:

	Any left parenthesis &#39;(&#39; must have a corresponding two consecutive right parenthesis &#39;))&#39;.
	Left parenthesis &#39;(&#39; must go before the corresponding two consecutive right parenthesis &#39;))&#39;.

In other words, we treat &#39;(&#39; as openning parenthesis and &#39;))&#39; as closing parenthesis.

For example, &quot;())&quot;, &quot;())(())))&quot; and &quot;(())())))&quot; are balanced, &quot;)()&quot;, &quot;()))&quot; and &quot;(()))&quot; are not balanced.

You can insert the characters &#39;(&#39; and &#39;)&#39; at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

 
Example 1:
Input: s = &quot;(()))&quot;
Output: 1
Explanation: The second &#39;(&#39; has two matching &#39;))&#39;, but the first &#39;(&#39; has only &#39;)&#39; matching. We need to to add one more &#39;)&#39; at the end of the string to be &quot;(())))&quot; which is balanced.

Example 2:
Input: s = &quot;())&quot;
Output: 0
Explanation: The string is already balanced.

Example 3:
Input: s = &quot;))())(&quot;
Output: 3
Explanation: Add &#39;(&#39; to match the first &#39;))&#39;, Add &#39;))&#39; to match the last &#39;(&#39;.

Example 4:
Input: s = &quot;((((((&quot;
Output: 12
Explanation: Add 12 &#39;)&#39; to balance the string.

Example 5:
Input: s = &quot;)))))))&quot;
Output: 5
Explanation: Add 4 &#39;(&#39; at the beginning of the string and one &#39;)&#39; at the end. The string becomes &quot;(((())))))))&quot;.

 
Constraints:
	1 <= s.length <= 10^5
	s consists of &#39;(&#39; and &#39;)&#39; only.


"""
class Solution:
    def minInsertions(self, s: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minInsertions(0) == 0

