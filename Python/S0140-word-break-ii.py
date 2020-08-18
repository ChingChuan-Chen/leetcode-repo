"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Note:
  The same word in the dictionary may be reused multiple times in the segmentation.
  You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""
from collections import Counter
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if Counter(s).keys() > Counter("".join(wordDict)).keys():
            return []

        wordDictSet = set(wordDict)
        dp = [[]] * (len(s) + 1)
        dp[0] = [[0]]

        for j in range(1, len(s) + 1):
            stops = []
            for i in range(0, j):
                if s[i:j] in wordDictSet:
                    stops.append([i, j])
            dp[j] = stops

        res = []
        def dfs(path, dp_index):
            if dp_index == 0:
                res.append(" ".join(path))
                return
            for i, j in dp[dp_index]:
                dfs([s[i:j]] + path, i)
        dfs([], len(s))
        return res

if __name__ == '__main__':
    assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == \
           ["cat sand dog", "cats and dog"]
    assert Solution().wordBreak("aaaaaa", ["aa", "aaa", "aaaa", "aaaaa"]) == \
           ['aa aaaa', 'aaa aaa', 'aaaa aa', 'aa aa aa']
    assert Solution().wordBreak("aaaaaaa", ["aa", "aaa", "aaaa", "aaaaa"]) == \
           ['aa aaaaa', 'aaa aaaa', 'aaaa aaa', 'aa aa aaa', 'aaaaa aa', 'aa aaa aa', 'aaa aa aa']
    assert Solution().wordBreak("pineapplepenapple",
                                ["apple", "pen", "applepen", "pine", "pineapple"]) == \
           ["pine applepen apple", "pineapple pen apple", "pine apple pen apple"]
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []

    string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    word_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    assert Solution().wordBreak(string, word_dict) == []
