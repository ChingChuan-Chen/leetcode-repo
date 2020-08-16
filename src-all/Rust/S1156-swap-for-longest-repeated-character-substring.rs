/*
Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

 
Example 1:
Input: text = "ababa"
Output: 3
Explanation: We can swap the first &#39;b&#39; with the last &#39;a&#39;, or the last &#39;b&#39; with the first &#39;a&#39;. Then, the longest repeated character substring is "aaa", which its length is 3.

Example 2:
Input: text = "aaabaaa"
Output: 6
Explanation: Swap &#39;b&#39; with the last &#39;a&#39; (or the first &#39;a&#39;), and we get longest repeated character substring "aaaaaa", which its length is 6.

Example 3:
Input: text = "aaabbaaa"
Output: 4

Example 4:
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.

Example 5:
Input: text = "abcdef"
Output: 1

 
Constraints:
	1 <= text.length <= 20000
	text consist of lowercase English characters only.

*/
pub struct Solution {}
impl Solution {
    pub fn max_rep_opt1(text: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::max_rep_opt1(0));
  println!("Pass test cases!");
}
