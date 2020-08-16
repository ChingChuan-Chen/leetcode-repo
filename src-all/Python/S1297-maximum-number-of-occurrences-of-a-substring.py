"""
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

	The number of unique characters in the substring must be less than or equal to maxLetters.
	The substring size must be between minSize and maxSize inclusive.

 
Example 1:
Input: s = &quot;aababcaab&quot;, maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring &quot;aab&quot; has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:
Input: s = &quot;aaaa&quot;, maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring &quot;aaa&quot; occur 2 times in the string. It can overlap.

Example 3:
Input: s = &quot;aabcabcab&quot;, maxLetters = 2, minSize = 2, maxSize = 3
Output: 3

Example 4:
Input: s = &quot;abcde&quot;, maxLetters = 2, minSize = 3, maxSize = 3
Output: 0

 
Constraints:
	1 <= s.length <= 10^5
	1 <= maxLetters <= 26
	1 <= minSize <= maxSize <= min(26, s.length)
	s only contains lowercase English letters.

"""
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().maxFreq(0) == 0

