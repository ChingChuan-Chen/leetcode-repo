# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
#
#  Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
#  Example 2:
# Input: "cbbd"
# Output: "bb"

# https://www.youtube.com/watch?v=UflHuQj6MVA
# https://medium.com/@ChYuan/leetcode-no-322-longest-palindromic-substring-%E5%BF%83%E5%BE%97-medium-3ff9eff34230
# https://www.felix021.com/blog/read.php?2040
# https://medium.com/hoskiss-stand/manacher-299cf75db97e
# it can be sovled by Manacher's Algorithm

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
                if (s[i] == s[j]) and ((i-j<2) or (is_palindromic[j+1][i-1])):
                    is_palindromic[j][i] = True
                    if max_len < i-j+1:
                        start = j
                        max_len = i-j+1
                j -= 1
        return s[start:(start+max_len)]

if __name__ == '__main__':
    assert Solution().longestPalindrome("babad") == "bab"
    assert Solution().longestPalindrome("cbbd") == "bb"
    assert Solution().longestPalindrome("abccba") == "abccba"
    assert Solution().longestPalindrome("abcAcba") == "abcAcba"
    assert Solution().longestPalindrome("abcda") == "a"
    assert Solution().longestPalindrome("a") == "a"
    assert Solution().longestPalindrome("") == ""

