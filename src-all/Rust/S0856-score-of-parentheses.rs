/*
Given a balanced parentheses string S, compute the score of the string based on the following rule:

	() has score 1
	AB has score A + B, where A and B are balanced parentheses strings.
	(A) has score 2 * A, where A is a balanced parentheses string.

 

Example 1:
Input: &quot;()&quot;
Output: 1

Example 2:
Input: &quot;(())&quot;
Output: 2

Example 3:
Input: &quot;()()&quot;
Output: 2

Example 4:
Input: &quot;(()(()))&quot;
Output: 6

 

Note:
	S is a balanced parentheses string, containing only ( and ).
	2 <= S.length <= 50


*/
pub struct Solution {}
impl Solution {
    pub fn score_of_parentheses(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::score_of_parentheses(0));
  println!("Pass test cases!");
}
