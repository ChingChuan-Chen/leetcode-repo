"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_char = {}
        for i, char in enumerate(s):
            seen_char[char] = seen_char.get(char, 0) + 1

        for i, char in enumerate(t):
            seen_char[char] = seen_char.get(char, 0) - 1
            if seen_char[char] < 0:
                return False
        return True

if __name__ == '__main__':
    assert Solution().isAnagram("anagram", "nagaram") == True
    assert Solution().isAnagram("rat", "car") == False
    assert Solution().isAnagram("rat", "") == False
    assert Solution().isAnagram("", "car") == False
    assert Solution().isAnagram("a", "ab") == False
    assert Solution().isAnagram("ab", "a") == False
