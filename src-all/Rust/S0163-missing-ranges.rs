/*
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]


*/
pub struct Solution {}
impl Solution {
    pub fn find_missing_ranges(nums: Vec<i32>, lower: i32, upper: i32) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::find_missing_ranges(0));
  println!("Pass test cases!");
}
