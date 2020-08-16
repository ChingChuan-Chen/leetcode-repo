"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid. The Sudoku board could be partially filled,
where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
 Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Note:
 A Sudoku board (partially filled) could be valid but is not necessarily solvable.
 Only the filled cells need to be validated according to the mentioned rules. 
 The given board contain only digits 1-9 and the character '.'.
 The given board size is always 9x9.
"""

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9:
            return False
        for i in range(9):
            if len(board[i]) != 9:
                return False

        validate_dict = {}
        for i in range(9):
            for j in range(9):
                validate_dict[f"r{i}"] = set()
                validate_dict[f"c{j}"] = set()
                validate_dict[f"b{i//3},{j//3}"] = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in validate_dict[f"r{i}"] or \
                        board[i][j] in validate_dict[f"c{j}"] or \
                        board[i][j] in validate_dict[f"b{i//3},{j//3}"]:
                        return False
                    validate_dict[f"r{i}"].add(board[i][j])
                    validate_dict[f"c{j}"].add(board[i][j])
                    validate_dict[f"b{i//3},{j//3}"].add(board[i][j])
        return True


if __name__ == '__main__':
    input = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert Solution().isValidSudoku(input) == True
    input[0][0] = "8"
    assert Solution().isValidSudoku(input) == False
