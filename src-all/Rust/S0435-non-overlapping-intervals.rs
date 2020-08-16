/*
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don&#39;t need to remove any of the intervals since they&#39;re already non-overlapping.

 

Note:
	You may assume the interval&#39;s end point is always bigger than its start point.
	Intervals like [1,2] and [2,3] have borders &quot;touching&quot; but they don&#39;t overlap each other.


*/
pub struct Solution {}
impl Solution {
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::erase_overlap_intervals(0));
  println!("Pass test cases!");
}
