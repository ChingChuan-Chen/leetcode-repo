"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. You must do it in place.

Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List
import copy


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row/col as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == '__main__':
    x = [[1], [0]]
    Solution().setZeroes(x)
    assert x == [[0], [0]]
    x = [[0, 1, 1], [1, 1, 1], [1, 0, 0]]
    Solution().setZeroes(x)
    assert x == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    x = [[2147483647], [2], [3]]
    Solution().setZeroes(x)
    assert x == [[2147483647], [2], [3]]
    x = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    Solution().setZeroes(x)
    assert x == [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    x = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(x)
    assert x == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    x = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(x)
    assert x == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
