"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  [&#39;o&#39;,&#39;a&#39;,&#39;a&#39;,&#39;n&#39;],
  [&#39;e&#39;,&#39;t&#39;,&#39;a&#39;,&#39;e&#39;],
  [&#39;i&#39;,&#39;h&#39;,&#39;k&#39;,&#39;r&#39;],
  [&#39;i&#39;,&#39;f&#39;,&#39;l&#39;,&#39;v&#39;]
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

 

Note:
	All inputs are consist of lowercase letters a-z.
	The values of words are distinct.


"""
from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().findWords(0) == 0

