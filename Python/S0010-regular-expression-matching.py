"""
Given an input string (s) and a pattern (p), implement regular expression matching with
support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
by repeating 'a' once, it becomes "aa".


Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".


Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0] = True

        for j in range(1, len(p)+1):
            if j > 1 and p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if dp[i-1][j-1] and p[j-1] in {s[i-1], '.'}:
                    dp[i][j] = True
                elif j > 1 and p[j-1] == '*':
                    if dp[i][j-1] or dp[i][j-2]:
                        dp[i][j] = True
                    elif p[j-2] in {s[i-1], '.'} and dp[i-1][j]:
                        dp[i][j] = True
        return dp[len(s)][len(p)]

if __name__ == '__main__':
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "a*") == True
    assert Solution().isMatch("ab", ".*") == True
    assert Solution().isMatch("az", "a.") == True
    assert Solution().isMatch("az", "a*") == False
    assert Solution().isMatch("", "b*") == True
    assert Solution().isMatch("aaa", "") == False
    assert Solution().isMatch("", "") == True
    assert Solution().isMatch("aab", "c*a*b") == True
    assert Solution().isMatch("mississippi", "mis*is*p*.") == False
    assert Solution().isMatch("mississippi", "mis*is*ip*i") == True

