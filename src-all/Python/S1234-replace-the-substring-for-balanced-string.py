"""
You are given a string containing only 4 kinds of characters &#39;Q&#39;, &#39;W&#39;, &#39;E&#39; and &#39;R&#39;.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.

 
Example 1:
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.

Example 2:
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a &#39;Q&#39; to &#39;R&#39;, so that "RQWE" (or "QRWE") is balanced.

Example 3:
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 

Example 4:
Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 &#39;Q&#39; to make s = "QWER".

 
Constraints:
	1 <= s.length <= 10^5
	s.length is a multiple of 4
	s contains only &#39;Q&#39;, &#39;W&#39;, &#39;E&#39; and &#39;R&#39;.


"""
class Solution:
    def balancedString(self, s: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().balancedString(0) == 0

