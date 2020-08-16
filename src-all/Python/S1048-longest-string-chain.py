"""
Given a list of words, each word consists of English lowercase letters.

Let&#39;s say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, &quot;abc&quot; is a predecessor of &quot;abac&quot;.

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:
Input: [&quot;a&quot;,&quot;b&quot;,&quot;ba&quot;,&quot;bca&quot;,&quot;bda&quot;,&quot;bdca&quot;]
Output: 4
Explanation: one of the longest word chain is &quot;a&quot;,&quot;ba&quot;,&quot;bda&quot;,&quot;bdca&quot;.

 

Note:
	1 <= words.length <= 1000
	1 <= words[i].length <= 16
	words[i] only consists of English lowercase letters.

 

"""
from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().longestStrChain(0) == 0

