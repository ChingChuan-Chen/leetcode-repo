/*
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input:  [0,1,2,4,5,7]
Output: [&quot;0->2&quot;,&quot;4->5&quot;,&quot;7&quot;]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:
Input:  [0,2,3,4,6,8,9]
Output: [&quot;0&quot;,&quot;2->4&quot;,&quot;6&quot;,&quot;8->9&quot;]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


*/
pub struct Solution {}
impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::summary_ranges(0));
  println!("Pass test cases!");
}
