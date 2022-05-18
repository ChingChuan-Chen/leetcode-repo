/*
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

 
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

 
Constraints:
	m == matrix.length
	n == matrix[i].length
	1 <= m, n <= 1000
	1 <= m * n <= 105
	-109 <= matrix[i][j] <= 109


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.transpose(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
