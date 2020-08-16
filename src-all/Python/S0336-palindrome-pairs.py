"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Input: [&quot;abcd&quot;,&quot;dcba&quot;,&quot;lls&quot;,&quot;s&quot;,&quot;sssll&quot;]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are [&quot;dcbaabcd&quot;,&quot;abcddcba&quot;,&quot;slls&quot;,&quot;llssssll&quot;]

Example 2:
Input: [&quot;bat&quot;,&quot;tab&quot;,&quot;cat&quot;]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are [&quot;battab&quot;,&quot;tabbat&quot;]


"""
from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        pass


if __name__ == '__main__':
    assert Solution().palindromePairs(0) == 0

