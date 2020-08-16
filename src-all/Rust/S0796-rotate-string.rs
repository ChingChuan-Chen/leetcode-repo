/*
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = &#39;abcde&#39;, then it will be &#39;bcdea&#39; after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = &#39;abcde&#39;, B = &#39;cdeab&#39;
Output: true

Example 2:
Input: A = &#39;abcde&#39;, B = &#39;abced&#39;
Output: false

Note:
	A and B will have length at most 100.


*/
pub struct Solution {}
impl Solution {
    pub fn rotate_string(a: String, b: String) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::rotate_string(0));
  println!("Pass test cases!");
}
