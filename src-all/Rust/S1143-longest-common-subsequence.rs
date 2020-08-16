/*
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, &quot;ace&quot; is a subsequence of &quot;abcde&quot; while &quot;aec&quot; is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 
Example 1:
Input: text1 = &quot;abcde&quot;, text2 = &quot;ace&quot; 
Output: 3  
Explanation: The longest common subsequence is &quot;ace&quot; and its length is 3.

Example 2:
Input: text1 = &quot;abc&quot;, text2 = &quot;abc&quot;
Output: 3
Explanation: The longest common subsequence is &quot;abc&quot; and its length is 3.

Example 3:
Input: text1 = &quot;abc&quot;, text2 = &quot;def&quot;
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

 
Constraints:
	1 <= text1.length <= 1000
	1 <= text2.length <= 1000
	The input strings consist of lowercase English characters only.


*/
pub struct Solution {}
impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::longest_common_subsequence(0));
  println!("Pass test cases!");
}
