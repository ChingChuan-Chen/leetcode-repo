/*
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 
Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

 
Constraints:
	rows == matrix.length
	cols == matrix[i].length
	1 <= row, cols <= 200
	matrix[i][j] is '0' or '1'.


*/
#include <cassert>
#include <iostream>

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.maximalRectangle(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
