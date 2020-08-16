"""
You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 
Example 1:
Input: s = &quot;(abcd)&quot;
Output: &quot;dcba&quot;

Example 2:
Input: s = &quot;(u(love)i)&quot;
Output: &quot;iloveu&quot;
Explanation: The substring &quot;love&quot; is reversed first, then the whole string is reversed.

Example 3:
Input: s = &quot;(ed(et(oc))el)&quot;
Output: &quot;leetcode&quot;
Explanation: First, we reverse the substring &quot;oc&quot;, then &quot;etco&quot;, and finally, the whole string.

Example 4:
Input: s = &quot;a(bcdefghijkl(mno)p)q&quot;
Output: &quot;apmnolkjihgfedcbq&quot;

 
Constraints:
	0 <= s.length <= 2000
	s only contains lower case English characters and parentheses.
	It&#39;s guaranteed that all parentheses are balanced.


"""
class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().reverseParentheses(0) == 0

