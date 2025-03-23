"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        i, j = 0, 0
        while i < len(strs[0]) and j < len(strs[1]):
            if strs[0][i] == strs[1][j]:
                i += 1
                j += 1
            else:
                break
        lcp = strs[0][:i]

        if i == 0 and j == 0:
            return ""

        if len(strs) == 2:
            return lcp

        for k in range(2, len(strs)):
            i, j = 0, 0
            while i < len(lcp) and j < len(strs[k]):
                if lcp[i] == strs[k][j]:
                    i += 1
                    j += 1
                else:
                    lcp = lcp[:i]
                    break
        return lcp[:i]


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["flower", "flowery", "flow"]) == "flow"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix(["carerr", "car"]) == "car"
    assert Solution().longestCommonPrefix(["carerr", "car", "example"]) == ""
    assert Solution().longestCommonPrefix([]) == ""
