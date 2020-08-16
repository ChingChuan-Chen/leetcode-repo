"""
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

 
Example 1:
Input: s = &quot;level&quot;
Output: &quot;l&quot;
Explanation: s contains 4 prefix excluding itself (&quot;l&quot;, &quot;le&quot;, &quot;lev&quot;, &quot;leve&quot;), and suffix (&quot;l&quot;, &quot;el&quot;, &quot;vel&quot;, &quot;evel&quot;). The largest prefix which is also suffix is given by &quot;l&quot;.

Example 2:
Input: s = &quot;ababab&quot;
Output: &quot;abab&quot;
Explanation: &quot;abab&quot; is the largest prefix which is also suffix. They can overlap in the original string.

Example 3:
Input: s = &quot;leetcodeleet&quot;
Output: &quot;leet&quot;

Example 4:
Input: s = &quot;a&quot;
Output: &quot;&quot;

 
Constraints:
	1 <= s.length <= 10^5
	s contains only lowercase English letters.


"""
class Solution:
    def longestPrefix(self, s: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().longestPrefix(0) == 0

