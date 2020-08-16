/*
Given a list of intervals, remove all intervals that are covered by another interval in the list. Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 
Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

 
Constraints:
	1 <= intervals.length <= 1000
	0 <= intervals[i][0] < intervals[i][1] <= 10^5
	intervals[i] != intervals[j] for all i != j


*/
pub struct Solution {}
impl Solution {
    pub fn remove_covered_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::remove_covered_intervals(0));
  println!("Pass test cases!");
}
