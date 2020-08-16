/*
Given a 2D grid, each cell is either a wall &#39;W&#39;, an enemy &#39;E&#39; or empty &#39;0&#39; (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.


*/
pub struct Solution {}
impl Solution {
    pub fn max_killed_enemies(grid: Vec<Vec<char>>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::max_killed_enemies(0));
  println!("Pass test cases!");
}
