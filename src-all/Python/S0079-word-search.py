"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where &quot;adjacent&quot; cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  [&#39;A&#39;,&#39;B&#39;,&#39;C&#39;,&#39;E&#39;],
  [&#39;S&#39;,&#39;F&#39;,&#39;C&#39;,&#39;S&#39;],
  [&#39;A&#39;,&#39;D&#39;,&#39;E&#39;,&#39;E&#39;]
]

Given word = &quot;ABCCED&quot;, return true.
Given word = &quot;SEE&quot;, return true.
Given word = &quot;ABCB&quot;, return false.

 
Constraints:
	board and word consists only of lowercase and uppercase English letters.
	1 <= board.length <= 200
	1 <= board[i].length <= 200
	1 <= word.length <= 10^3


"""
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().exist(0) == 0

