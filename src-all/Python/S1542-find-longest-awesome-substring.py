"""
Given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it palindrome.

Return the length of the maximum length awesome substring of s.

 
Example 1:
Input: s = &quot;3242415&quot;
Output: 5
Explanation: &quot;24241&quot; is the longest awesome substring, we can form the palindrome &quot;24142&quot; with some swaps.

Example 2:
Input: s = &quot;12345678&quot;
Output: 1

Example 3:
Input: s = &quot;213123&quot;
Output: 6
Explanation: &quot;213123&quot; is the longest awesome substring, we can form the palindrome &quot;231132&quot; with some swaps.

Example 4:
Input: s = &quot;00&quot;
Output: 2

 
Constraints:
	1 <= s.length <= 10^5
	s consists only of digits.


"""
class Solution:
    def longestAwesome(self, s: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().longestAwesome(0) == 0

