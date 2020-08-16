/*
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]


*/
pub struct Solution {}
impl Solution {
    pub fn group_strings(strings: Vec<String>) -> Vec<Vec<String>> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::group_strings(0));
  println!("Pass test cases!");
}
