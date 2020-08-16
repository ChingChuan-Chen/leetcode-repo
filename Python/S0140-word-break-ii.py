"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
	The same word in the dictionary may be reused multiple times in the segmentation.
	You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = &quot;catsanddog&quot;
wordDict = [&quot;cat&quot;, &quot;cats&quot;, &quot;and&quot;, &quot;sand&quot;, &quot;dog&quot;]
Output:
[
  &quot;cats and dog&quot;,
  &quot;cat sand dog&quot;
]

Example 2:
Input:
s = &quot;pineapplepenapple&quot;
wordDict = [&quot;apple&quot;, &quot;pen&quot;, &quot;applepen&quot;, &quot;pine&quot;, &quot;pineapple&quot;]
Output:
[
  &quot;pine apple pen apple&quot;,
  &quot;pineapple pen apple&quot;,
  &quot;pine applepen apple&quot;
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = &quot;catsandog&quot;
wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]
Output:
[]

"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().wordBreak(0) == 0

