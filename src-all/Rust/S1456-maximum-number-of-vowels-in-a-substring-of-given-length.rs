/*
Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

 
Example 1:
Input: s = &quot;abciiidef&quot;, k = 3
Output: 3
Explanation: The substring &quot;iii&quot; contains 3 vowel letters.

Example 2:
Input: s = &quot;aeiou&quot;, k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = &quot;leetcode&quot;, k = 3
Output: 2
Explanation: &quot;lee&quot;, &quot;eet&quot; and &quot;ode&quot; contain 2 vowels.

Example 4:
Input: s = &quot;rhythms&quot;, k = 4
Output: 0
Explanation: We can see that s doesn&#39;t have any vowel letters.

Example 5:
Input: s = &quot;tryhard&quot;, k = 4
Output: 1

 
Constraints:
	1 <= s.length <= 10^5
	s consists of lowercase English letters.
	1 <= k <= s.length

*/
pub struct Solution {}
impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::max_vowels(0));
  println!("Pass test cases!");
}
