/*
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

 

Note:
	1 <= k <= n <= 30,000.
	Elements of the given array will be in the range [-10,000, 10,000].

 

*/
pub struct Solution {}
impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_max_average(0));
  println!("Pass test cases!");
}
