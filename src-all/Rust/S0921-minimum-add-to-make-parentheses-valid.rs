/*
Given a string S of &#39;(&#39; and &#39;)&#39; parentheses, we add the minimum number of parentheses ( &#39;(&#39; or &#39;)&#39;, and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

	It is the empty string, or
	It can be written as AB (A concatenated with B), where A and B are valid strings, or
	It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4

 

Note:
	S.length <= 1000
	S only consists of &#39;(&#39; and &#39;)&#39; characters.

 


*/
pub struct Solution {}
impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_add_to_make_valid(0));
  println!("Pass test cases!");
}
