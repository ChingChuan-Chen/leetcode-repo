/*
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 &quot;magic square&quot; subgrids are there?  (Each subgrid is contiguous).

 

Example 1:
Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.

Note:
	1 <= grid.length <= 10
	1 <= grid[0].length <= 10
	0 <= grid[i][j] <= 15


*/
pub struct Solution {}
impl Solution {
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::num_magic_squares_inside(0));
  println!("Pass test cases!");
}
