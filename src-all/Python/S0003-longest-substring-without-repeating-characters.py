"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        used_chars = {}
        for index, char in enumerate(s):
            if char in used_chars.keys() and start <= used_chars[char]:
                start = used_chars[char] + 1
            else:
                max_length = max(max_length, index-start+1)
            used_chars[char] = index
        return max_length


if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring(0) == 0

