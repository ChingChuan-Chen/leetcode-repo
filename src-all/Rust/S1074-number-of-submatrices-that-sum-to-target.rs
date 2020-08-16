/*
Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1&#39;, y1&#39;, x2&#39;, y2&#39;) are different if they have some coordinate that is different: for example, if x1 != x1&#39;.

 

Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

 

Note:
	1 <= matrix.length <= 300
	1 <= matrix[0].length <= 300
	-1000 <= matrix[i] <= 1000
	-10^8 <= target <= 10^8

 
Constraints:
	1 <= matrix.length <= 100
	1 <= matrix[0].length <= 100
	-1000 <= matrix[i] <= 1000
	-10^8 <= target <= 10^8


*/
pub struct Solution {}
impl Solution {
    pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::num_submatrix_sum_target(0));
  println!("Pass test cases!");
}
