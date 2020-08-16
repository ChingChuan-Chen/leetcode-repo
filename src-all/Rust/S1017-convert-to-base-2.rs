/*
Given a number N, return a string consisting of &quot;0&quot;s and &quot;1&quot;s that represents its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is &quot;0&quot;.

 

Example 1:
Input: 2
Output: &quot;110&quot;
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2

Example 2:
Input: 3
Output: &quot;111&quot;
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

Example 3:
Input: 4
Output: &quot;100&quot;
Explantion: (-2) ^ 2 = 4

 

Note:
	0 <= N <= 10^9


*/
pub struct Solution {}
impl Solution {
    pub fn base_neg2(n: i32) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::base_neg2(0));
  println!("Pass test cases!");
}
