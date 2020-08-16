/*
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: S = &quot;ab#c&quot;, T = &quot;ad#c&quot;
Output: true
Explanation: Both S and T become &quot;ac&quot;.

Example 2:
Input: S = &quot;ab##&quot;, T = &quot;c#d#&quot;
Output: true
Explanation: Both S and T become &quot;&quot;.

Example 3:
Input: S = &quot;a##c&quot;, T = &quot;#a#c&quot;
Output: true
Explanation: Both S and T become &quot;c&quot;.

Example 4:
Input: S = &quot;a#c&quot;, T = &quot;b&quot;
Output: false
Explanation: S becomes &quot;c&quot; while T becomes &quot;b&quot;.

Note:
	1 <= S.length <= 200
	1 <= T.length <= 200
	S and T only contain lowercase letters and &#39;#&#39; characters.

Follow up:
	Can you solve it in O(N) time and O(1) space?


*/
pub struct Solution {}
impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::backspace_compare(0));
  println!("Pass test cases!");
}
