"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
  The same word in the dictionary may be reused multiple times in the segmentation.
  You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(0, n+1):
            for j in range(0, i):
                # split s[:i] into s[:j] and s[j:i]
                if dp[j] and s[j:i] in wordDictSet:
                    dp[i] = True
        return dp[n]


if __name__ == '__main__':
    assert Solution().wordBreak("leetcode", ["leet", "code"]) == True
    assert Solution().wordBreak("applepenapple", ["apple", "pen"]) == True
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert Solution().wordBreak("catsanddogs", ["cats", "and", "dogs"]) == True
    assert Solution().wordBreak("catsanddogs", ["cats", "catsand", "dogs"]) == True
    assert Solution().wordBreak("catsanddogs", ["cat", "and", "dog", "s"]) == True
