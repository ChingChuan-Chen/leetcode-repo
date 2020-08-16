"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters &#39;R&#39;, &#39;.&#39;, &#39;B&#39;, and &#39;p&#39; respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

 

Example 1:
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.

Example 2:
Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.

Example 3:
Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.

 

Note:
	board.length == board[i].length == 8
	board[i][j] is either &#39;R&#39;, &#39;.&#39;, &#39;B&#39;, or &#39;p&#39;
	There is exactly one cell with board[i][j] == &#39;R&#39;


"""
from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numRookCaptures(0) == 0

