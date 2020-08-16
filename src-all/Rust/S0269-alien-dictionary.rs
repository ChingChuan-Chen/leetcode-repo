/*
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"

Example 2:
Input:
[
  "z",
  "x"
]

Output: "zx"

Example 3:
Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".

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
