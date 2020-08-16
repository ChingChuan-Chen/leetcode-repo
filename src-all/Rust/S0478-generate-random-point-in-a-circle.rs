/*
Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

Note:
	input and output values are in floating-point.
	radius and x-y position of the center of the circle is passed into the class constructor.
	a point on the circumference of the circle is considered to be in the circle.
	randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

Example 1:
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:
Input: 
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution&#39;s constructor has three arguments, the radius, x-position of the center, and y-position of the center of the circle. randPoint has no arguments. Arguments are always wrapped with a list, even if there aren&#39;t any.


*/
pub struct Solution {}
struct Solution {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(radius: f64, x_center: f64, y_center: f64) -> Self {
        
    }
    
    fn rand_point(&self) -> Vec<f64> {
        
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(radius, x_center, y_center);
 * let ret_1: Vec<f64> = obj.rand_point();
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
