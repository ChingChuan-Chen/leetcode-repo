"""
We are given that the string &quot;abc&quot; is valid.

From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X + &quot;abc&quot; + Y is also valid.

If for example S = &quot;abc&quot;, then examples of valid strings are: &quot;abc&quot;, &quot;aabcbc&quot;, &quot;abcabc&quot;, &quot;abcabcababcc&quot;.  Examples of invalid strings are: &quot;abccba&quot;, &quot;ab&quot;, &quot;cababc&quot;, &quot;bac&quot;.

Return true if and only if the given string S is valid.

 

Example 1:
Input: &quot;aabcbc&quot;
Output: true
Explanation: 
We start with the valid string &quot;abc&quot;.
Then we can insert another &quot;abc&quot; between &quot;a&quot; and &quot;bc&quot;, resulting in &quot;a&quot; + &quot;abc&quot; + &quot;bc&quot; which is &quot;aabcbc&quot;.

Example 2:
Input: &quot;abcabcababcc&quot;
Output: true
Explanation: 
&quot;abcabcabc&quot; is valid after consecutive insertings of &quot;abc&quot;.
Then we can insert &quot;abc&quot; before the last letter, resulting in &quot;abcabcab&quot; + &quot;abc&quot; + &quot;c&quot; which is &quot;abcabcababcc&quot;.

Example 3:
Input: &quot;abccba&quot;
Output: false

Example 4:
Input: &quot;cababc&quot;
Output: false

 

Note:
	1 <= S.length <= 20000
	S[i] is &#39;a&#39;, &#39;b&#39;, or &#39;c&#39;

 


"""
class Solution:
    def isValid(self, S: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().isValid(0) == 0

