"""
The n-queens puzzle is the problem of placing n queens on an n&times;n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


"""
from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        pass


if __name__ == '__main__':
    assert Solution().solveNQueens(0) == 0

