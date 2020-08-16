/*
Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

 
Example 1:
Input: text = &quot;ababa&quot;
Output: 3
Explanation: We can swap the first &#39;b&#39; with the last &#39;a&#39;, or the last &#39;b&#39; with the first &#39;a&#39;. Then, the longest repeated character substring is &quot;aaa&quot;, which its length is 3.

Example 2:
Input: text = &quot;aaabaaa&quot;
Output: 6
Explanation: Swap &#39;b&#39; with the last &#39;a&#39; (or the first &#39;a&#39;), and we get longest repeated character substring &quot;aaaaaa&quot;, which its length is 6.

Example 3:
Input: text = &quot;aaabbaaa&quot;
Output: 4

Example 4:
Input: text = &quot;aaaaa&quot;
Output: 5
Explanation: No need to swap, longest repeated character substring is &quot;aaaaa&quot;, length is 5.

Example 5:
Input: text = &quot;abcdef&quot;
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
