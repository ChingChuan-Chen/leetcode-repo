/*
You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to minimize the number of calls to system&#39;s Math.random() and optimize the time and space complexity.

Note:
	1 <= n_rows, n_cols <= 10000
	0 <= row.id < n_rows and 0 <= col.id < n_cols
	flip will not be called when the matrix has no 0 values left.
	the total number of calls to flip and reset will not exceed 1000.

Example 1:
Input: 
[&quot;Solution&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;flip&quot;]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]

Example 2:
Input: 
[&quot;Solution&quot;,&quot;flip&quot;,&quot;flip&quot;,&quot;reset&quot;,&quot;flip&quot;]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution&#39;s constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren&#39;t any.

*/
pub struct Solution {}
struct Solution {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(n_rows: i32, n_cols: i32) -> Self {
        
    }
    
    fn flip(&self) -> Vec<i32> {
        
    }
    
    fn reset(&self) {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(n_rows, n_cols);
 * let ret_1: Vec<i32> = obj.flip();
 * obj.reset();
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
