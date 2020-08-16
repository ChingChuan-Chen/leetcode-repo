/*
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

 

Note:
	1 <= k <= len(nums) <= 16.
	0 < nums[i] < 10000.


*/
pub struct Solution {}
impl Solution {
    pub fn can_partition_k_subsets(nums: Vec<i32>, k: i32) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::can_partition_k_subsets(0));
  println!("Pass test cases!");
}
