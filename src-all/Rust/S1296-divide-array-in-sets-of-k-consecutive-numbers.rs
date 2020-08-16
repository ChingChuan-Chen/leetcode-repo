/*
Given an array of integers nums and a positive integer k, find whether it&#39;s possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

 
Example 1:
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

Example 2:
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

Example 3:
Input: nums = [3,3,2,2,1,1], k = 3
Output: true

Example 4:
Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.

 
Constraints:
	1 <= nums.length <= 10^5
	1 <= nums[i] <= 10^9
	1 <= k <= nums.length

Note: This question is the same as 846: https://leetcode.com/problems/hand-of-straights/
*/
pub struct Solution {}
impl Solution {
    pub fn is_possible_divide(nums: Vec<i32>, k: i32) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::is_possible_divide(0));
  println!("Pass test cases!");
}
