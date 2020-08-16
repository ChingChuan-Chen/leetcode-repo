/*
Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 
Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first &#39;a&#39; in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace &#39;p&#39;, &#39;r&#39;, &#39;a&#39;, &#39;i&#39; and &#39;c&#39; from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

Example 4:
Input: s = "xxyyzz", t = "xxyyzz"
Output: 0

Example 5:
Input: s = "friend", t = "family"
Output: 4

 
Constraints:
	1 <= s.length <= 50000
	s.length == t.length
	s and t contain lower-case English letters only.


*/
pub struct Solution {}
impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_steps(0));
  println!("Pass test cases!");
}
