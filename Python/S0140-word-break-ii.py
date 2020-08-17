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
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDictSet = set(wordDict)
        n = len(s)

        res = []
        def dfs(idx: int, result: List[str]):
            if idx == n:
                res.append(" ".join(result))
                return
            for j in range(idx, n+1):
                if s[idx:j] in wordDictSet:
                    result.append(s[idx:j])
                    dfs(j, result)
                    result.pop()
        dfs(0, [])
        return res


if __name__ == '__main__':
    assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == \
           ["cat sand dog", "cats and dog"]
    assert Solution().wordBreak("pineapplepenapple",
                                ["apple", "pen", "applepen", "pine", "pineapple"]) == \
           ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []

    string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    word_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    assert Solution().wordBreak(string, word_dict) == []
