"""
Given two words (beginWord and endWord), and a dictionary&#39;s word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

	Only one letter can be changed at a time.
	Each transformed word must exist in the word list.

Note:
	Return 0 if there is no such transformation sequence.
	All words have the same length.
	All words contain only lowercase alphabetic characters.
	You may assume no duplicates in the word list.
	You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

Output: 5

Explanation: As one shortest transformation is &quot;hit&quot; -> &quot;hot&quot; -> &quot;dot&quot; -> &quot;dog&quot; -> &quot;cog&quot;,
return its length 5.

Example 2:
Input:
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

Output: 0

Explanation: The endWord &quot;cog&quot; is not in wordList, therefore no possible transformation.


"""
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().ladderLength(0) == 0

