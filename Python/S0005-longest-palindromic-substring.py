"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        start = 0
        max_len = 1
        is_palindromic = []
        for i in range(len(s)):
            is_palindromic.append([False] * len(s))
        for i in range(len(s)):
            j = i
            while j >= 0:
                if (s[i] == s[j]) and ((i - j < 2) or (is_palindromic[j + 1][i - 1])):
                    is_palindromic[j][i] = True
                    if max_len < i - j + 1:
                        start = j
                        max_len = i - j + 1
                j -= 1
        return s[start:(start + max_len)]


if __name__ == '__main__':
    assert Solution().longestPalindrome("babad") == "bab"
    assert Solution().longestPalindrome("cbbd") == "bb"
    assert Solution().longestPalindrome("abccba") == "abccba"
    assert Solution().longestPalindrome("abcAcba") == "abcAcba"
    assert Solution().longestPalindrome("abcda") == "a"
    assert Solution().longestPalindrome("a") == "a"
    assert Solution().longestPalindrome("") == ""
