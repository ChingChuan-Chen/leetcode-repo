"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, &quot;ACE&quot; is a subsequence of &quot;ABCDE&quot; while &quot;AEC&quot; is not).

It&#39;s guaranteed the answer fits on a 32-bit signed integer.

Example 1:
Input: S = &quot;rabbbit&quot;, T = &quot;rabbit&quot;
Output: 3
Explanation:
As shown below, there are 3 ways you can generate &quot;rabbit&quot; from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:
Input: S = &quot;babgbag&quot;, T = &quot;bag&quot;
Output: 5
Explanation:
As shown below, there are 5 ways you can generate &quot;bag&quot; from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^


"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numDistinct(0) == 0

