"""
Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).

 
Example 1:
Input: text = &quot;abcabcabc&quot;
Output: 3
Explanation: The 3 substrings are &quot;abcabc&quot;, &quot;bcabca&quot; and &quot;cabcab&quot;.

Example 2:
Input: text = &quot;leetcodeleetcode&quot;
Output: 2
Explanation: The 2 substrings are &quot;ee&quot; and &quot;leetcodeleetcode&quot;.

 
Constraints:
	1 <= text.length <= 2000
	text has only lowercase English letters.


"""
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().distinctEchoSubstrings(0) == 0

