/*
Balanced strings are those who have equal quantity of &#39;L&#39; and &#39;R&#39; characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 
Example 1:
Input: s = &quot;RLRRLLRLRL&quot;
Output: 4
Explanation: s can be split into &quot;RL&quot;, &quot;RRLL&quot;, &quot;RL&quot;, &quot;RL&quot;, each substring contains same number of &#39;L&#39; and &#39;R&#39;.

Example 2:
Input: s = &quot;RLLLLRRRLR&quot;
Output: 3
Explanation: s can be split into &quot;RL&quot;, &quot;LLLRRR&quot;, &quot;LR&quot;, each substring contains same number of &#39;L&#39; and &#39;R&#39;.

Example 3:
Input: s = &quot;LLLLRRRR&quot;
Output: 1
Explanation: s can be split into &quot;LLLLRRRR&quot;.

Example 4:
Input: s = &quot;RLRRRLLRLL&quot;
Output: 2
Explanation: s can be split into &quot;RL&quot;, &quot;RRRLLRLL&quot;, since each substring contains an equal number of &#39;L&#39; and &#39;R&#39;

 
Constraints:
	1 <= s.length <= 1000
	s[i] = &#39;L&#39; or &#39;R&#39;


*/
pub struct Solution {}
impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::balanced_string_split(0));
  println!("Pass test cases!");
}
