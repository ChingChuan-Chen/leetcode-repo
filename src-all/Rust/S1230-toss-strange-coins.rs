/*
You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.

Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.

 
Example 1:
Input: prob = [0.4], target = 1
Output: 0.40000
Example 2:
Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
Output: 0.03125

 
Constraints:
	1 <= prob.length <= 1000
	0 <= prob[i] <= 1
	0 <= target <= prob.length
	Answers will be accepted as correct if they are within 10^-5 of the correct answer.


*/
pub struct Solution {}
impl Solution {
    pub fn probability_of_heads(prob: Vec<f64>, target: i32) -> f64 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::probability_of_heads(0));
  println!("Pass test cases!");
}
