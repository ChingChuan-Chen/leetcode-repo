"""
Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.

 

Example 1:
Input: text = &quot;thestoryofleetcodeandme&quot;, words = [&quot;story&quot;,&quot;fleet&quot;,&quot;leetcode&quot;]
Output: [[3,7],[9,13],[10,17]]

Example 2:
Input: text = &quot;ababa&quot;, words = [&quot;aba&quot;,&quot;ab&quot;]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: 
Notice that matches can overlap, see &quot;aba&quot; is found in [0,2] and [2,4].

 

Note:
	All strings contains only lowercase English letters.
	It&#39;s guaranteed that all strings in words are different.
	1 <= text.length <= 100
	1 <= words.length <= 20
	1 <= words[i].length <= 50
	Return the pairs [i,j] in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their second coordinate).

"""
from typing import List
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        
        pass


if __name__ == '__main__':
    assert Solution().indexPairs(0) == 0

