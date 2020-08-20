"""
Given an input string, reverse the string word by word.

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Note:
	A word is defined as a sequence of non-space characters.
	Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
	You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up:
For C programmers, try to solve it in-place in O(1) extra space.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        out_str = ""
        start_idx = -1
        for i in range(0, len(s)):
            if s[i] != " " and start_idx == -1:
                start_idx = i
            elif s[i] == " " and start_idx >= 0:
                out_str = s[start_idx:i] + " " + out_str
                start_idx = -1
        # for the last word
        if start_idx >= 0:
            out_str = s[start_idx:] + " " + out_str
        # for the last single word
        if s[-1] != " " and start_idx == -1:
            out_str = s[-1] + " " + out_str
        return out_str[:len(out_str)-1]


if __name__ == '__main__':
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"
    assert Solution().reverseWords("  hello world!  ") == "world! hello"
    assert Solution().reverseWords("a good   example") == "example good a"
    assert Solution().reverseWords(" 12") == "12"
    assert Solution().reverseWords(" 1") == "1"
    assert Solution().reverseWords("hi!") == "hi!"
    assert Solution().reverseWords(" 12 1") == "1 12"
