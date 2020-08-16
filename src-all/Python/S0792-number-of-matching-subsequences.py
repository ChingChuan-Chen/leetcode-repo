"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = &quot;abcde&quot;
words = [&quot;a&quot;, &quot;bb&quot;, &quot;acd&quot;, &quot;ace&quot;]
Output: 3
Explanation: There are three words in words that are a subsequence of S: &quot;a&quot;, &quot;acd&quot;, &quot;ace&quot;.

Note:
	All words in words and S will only consists of lowercase letters.
	The length of S will be in the range of [1, 50000].
	The length of words will be in the range of [1, 5000].
	The length of words[i] will be in the range of [1, 50].


"""
from typing import List
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numMatchingSubseq(0) == 0

