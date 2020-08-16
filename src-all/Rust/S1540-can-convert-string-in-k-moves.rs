/*
Given two strings s and t, your goal is to convert s into t in k moves or less.

During the ith (1 <= i <= k) move you can:

	Choose any index j (1-indexed) from s, such that 1 <= j <= s.length and j has not been chosen in any previous move, and shift the character at that index i times.
	Do nothing.

Shifting a character means replacing it by the next letter in the alphabet (wrapping around so that &#39;z&#39; becomes &#39;a&#39;). Shifting a character by i means applying the shift operations i times.

Remember that any index j can be picked at most once.

Return true if it&#39;s possible to convert s into t in no more than k moves, otherwise return false.

 
Example 1:
Input: s = "input", t = "ouput", k = 9
Output: true
Explanation: In the 6th move, we shift &#39;i&#39; 6 times to get &#39;o&#39;. And in the 7th move we shift &#39;n&#39; to get &#39;u&#39;.

Example 2:
Input: s = "abc", t = "bcd", k = 10
Output: false
Explanation: We need to shift each character in s one time to convert it into t. We can shift &#39;a&#39; to &#39;b&#39; during the 1st move. However, there is no way to shift the other characters in the remaining moves to obtain t from s.

Example 3:
Input: s = "aab", t = "bbb", k = 27
Output: true
Explanation: In the 1st move, we shift the first &#39;a&#39; 1 time to get &#39;b&#39;. In the 27th move, we shift the second &#39;a&#39; 27 times to get &#39;b&#39;.

 
Constraints:
	1 <= s.length, t.length <= 10^5
	0 <= k <= 10^9
	s, t contain only lowercase English letters.


*/
pub struct Solution {}
impl Solution {
    pub fn can_convert_string(s: String, t: String, k: i32) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::can_convert_string(0));
  println!("Pass test cases!");
}
