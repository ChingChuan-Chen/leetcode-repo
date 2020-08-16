/*
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Input:
[
  &quot;wrt&quot;,
  &quot;wrf&quot;,
  &quot;er&quot;,
  &quot;ett&quot;,
  &quot;rftt&quot;
]

Output: &quot;wertf&quot;

Example 2:
Input:
[
  &quot;z&quot;,
  &quot;x&quot;
]

Output: &quot;zx&quot;

Example 3:
Input:
[
  &quot;z&quot;,
  &quot;x&quot;,
  &quot;z&quot;
] 

Output: &quot;&quot; 

Explanation: The order is invalid, so return &quot;&quot;.

Note:
	You may assume all letters are in lowercase.
	If the order is invalid, return an empty string.
	There may be multiple valid order of letters, return any one of them is fine.


*/
pub struct Solution {}
impl Solution {
    pub fn alien_order(words: Vec<String>) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::alien_order(0));
  println!("Pass test cases!");
}
