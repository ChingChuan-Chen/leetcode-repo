/*
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

 

Note:
	1 <= A.length <= 30000
	1 <= A[i] <= 30000

 


*/
pub struct Solution {}
impl Solution {
    pub fn sum_subarray_mins(a: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::sum_subarray_mins(0));
  println!("Pass test cases!");
}
