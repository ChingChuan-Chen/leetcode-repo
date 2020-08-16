"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

&#39;A&#39; -> 1
&#39;B&#39; -> 2
...
&#39;Z&#39; -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: &quot;12&quot;
Output: 2
Explanation: It could be decoded as &quot;AB&quot; (1 2) or &quot;L&quot; (12).

Example 2:
Input: &quot;226&quot;
Output: 3
Explanation: It could be decoded as &quot;BZ&quot; (2 26), &quot;VF&quot; (22 6), or &quot;BBF&quot; (2 2 6).

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numDecodings(0) == 0

