"""
A string is called happy if it does not have any of the strings &#39;aaa&#39;, &#39;bbb&#39; or &#39;ccc&#39; as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

	s is happy and longest possible.
	s contains at most a occurrences of the letter &#39;a&#39;, at most b occurrences of the letter &#39;b&#39; and at most c occurrences of the letter &#39;c&#39;.
	s will only contain &#39;a&#39;, &#39;b&#39; and &#39;c&#39; letters.

If there is no such string s return the empty string &quot;&quot;.

 
Example 1:
Input: a = 1, b = 1, c = 7
Output: &quot;ccaccbcc&quot;
Explanation: &quot;ccbccacc&quot; would also be a correct answer.

Example 2:
Input: a = 2, b = 2, c = 1
Output: &quot;aabbc&quot;

Example 3:
Input: a = 7, b = 1, c = 0
Output: &quot;aabaa&quot;
Explanation: It&#39;s the only correct answer in this case.

 
Constraints:
	0 <= a, b, c <= 100
	a + b + c > 0


"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().longestDiverseString(0) == 0

