/*
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


*/
pub struct Solution {}
impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::solve_n_queens(0));
  println!("Pass test cases!");
}
