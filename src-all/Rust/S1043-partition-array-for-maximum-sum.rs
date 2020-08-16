/*
Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:
Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]

 

Note:
	1 <= K <= A.length <= 500
	0 <= A[i] <= 10^6


*/
pub struct Solution {}
impl Solution {
    pub fn max_sum_after_partitioning(a: Vec<i32>, k: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::max_sum_after_partitioning(0));
  println!("Pass test cases!");
}
