"""
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 
Example 1:
Input: s = &quot;abcabc&quot;
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are &quot;abc&quot;, &quot;abca&quot;, &quot;abcab&quot;, &quot;abcabc&quot;, &quot;bca&quot;, &quot;bcab&quot;, &quot;bcabc&quot;, &quot;cab&quot;, &quot;cabc&quot; and &quot;abc&quot; (again). 

Example 2:
Input: s = &quot;aaacb&quot;
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are &quot;aaacb&quot;, &quot;aacb&quot; and &quot;acb&quot;. 

Example 3:
Input: s = &quot;abc&quot;
Output: 1

 
Constraints:
	3 <= s.length <= 5 x 10^4
	s only consists of a, b or c characters.

"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numberOfSubstrings(0) == 0

