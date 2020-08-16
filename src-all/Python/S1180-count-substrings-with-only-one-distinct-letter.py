"""
Given a string S, return the number of substrings that have only one distinct letter.

 
Example 1:
Input: S = &quot;aaaba&quot;
Output: 8
Explanation: The substrings with one distinct letter are &quot;aaa&quot;, &quot;aa&quot;, &quot;a&quot;, &quot;b&quot;.
&quot;aaa&quot; occurs 1 time.
&quot;aa&quot; occurs 2 times.
&quot;a&quot; occurs 4 times.
&quot;b&quot; occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.

Example 2:
Input: S = &quot;aaaaaaaaaa&quot;
Output: 55

 
Constraints:
	1 <= S.length <= 1000
	S[i] consists of only lowercase English letters.


"""
class Solution:
    def countLetters(self, S: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().countLetters(0) == 0

