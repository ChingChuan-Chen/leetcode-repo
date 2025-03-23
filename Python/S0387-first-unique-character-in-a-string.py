"""
Given a string, find the first non-repeating character in it and return its index.
If it doesn't exist, return -1.

Examples:
1. s = "leetcode" return 0.
2. s = "loveleetcode" return 2.

Note: You may assume the string contains only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1

        seen_char = {}
        for i, char in enumerate(s):
            seen_char[char] = seen_char.get(char, 0) + 1

        for i, char in enumerate(s):
            if seen_char[char] == 1:
                return i
        return -1


if __name__ == '__main__':
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
    assert Solution().firstUniqChar("letcod") == 0
    assert Solution().firstUniqChar("ll") == -1
    assert Solution().firstUniqChar("l") == 0
    assert Solution().firstUniqChar("") == -1
