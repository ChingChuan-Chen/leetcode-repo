"""
Implement strStr().
Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string?
This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().

Constraints:
	haystack and needle consist only of lowercase English characters.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) < len(needle):
            return -1
        # build the KMP table
        lps = [0] * len(needle)
        for i in range(1, len(needle)):
            lps[i] = lps[i-1]
            while lps[i] > 0 and needle[lps[i]] != needle[i]:
                lps[i] = lps[lps[i] - 1]
            if needle[lps[i]] == needle[i]:
                lps[i] += 1

        # do the matching
        pre = 0
        for j in range(len(haystack)):
            while pre > 0 and needle[pre] != haystack[j]:
                pre = lps[pre - 1]
            if needle[pre] == haystack[j]:
                pre += 1
            if pre == len(needle):
                return j - pre + 1
        return -1

if __name__ == '__main__':
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("hello", "lo") == 3
    assert Solution().strStr("hello", "lop") == -1
    assert Solution().strStr("aaaaa", "bba") == -1
    assert Solution().strStr("aaaaa", "") == 0
    assert Solution().strStr("abxabcabcaby", "abcaby") ==  6
