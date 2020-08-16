"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters &quot; &quot;, &quot;X&quot;, and &quot;O&quot;.  The &quot; &quot; character represents an empty square.

Here are the rules of Tic-Tac-Toe:

	Players take turns placing characters into empty squares (&quot; &quot;).
	The first player always places &quot;X&quot; characters, while the second player always places &quot;O&quot; characters.
	&quot;X&quot; and &quot;O&quot; characters are always placed into empty squares, never filled ones.
	The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
	The game also ends if all squares are non-empty.
	No more moves can be played if the game is over.

Example 1:
Input: board = [&quot;O  &quot;, &quot;   &quot;, &quot;   &quot;]
Output: false
Explanation: The first player always plays &quot;X&quot;.

Example 2:
Input: board = [&quot;XOX&quot;, &quot; X &quot;, &quot;   &quot;]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = [&quot;XXX&quot;, &quot;   &quot;, &quot;OOO&quot;]
Output: false

Example 4:
Input: board = [&quot;XOX&quot;, &quot;O O&quot;, &quot;XOX&quot;]
Output: true

Note:
	board is a length-3 array of strings, where each string board[i] has length 3.
	Each board[i][j] is a character in the set {&quot; &quot;, &quot;X&quot;, &quot;O&quot;}.


"""
from typing import List
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().validTicTacToe(0) == 0

