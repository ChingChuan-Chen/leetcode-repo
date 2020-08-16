/*
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.

 
Example 1:
Input: n = 2
Output: [&quot;1/2&quot;]
Explanation: &quot;1/2&quot; is the only unique fraction with a denominator less-than-or-equal-to 2.

Example 2:
Input: n = 3
Output: [&quot;1/2&quot;,&quot;1/3&quot;,&quot;2/3&quot;]

Example 3:
Input: n = 4
Output: [&quot;1/2&quot;,&quot;1/3&quot;,&quot;1/4&quot;,&quot;2/3&quot;,&quot;3/4&quot;]
Explanation: &quot;2/4&quot; is not a simplified fraction because it can be simplified to &quot;1/2&quot;.

Example 4:
Input: n = 1
Output: []

 
Constraints:
	1 <= n <= 100

*/
pub struct Solution {}
impl Solution {
    pub fn simplified_fractions(n: i32) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::simplified_fractions(0));
  println!("Pass test cases!");
}
