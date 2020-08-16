"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

	Players take turns placing characters into empty squares (&quot; &quot;).
	The first player A always places &quot;X&quot; characters, while the second player B always places &quot;O&quot; characters.
	&quot;X&quot; and &quot;O&quot; characters are always placed into empty squares, never on filled ones.
	The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
	The game also ends if all squares are non-empty.
	No more moves can be played if the game is over.

Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return &quot;Draw&quot;, if there are still movements to play return &quot;Pending&quot;.

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 
Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: &quot;A&quot;
Explanation: &quot;A&quot; wins, he always plays first.
&quot;X  &quot;    &quot;X  &quot;    &quot;X  &quot;    &quot;X  &quot;    &quot;X  &quot;
&quot;   &quot; -> &quot;   &quot; -> &quot; X &quot; -> &quot; X &quot; -> &quot; X &quot;
&quot;   &quot;    &quot;O  &quot;    &quot;O  &quot;    &quot;OO &quot;    &quot;OOX&quot;

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: &quot;B&quot;
Explanation: &quot;B&quot; wins.
&quot;X  &quot;    &quot;X  &quot;    &quot;XX &quot;    &quot;XXO&quot;    &quot;XXO&quot;    &quot;XXO&quot;
&quot;   &quot; -> &quot; O &quot; -> &quot; O &quot; -> &quot; O &quot; -> &quot;XO &quot; -> &quot;XO &quot; 
&quot;   &quot;    &quot;   &quot;    &quot;   &quot;    &quot;   &quot;    &quot;   &quot;    &quot;O  &quot;

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: &quot;Draw&quot;
Explanation: The game ends in a draw since there are no moves to make.
&quot;XXO&quot;
&quot;OOX&quot;
&quot;XOX&quot;

Example 4:
Input: moves = [[0,0],[1,1]]
Output: &quot;Pending&quot;
Explanation: The game has not finished yet.
&quot;X  &quot;
&quot; O &quot;
&quot;   &quot;

 
Constraints:
	1 <= moves.length <= 9
	moves[i].length == 2
	0 <= moves[i][j] <= 2
	There are no repeated elements on moves.
	moves follow the rules of tic tac toe.

"""
from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().tictactoe(0) == 0

